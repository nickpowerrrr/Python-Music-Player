import os
import sys
import tkinter as tk
import numpy as np

from PIL import Image, ImageTk
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lerp import lerp

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# ADD LOCAL IMPORTS AFTER THIS
from get_asset_path import get_asset_path

# CONSTANTS
GUI_WIDTH = 750
GUI_HEIGHT = 500

CONTROL_BUTTON_SIZE = (100, 100)


class MainGui:
    def __init__(self):
        # Gui Initilization
        self.root = tk.Tk()
        self.root.title("Python-Music-Player v.0.0.1")
        self.root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")  # Window size
        self.root.resizable(False, False)

        # Canvas
        self.canvas: tk.Canvas = tk.Canvas(
            self.root, width=750, height=500, highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.update()
        # Variables
        self.delta_time = 0.00
        self.playing = False
        self.mouse_position_x = 0
        self.mouse_position_y = 0
        # Images

        # --Control button
        self.play_image_file = Image.open(
            get_asset_path("assets\\images\\play_button.png")
        )
        self.play_image = self.play_image_file.resize(CONTROL_BUTTON_SIZE)
        self.play_image = ImageTk.PhotoImage(self.play_image, master=self.root)
        self.pause_image_file = Image.open(
            get_asset_path("assets\\images\\pauze_button.png")
        )
        self.pause_image = self.pause_image_file.resize(CONTROL_BUTTON_SIZE)
        self.pause_image = ImageTk.PhotoImage(self.pause_image, master=self.root)
        self.control_button = ImageButton(self, self.play_image,self.play_image_file)

    def track_motion(self, event):
        x, y = event.x, event.y
        self.mouse_position_x: int = x
        self.mouse_position_y: int = y


class ImageButton:
    """Creates an image button with hover functions"""

    def __init__(self, main_gui: MainGui, selected_image: ImageTk.PhotoImage, selected_image_file):
        self.position_x = GUI_WIDTH / 2
        self.position_y = GUI_HEIGHT / 2
        self.min_position_x = self.position_x - 50  # 50% of size.
        self.max_position_x = self.position_x + 50
        self.min_position_y = self.position_y - 50
        self.max_position_y = self.position_y + 50
        self.button: int = main_gui.canvas.create_image(
            self.position_x, self.position_y, image=selected_image
        )
        self.selected_image_file = selected_image_file
        self.current_size = 100
        
        self.update(main_gui)

    def update(self, main_gui: MainGui):

        is_in_x_range = (main_gui.mouse_position_x > self.min_position_x) and (
            main_gui.mouse_position_x < self.max_position_x
        )
        is_in_y_range = (main_gui.mouse_position_y > self.min_position_y) and (
            main_gui.mouse_position_y < self.max_position_y
        )
        is_in_range = is_in_x_range and is_in_y_range
        if is_in_range:
            self.on_enter(main_gui)
        else:
            self.on_leave(main_gui)
        main_gui.root.after(16, lambda: self.update(main_gui))

    def on_enter(self, main_gui :MainGui):
        target_size = 200
        speed = main_gui.delta_time * 100
        current_size = lerp(self.current_size,target_size,speed)
        # self.selected_image_file = self.selected_image_file.resize(current_size,current_size)
        # main_gui.canvas.itemconfig(main_gui.control_button.button, image=self.selected_image_file)
        self.current_size = current_size
        print(self.current_size)

    def on_leave(self, main_gui :MainGui):
        target_size = 100
        speed = main_gui.delta_time * 100
        current_size = lerp(self.current_size,target_size,speed)
        # self.selected_image_file = self.selected_image_file.resize(current_size,current_size)
        main_gui.canvas.itemconfig(main_gui.control_button.button, image=self.selected_image_file)
        self.current_size = current_size
        print(self.current_size)
