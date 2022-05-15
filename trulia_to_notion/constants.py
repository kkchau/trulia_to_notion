import os

# Trulia
TRULIA_BASE_URL = "https://www.trulia.com"
TRULIA_QUERY_ENDPOINT = "for_sale/37.31454,37.52585,-122.12055,-121.7992_xy/3p_beds/2p_baths/800000-1500000_price/1000p_sqft/SINGLE-FAMILY_HOME_type/date;d_sort/0.0459p_ls/0-200_hoa/12_zm/"
SCRAPE_HEADERS = {
    "Content-Type": "text/html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
}

# Notion
NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_AUTH_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_AUTH_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
}

NOTION_DATABASE_ID = "92ec2168f53d481d81baa34962bb3ea6"