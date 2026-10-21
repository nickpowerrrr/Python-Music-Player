import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from classes import *
from player_controller import *


def initialize_gui():
    self = MainGui()
    # Interactions
    # --Control button
    self.canvas.tag_bind(self.control_button.button, "<Button-1>", lambda event: control_player(self))
    self.canvas.bind("<Motion>", lambda event: self.track_motion(event))
    
    return self
