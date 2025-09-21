from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging

# -----------------------------
# Task Functions
# -----------------------------

def scrape_reviews(**context):
    try:
        logging.info("Starting scraping...")
        # call your scraping logic here
        scraped_count = 120  # Example
        context['ti'].xcom_push(key='scraped_count', value=scraped_count)
        logging.info(f"Scraping completed. Records: {scraped_count}")
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        # Raise only if it's critical; otherwise skip gracefully
        raise

def validate_and_store(**context):
    scraped_count = context['ti'].xcom_pull(key='scraped_count', task_ids='scrape_task')
    logging.info(f"Validating {scraped_count} records...")
    # Add validation + DB insert logic here
    logging.info("Validation and storage complete.")

def filter_and_export(**context):
    logging.info("Filtering and exporting data...")
    # Add filtering, export, or API push logic here
    logging.info("Filtering/export complete.")

def log_summary(**context):
    scraped_count = context['ti'].xcom_pull(key='scraped_count', task_ids='scrape_task')
    logging.info("=== RUN SUMMARY ===")
    logging.info(f"Run Date: {datetime.now()}")
    logging.info(f"Records processed: {scraped_count}")
    logging.info("===================")

# -----------------------------
# DAG Definition
# -----------------------------

default_args = {
    'owner': 'auto-intel',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

with DAG(
    dag_id='auto_review_pipeline',
    default_args=default_args,
    description='Automated daily scraping and processing of automotive reviews',
    schedule_interval='@daily',   # Runs every 24 hours
    start_date=datetime(2025, 9, 6),
    catchup=False,
    max_active_runs=1,
    tags=['scraping', 'automation', 'auto-intel'],
) as dag:

    scrape_task = PythonOperator(
        task_id='scrape_task',
        python_callable=scrape_reviews,
        provide_context=True,
    )

    validate_task = PythonOperator(
        task_id='validate_task',
        python_callable=validate_and_store,
        provide_context=True,
    )

    filter_task = PythonOperator(
        task_id='filter_task',
        python_callable=filter_and_export,
        provide_context=True,
    )

    log_task = PythonOperator(
        task_id='log_task',
        python_callable=log_summary,
        provide_context=True,
        trigger_rule='all_done',  # Runs even if earlier tasks fail
    )

    # Task flow
    scrape_task >> validate_task >> filter_task >> log_task

# Install Airflow
# !pip install apache-airflow
