from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Hello from the backend!"})

# No need to include __main__ as Gunicorn will handle the app initialization
