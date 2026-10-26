from classes import *


def update_ui(main_gui :MainGui):
    for button in main_gui.current_buttons:
        button.update(main_gui)