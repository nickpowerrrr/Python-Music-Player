import json
import os


from get_asset_path import get_asset_path
from classes import SongData
from find_file_type import find_file_type

DATA_FOLDER = get_asset_path("assets\\data")
MUSIC_FOLDER = get_asset_path("assets\\music")
SONGS_DATA_PATH = os.path.join(DATA_FOLDER, "songs_data.json")

SUPPORTED_SONG_TYPES = {".mp3", ".wav"}
SUPPORTED_ICON_TYPES = {".jpeg", ".png", ".jpg"}


def create_song_data(song_name: str):
    
    current_relative_path = f"assets\\music\\{song_name}"
    song_file_path = None
    song_icon_path = None
    for file_type in SUPPORTED_SONG_TYPES:
        _, relative_path = find_file_type(current_relative_path, file_type)
        if relative_path:
            song_file_path = relative_path
    if not song_file_path:
        raise FileNotFoundError(f"Couldnt find music file for: {song_name}!")

    for file_type in SUPPORTED_ICON_TYPES:
        _, relative_path = find_file_type(current_relative_path, file_type)
        if relative_path:
            song_icon_path = relative_path
    if not song_icon_path:
        song_icon_path = "assets\\images\\default_icon.png"

    data: SongData = {
        "name": song_name,
        "song_file_path": song_file_path,
        "song_icon_path": song_icon_path,
    }
    json_str = json.dumps(data, indent=4)
    with open(SONGS_DATA_PATH, "w") as f:
        f.write(json_str)
