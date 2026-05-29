from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    content = "העיתון מתעדכן..."
    if os.path.exists("news_data.txt"):
        with open("news_data.txt", "r", encoding="utf-8") as f:
            content = f.read()
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(port=5000)