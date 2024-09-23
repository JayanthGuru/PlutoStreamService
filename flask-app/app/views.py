from flask import Flask, request, jsonify
from app import app
# from app.controllers import add_user, get_users

app = Flask(__name__)

# User Endpoints
@app.route('/lyrics/<song_name>', methods=['GET'])
def get_lyrics(song_name):
    return jsonify({"lyrics": "Lyrics for " + song_name})

@app.route('/songs/<song_name>', methods=['GET'])
def get_song(song_name):
    return jsonify({"song": "Song data for " + song_name})

@app.route('/bgms/<song_name>', methods=['GET'])
def get_bgm(song_name):
    return jsonify({"bgm": "BGM data for " + song_name})

app.route('/<song_name>', methods=['GET'])
def get_full_details(song_name):
    """
    Should return all the details like metadata and lyrics.
    """
    return jsonify({"details": "Full details"})




# Admin Endpoints
@app.route('/songs', methods=['POST'])
def add_song():
    data = request.get_json()
    return jsonify({"message": "Song added"}), 201

@app.route('/songs/<song_id>', methods=['PUT', 'PATCH'])
def edit_song(song_id):
    data = request.get_json()
    return jsonify({"message": "Song updated"})

@app.route('/songs/<song_id>', methods=['DELETE'])
def delete_song(song_id):
    return jsonify({"message": "Song deleted"})
