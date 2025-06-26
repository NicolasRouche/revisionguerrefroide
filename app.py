from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)
SCORES_FILE = 'scores.json'

@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            try:
                scores = json.load(f)
            except json.JSONDecodeError:
                scores = []
    else:
        scores = []

    data['date'] = datetime.now().isoformat()
    scores.append(data)

    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
