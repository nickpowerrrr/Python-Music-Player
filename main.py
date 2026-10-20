from time import time

from modules.classes import *
from modules.initialize_gui import initialize_gui

MAIN_GUI = initialize_gui()

# Variables
last_frame_time: float = 0


def update():
    while True:
        global last_frame_time
        frame_time = time()
        delta_time = frame_time - last_frame_time
        last_frame_time = frame_time
        MAIN_GUI.delta_time = round(delta_time,6)
        MAIN_GUI.root.update()
        MAIN_GUI.root.update_idletasks()


update()
