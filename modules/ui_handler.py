from classes import *


def update_ui(main_gui :MainGui):
    delta_time = main_gui.delta_time
    for button in main_gui.current_buttons:
        button.update(main_gui,delta_time)