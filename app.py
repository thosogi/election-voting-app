from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # CORSをすべて許可

# ベースディレクトリを定義
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOTES_FILE = os.path.join(BASE_DIR, 'votes.txt')
MOVIES_DIR = os.path.join(BASE_DIR, 'movies')

def save_vote_to_file(candidate):
    """投票をファイルに保存"""
    with open(VOTES_FILE, 'a') as f:
        f.write(f'{candidate}\n')

def read_votes_from_file():
    """ファイルから投票結果を読み込む"""
    try:
        with open(VOTES_FILE, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

@app.route('/')
def serve_index():
    """トップページを返す"""
    return send_from_directory(BASE_DIR, 'front.html')

@app.route('/movies/<path:filename>')
def serve_movies(filename):
    """moviesフォルダ内の動画を提供"""
    return send_from_directory(MOVIES_DIR, filename)

@app.route('/submit-vote', methods=['POST'])
def submit_vote():
    """投票を受け取り、ファイルに保存"""
    data = request.json
    candidate = data.get('candidate')
    if candidate in ['A', 'B', 'C']:
        save_vote_to_file(candidate)
        return jsonify({'message': 'Vote submitted successfully'}), 200
    return jsonify({'message': 'Invalid candidate'}), 400

@app.route('/results', methods=['GET'])
def get_results():
    """投票結果を集計して返す"""
    from collections import Counter
    votes = read_votes_from_file()
    results = Counter(votes)
    return jsonify(results)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=False)
