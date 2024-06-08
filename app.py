from flask import Flask
import google.generativeai as genai
from collections.abc import MutableMapping  # Correct import
from apscheduler.schedulers.background import BackgroundScheduler

# Configure the API key
api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/news/<category>', methods=['POST'])
def generate_news(category: str):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate 5 specific news about {category}"
    response = model.generate_content(prompt)
    return response.text  # Use jsonify to return a proper JSON response

sched = BackgroundScheduler(daemon=True)
sched.add_job(hello_world, 'interval', seconds=10)
sched.start()

if __name__ == '__main__':
    app.run()
