import feedparser

# 10 המקורות הכי יציבים (למנוע עומס על ה-AI)
urls = [
    "https://www.ynet.co.il/Integration/StoryRss1854.xml",
    "https://rss.walla.co.il/feed/22",
    "https://www.israelhayom.co.il/rss.xml",
    "https://www.globes.co.il/feed/news-rss.xml"
]

def update_news():
    news_text = ""
    for url in urls:
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                # לוקחים רק כותרת אחת לכל מקור כדי לשמור על קובץ קטן
                news_text += f"{feed.entries[0].title}\n"
        except: continue

    # כאן אתה שולח ל-AI. 
    # טיפ: בקש ממנו "כתוב תגובה קצרה וממוקדת בפורמט HTML"
    ai_html = "<h2>סקירה</h2><p>ניתוח קצר...</p>" 
    
    html_content = f"""
    <html><body dir="rtl">
    <h1>עיתון ה-AI</h1>
    {ai_html}
    </body></html>
    """
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    update_news()