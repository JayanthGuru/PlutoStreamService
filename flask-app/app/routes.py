# app/routes/__init__.py
from flask import Blueprint, request
from app.controllers import DataBaseManager

api = Blueprint('api', __name__)
DBManager = DataBaseManager()

# Public Endpoints
@api.route('/lyrics/<song_name>', methods=['GET'])
def lyrics(song_name):
    print("song_name ",song_name)
    DBManager.get_lyrics(song_name)

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
@api.route('/admin/records', methods=['POST'])
def add_record():
    data = request.get_json()
    print("Add_records")
    DBManager.add_row(data)
    return {"status_message": "fuck off"}, 200

@api.route('/admin/records/<song_name>', methods=['PUT', 'PATCH'])
def update_record(song_name):
    data = request.get_json()
    print("song_name", song_name)
    print("Update_records")
    return {"status_message": "fuck off"}, 200

@api.route('/admin/records/<song_name>', methods=['DELETE'])
def remove_record(song_name):
    data = request.get_json()
    print("song_name", song_name)
    print("Delete_records")
    return {"status_message": "fuck off"}, 200
