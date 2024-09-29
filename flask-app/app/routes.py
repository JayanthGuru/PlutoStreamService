# app/routes/__init__.py
from flask import Blueprint, request
from app.controllers import get_lyrics

api = Blueprint('api', __name__)

# Public Endpoints
@api.route('/lyrics/<song_name>', methods=['GET'])
def lyrics(song_name):
    return get_lyrics(song_name)

@api.route('/songs/<song_name>', methods=['GET'])
def song(song_name):
    pass

@api.route('/bgms/<song_name>', methods=['GET'])
def bgm(song_name):
    pass

@api.route('/<song_name>', methods=['GET'])
def full_details(song_name):
    # Implement logic to get full details (metadata, lyrics, etc.)
    pass

# Admin Endpoints
@api.route('/songs', methods=['POST'])
def new_song():
    data = request.get_json()
    pass

@api.route('/songs/<song_id>', methods=['PUT', 'PATCH'])
def update_song(song_id):
    data = request.get_json()
    pass

@api.route('/songs/<song_id>', methods=['DELETE'])
def remove_song(song_id):
    pass
