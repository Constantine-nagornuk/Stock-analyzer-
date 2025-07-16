import yfinance as yf
from datetime import datetime

ticker = yf.Ticker("TSLA")
news_items = ticker.news  # List of dicts

# Display the latest 5 stories, or fewer if there aren't that many
for item in news_items[:10]:
    content = item.get("content", {})  # Some responses wrap details under 'content'
    
    title = content.get("title", "No Title")
    summary = content.get("summary", "No summary available.")
    provider = content.get("provider", {}).get("displayName", "Unknown Source")
    pub_date = content.get("pubDate", "Unknown Time")
    url = (
        (content.get("clickThroughUrl") or {}).get("url")
        or (content.get("canonicalUrl") or {}).get("url")
        or "No URL"
    )


    # Format publication date nicely
    try:
        pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ")
        pub_date = pub_date.strftime("%b %d, %Y %I:%M %p")
    except:
        pass

    print(f"📰 Title: {title}")
    print(f"📄 Summary: {summary}")
    print(f"🌐 Source: {provider}")
    print(f"🕓 Published: {pub_date}")
    print(f"🔗 Link: {url}")
    print("-" * 80)
