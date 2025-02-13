web_api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"status": "Atomic Nexus AI is running"})

if __name__ == '__main__':
    app.run(debug=True)