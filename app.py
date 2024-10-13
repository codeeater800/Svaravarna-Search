from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Render Hosting Test</h1><p>This is a test deployment on Render using Gunicorn and Flask.</p>"

@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Hello from the backend!"})
