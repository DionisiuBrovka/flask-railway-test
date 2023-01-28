from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status":200})

@app.route('/api/getMe')
def apiGetMe():
    response = requests.get(f"https://api.telegram.org/bot{HTTP_TOKEN}/getMe")
    return response.json()


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
