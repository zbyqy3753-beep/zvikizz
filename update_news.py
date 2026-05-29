# update_news.py
import feedparser
import requests

def update():
    # סריקה
    sources = ["https://www.ynet.co.il/Integration/StoryRss1854.xml"] # צמצם ל-3 מקורות בלבד למניעת עומס
    news_text = ""
    for url in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]: news_text += entry.title + "\n"
    
    # שליחה ל-AI
    url = "http://localhost:11434/api/generate"
    payload = {"model": "gemma3:4b", "prompt": f"סכם לי את החדשות: {news_text}", "stream": False}
    try:
        response = requests.post(url, json=payload, timeout=120)
        with open("news_cache.txt", "w", encoding="utf-8") as f:
            f.write(response.json()['response'])
        print("העיתון עודכן!")
    except Exception as e:
        print(f"שגיאה בעדכון: {e}")

if __name__ == "__main__":
    update()