# Scrapy settings for auto_intel project

BOT_NAME = "auto_intel"

SPIDER_MODULES = ["auto_intel.spiders"]
NEWSPIDER_MODULE = "auto_intel.spiders"

# --- Main Configuration ---
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1.5
CONCURRENT_REQUESTS = 4
FEED_EXPORT_ENCODING = "utf-8"

# --- Pipelines ---
# This now correctly points to the PostgresPipeline class
ITEM_PIPELINES = {
    'auto_intel.pipelines.PostgresPipeline': 300,
}

# --- Middlewares ---
DOWNLOADER_MIDDLEWARES = {
    'auto_intel.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, # Disable default
    'auto_intel.middlewares.AutoIntelDownloaderMiddleware': 543,
}

# --- User Agents ---
# This list will be used by the RandomUserAgentMiddleware
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
]