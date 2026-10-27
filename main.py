import time

from modules.classes import MainGui
from modules.initialize_gui import initialize_gui
from modules.ui_handler import update_ui

MAIN_GUI :MainGui = initialize_gui()

# Variables

last_frame_time = time.perf_counter()


def update():
    global last_frame_time

    current_time = time.perf_counter()
    delta_time = current_time - last_frame_time
    last_frame_time = current_time

    MAIN_GUI.delta_time = delta_time
    update_ui(MAIN_GUI)
    MAIN_GUI.root.after(16, update)  # 60 fps

update()
MAIN_GUI.root.mainloop()