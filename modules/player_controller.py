import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from classes import *
from get_asset_path import get_asset_path


def start_player(self: MainGui):
    if self.current_song:
       current_song :SongInfo = self.current_song
       song_details =  next(iter(current_song.values()))
       self.playing = True
       # Audio
       self.audio_player.start_audio(get_asset_path(song_details["song_file_path"]))
       # Visual
       self.control_button.selected_image_file = self.pause_image_file
   
    
    
    


def reset_player(self: MainGui):
    print("resetting player!")  # THIS WILL RESET THE SONG!
    self.audio_player.reset_audio()


def pause_player(self: MainGui):
    print("pausing player!")
    self.playing = False
    # Visual
    self.control_button.selected_image_file = self.play_image_file
    # Audio
    self.audio_player.pause_audio()


def control_player(self: MainGui):
    if self.playing:
        pause_player(self)
    else:
        start_player(self)
