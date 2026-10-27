import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from classes import MainGui
from song_data_handler import create_song_data, get_song_data
from player_controller import control_player, reset_player


def initialize_gui():
    self = MainGui()
    # Interactions
    # --Control button
    self.canvas.tag_bind(
        self.control_button.button, "<Button-1>", lambda event: control_player(self)
    )
    # Skip Buttons
    self.canvas.tag_bind(
        self.skip_left_button.button, "<Button-1>", lambda event: reset_player(self)
    )
    self.canvas.tag_bind(
        self.skip_right_button.button, "<Button-1>", lambda event: reset_player(self)
    )

    # ---
    self.canvas.bind("<Motion>", lambda event: self.track_motion(event))
    create_song_data("I miss the quiet")
    current_song = get_song_data("I miss the quiet")
    self.current_song = current_song

    return self
