# 🚗 Automotive BI System

### Design and Implementation of a Business Intelligence System for Automotive News and Reviews

This project demonstrates a complete end-to-end data pipeline integrating **web scraping**, **data validation**, **PostgreSQL storage**, **API connectivity**, and **interactive dashboards** for actionable automotive insights.  
It was developed as part of my **Master’s Dissertation**, completed with *Distinction (2025)*.

---

## 🧩 Project Overview
The rise of digital platforms has created an explosion of online automotive reviews — a rich but unstructured source of market intelligence for manufacturers, dealers, and consumers.  
However, extracting meaningful insights from these dispersed, unstructured reviews remains a major challenge.

This project addresses that gap by building a **modular and ethical data pipeline** capable of:
1. Acquiring automotive reviews and news from multiple sources (with `robots.txt` compliance)  
2. Validating and cleaning data using a **Pydantic-based schema**  
3. Structuring and storing data in **PostgreSQL**  
4. Creating a lightweight **API layer** to connect the database and the dashboard  
5. Filtering and analysing sentiment and brand-specific content  
6. Visualising results through an interactive **Matplotlib/Plotly** dashboard  

---

## ⚙️ System Architecture
**Core modules include:**
- **Data Acquisition:** Web scraping pipeline built with Python and BeautifulSoup/Requests, respecting website policies and rate limits.  
- **Data Validation:** Schema enforcement using **Pydantic**, ensuring clean and consistent data ingestion.  
- **Data Storage:** PostgreSQL database designed for scalability and efficient querying.  
- **API Layer:** A RESTful API built using **FastAPI** (or Flask) to connect the PostgreSQL backend with the dashboard interface, enabling dynamic data retrieval and updates.  
- **Analysis & Filtering:** Targeted sentiment analysis and keyword filtering to identify trends by brand or category.  
- **Visualization:** Interactive dashboards built with **Plotly Dash** and **Matplotlib**, enabling both high-level summaries and detailed inspection.

---

## 📊 Dashboard Features
- Sentiment distribution charts for brand perception tracking  
- Review volume trends over time  
- Filterable and exportable review tables  
- Real-time data retrieval through API connection  
- Quick, visual insights to support decision-making  

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|-------------|
| Language | Python |
| Database | PostgreSQL |
| Data Validation | Pydantic |
| API | FastAPI / Flask |
| Web Scraping | Requests, BeautifulSoup |
| Visualization | Plotly, Matplotlib |
| Data Export | CSV, Excel |
| Deployment | Local / Cloud-ready |

---

## 🚀 Results
- Successful ingestion, validation, and visualisation of multiple automotive review datasets  
- Reliable API-based integration between the database and the dashboard  
- High data accuracy and completeness through strict validation models  
- Exportable dashboards enabling both **trend-level** and **record-level** insights  
- Extensible design — adaptable to other domains beyond automotive reviews  

---

## 🔍 Future Enhancements
- Integration of **NLP-based sentiment classification**  
- Addition of **asynchronous scraping** for scalability  
- Enhanced **filtering and dashboard interactivity**  
- Cloud deployment and automated ETL scheduling  

---

## 🧾 Keywords
`Automotive Reviews` · `Web Scraping` · `Data Validation` · `PostgreSQL` · `API Integration` · `Sentiment Analysis` · `Data Visualization` · `Plotly` · `Matplotlib` · `Pydantic` · `Market Intelligence`
