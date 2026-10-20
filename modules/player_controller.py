import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from classes import MainGui


def start_player(self: MainGui):
    print("starting player!")
    self.playing = True
    #self.canvas.itemconfig(self.control_button.button, image=self.pause_image)
    self.control_button.selected_image_file = self.pause_image_file
    print(self.delta_time)


def reset_player(self: MainGui):
    print("resetting player!")  # THIS WILL RESET THE SONG!


def pause_player(self: MainGui):
    print("pausing player!")
    self.playing = False
    #self.canvas.itemconfig(self.control_button.button, image=self.play_image)
    self.control_button.selected_image_file = self.play_image_file


def control_player(self: MainGui):
    if self.playing:
        pause_player(self)
    else:
        start_player(self)
