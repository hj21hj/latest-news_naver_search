import requests
import os
from datetime import datetime

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
SEARCH_QUERY = "한국언론진흥재단 OR 언론진흥재단 OR 언론재단 or KPF or 정부광고"  # 원하는 검색어

def get_naver_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {
        "query": query,
        "display": 5,
        "sort": "date"
    }

    response = requests.get(url, headers=headers, params=params)
    items = response.json().get("items", [])
    return items

def update_readme(items):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"# 📰 최신 뉴스 - {SEARCH_QUERY}\n")
        f.write(f"업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for item in items:
            title = item['title'].replace("<b>", "").replace("</b>", "")
            link = item['link']
            f.write(f"- [{title}]({link})\n")

if __name__ == "__main__":
    news_items = get_naver_news(SEARCH_QUERY)
    update_readme(news_items)
