from flask import Flask, request
import google.generativeai as genai
# from crontab import CronTab
import threading
import schedule
import time
import sys
# Configure the API key
api_key = "AIzaSyCpSIq8LG5rr7TRqeI33tSXXTyjvj_U8Xg"
genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello World!")  # Print to stdout, which cron can capture
    return 'Hello World!'

def scheduled_task():
    schedule.every(24).hours.do(generate_news)
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/news/<category>', methods=['POST'])
def generate_news(category: str):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate 5 specific news about {category}"
    response = model.generate_content(prompt)    
    return response.text

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=scheduled_task)
    scheduler_thread.start()
    try:
        app.run(debug=True)  # Run Flask app in debug mode
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
