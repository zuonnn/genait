from flask import Flask, request
import google.generativeai as genai
# from crontab import CronTab
import threading
import schedule
import time
import sys
import signal
# Configure the API key
api_key = "AIzaSyCpSIq8LG5rr7TRqeI33tSXXTyjvj_U8Xg"
genai.configure(api_key=api_key)

app = Flask(__name__)

category = ['football', 'basketball', 'badminton', 'cricket']
scheduler_running = True  

def scheduled_task():
    schedule.every(24).hours.do(generate_news_by_category)
    while scheduler_running:  
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def hello_world():
    print("Hello World!")  
    return 'Hello World!'

@app.route('/news/<category>', methods=['POST'])
def generate_news(category: str):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate 5 specific news about {category}"
    response = model.generate_content(prompt)    
    return response.text

@app.route('/news', methods=['GET'])
def generate_news_by_category():
    category = ['football', 'basketball', 'badminton', 'cricket']
    news = {}

    model = genai.GenerativeModel('gemini-1.5-flash')

    for cat in category:
        prompt = f"Generate 5 specific news for {cat}"
        response = model.generate_content(prompt)
        news[cat] = response.text
    return news

def signal_handler(sig, frame):
    global scheduler_running  
    scheduler_running = False  
    sys.exit(0)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=scheduled_task)
    scheduler_thread.start()
    signal.signal(signal.SIGINT, signal_handler)  
    try:
        app.run()  
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)  