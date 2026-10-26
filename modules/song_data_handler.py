import json
import os

from classes import *
from find_file_type import find_file_type
from get_asset_path import get_asset_path

DATA_FOLDER = get_asset_path("assets/data")
MUSIC_FOLDER = get_asset_path("assets/music")
SONGS_DATA_PATH = os.path.join(DATA_FOLDER, "songs_data.json")

SUPPORTED_SONG_TYPES = (".mp3", ".wav")
SUPPORTED_ICON_TYPES = (".jpeg", ".png", ".jpg")


def create_song_data(song_name: str):
    if os.path.exists(SONGS_DATA_PATH):
        with open(SONGS_DATA_PATH, "r") as f:
            song_json_data = json.load(f)
            if song_json_data[song_name]:
                print("Song data already exists for:", song_name, "!")
                return

    current_relative_path = f"assets/music/{song_name}"
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
        song_icon_path = "assets/images/default_icon.png"

    data: SongInfo = {
        song_name: {
            "song_file_path": song_file_path,
            "song_icon_path": song_icon_path,
        }
    }
    json_str = json.dumps(data, indent=4)
    with open(SONGS_DATA_PATH, "w") as f:
        f.write(json_str)


def get_song_data(song_name: str) -> SongInfo | None:
    if os.path.exists(SONGS_DATA_PATH):
        with open(SONGS_DATA_PATH, "r") as f:
            song_json_data = json.load(f)
           
            if song_json_data[song_name]:
                song_data = song_json_data[song_name]
                song_info: SongInfo = {
                    song_name: {
                        "song_file_path": song_data["song_file_path"],
                        "song_icon_path": song_data["song_icon_path"],
                    }
                }
                return song_info
            else:
                return None
