# news_fetcher.py

import yfinance as yf
from datetime import datetime

def Display_News(Stock):
    news_items = Stock.news
    parsed_news = []

    for item in news_items[:10]:
        content = item.get("content", {})
        title = content.get("title", "No Title")
        summary = content.get("summary", "No summary available.")
        provider = content.get("provider", {}).get("displayName", "Unknown Source")
        pub_date = content.get("pubDate", "Unknown Time")
        url = (
            (content.get("clickThroughUrl") or {}).get("url")
            or (content.get("canonicalUrl") or {}).get("url")
            or "No URL"
        )
        try:
            pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ")
            pub_date = pub_date.strftime("%b %d, %Y %I:%M %p")
        except:
            pass

        parsed_news.append({
            "title": title,
            "summary": summary,
            "provider": provider,
            "pub_date": pub_date,
            "url": url
        })

    return parsed_news
