import feedparser

# רשימת ה-RSS שלך
urls = [
    "https://www.ynet.co.il/Integration/StoryRss1854.xml",
    "https://rss.walla.co.il/feed/22"
]

def get_ai_content(raw_news):
    # כאן אתה קורא ל-AI שלך. 
    # חשוב: תחזיר רק טקסט HTML תקין, ללא {{ }}
    return f"<h2>סיכום היום</h2><p>הנה חדשות היום: {raw_news[:200]}...</p>"

def run_newspaper():
    # 1. איסוף נתונים
    news_items = []
    for url in urls:
        feed = feedparser.parse(url)
        if feed.entries:
            news_items.append(feed.entries[0].title)
    
    raw_news = " | ".join(news_items)
    
    # 2. קבלת התוכן מה-AI
    ai_html_content = get_ai_content(raw_news)
    
    # 3. יצירת ה-HTML הסופי (נקי מ-Jinja)
    final_html = f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="he">
    <head>
        <meta charset="UTF-8">
        <title>עיתון ה-AI</title>
        <style>
            body {{ font-family: sans-serif; background: #eee; padding: 20px; }}
            .card {{ background: white; padding: 20px; border-radius: 8px; max-width: 600px; margin: auto; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📰 עיתון ה-AI היומי</h1>
            {ai_html_content}
        </div>
    </body>
    </html>
    """
    
    # 4. שמירה כ-index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

if __name__ == "__main__":
    run_newspaper()
