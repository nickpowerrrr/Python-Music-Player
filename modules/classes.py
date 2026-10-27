import os
import sys
import tkinter as tk
from typing import TypedDict

import numpy as np
from PIL import Image, ImageFile, ImageTk

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lerp import lerp

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# ADD LOCAL IMPORTS AFTER THIS
from audioplayer import AudioPlayer
from get_asset_path import get_asset_path

# CONSTANTS
GUI_WIDTH = 750
GUI_HEIGHT = 500

CONTROL_BUTTON_SIZE = (100, 100)
COVER_ART_SIZE = (250, 250)
SKIP_BUTTON_OFFSET = 150


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
        self.CONTROL_BUTTON_SIZE = CONTROL_BUTTON_SIZE
        self.COVER_ART_SIZE = COVER_ART_SIZE
        # Images

        # Ui Handler Variables
        self.current_buttons: list[ImageButton] = []

        # --Control button

        self.play_image_file = Image.open(
            get_asset_path("assets/images/play_button.png")
        )
        self.play_image = self.play_image_file.resize(CONTROL_BUTTON_SIZE)
        self.play_image = ImageTk.PhotoImage(self.play_image, master=self.root)

        self.pause_image_file = Image.open(
            get_asset_path("assets/images/pauze_button.png")
        )
        self.pause_image = self.pause_image_file.resize(CONTROL_BUTTON_SIZE)
        self.pause_image = ImageTk.PhotoImage(self.pause_image, master=self.root)
        self.control_button = ImageButton(
            self,
            self.play_image,
            self.play_image_file,
            GUI_WIDTH / 2,
            GUI_HEIGHT / 2 + 100,
        )
        self.current_buttons.append(self.control_button)
        self.skip_left_image_file = Image.open(
            get_asset_path("assets/images/skip_left.png")
        )
        self.skip_left_image = self.skip_left_image_file.resize(CONTROL_BUTTON_SIZE)
        self.skip_left_image = ImageTk.PhotoImage(
            self.skip_left_image, master=self.root
        )
        self.skip_left_button = ImageButton(
            self,
            self.skip_left_image,
            self.skip_left_image_file,
            self.control_button.position_x - SKIP_BUTTON_OFFSET,
            GUI_HEIGHT / 2 + 100,
        )
        self.current_buttons.append(self.skip_left_button)
        self.skip_right_image_file = Image.open(
            get_asset_path("assets/images/skip_right.png")
        )
        self.skip_right_image = self.skip_right_image_file.resize(CONTROL_BUTTON_SIZE)
        self.skip_right_image = ImageTk.PhotoImage(
            self.skip_right_image, master=self.root
        )
        self.skip_right_button = ImageButton(
            self,
            self.skip_right_image,
            self.skip_right_image_file,
            self.control_button.position_x + SKIP_BUTTON_OFFSET,
            GUI_HEIGHT / 2 + 100,
        )
        self.current_buttons.append(self.skip_right_button)

        # Cover Art Image
        self.cover_art_image_file = Image.open(  # Will probably be replaced later with last song that played before exit, probably..
            get_asset_path("assets/images/default_icon.png")
        )
        self.cover_art_image_file = self.cover_art_image_file.resize(COVER_ART_SIZE)
        self.cover_art_image_file = ImageTk.PhotoImage(
            self.cover_art_image_file, master=self.root
        )
        self.cover_art_image = self.canvas.create_image(
            GUI_WIDTH / 2, 150, image=self.cover_art_image_file
        )

        # Audio Player
        self.audio_player = AudioPlayer()
        # Data
        self.current_song: SongInfo | None = None

    def track_motion(self, event: tk.Event):
        x, y = event.x, event.y
        self.mouse_position_x: int = x
        self.mouse_position_y: int = y


class ImageButton:
    """Creates an image button with hover functions"""

    def __init__(
        self,
        main_gui: MainGui,
        selected_image: ImageTk.PhotoImage,
        selected_image_file: ImageFile.ImageFile,
        position_x: float,
        position_y: float,
    ):
        self.position_x = position_x
        self.position_y = position_y
        self.min_position_x = self.position_x - 50  # 50% of size.
        self.max_position_x = self.position_x + 50
        self.min_position_y = self.position_y - 50
        self.max_position_y = self.position_y + 50
        self.button: int = main_gui.canvas.create_image(  # type: ignore
            self.position_x, self.position_y, image=selected_image
        )
        self.selected_image_file = selected_image_file
        self.current_size = 100

    def update(self, main_gui: MainGui, delta_time: float):

        is_in_x_range = (main_gui.mouse_position_x > self.min_position_x) and (
            main_gui.mouse_position_x < self.max_position_x
        )
        is_in_y_range = (main_gui.mouse_position_y > self.min_position_y) and (
            main_gui.mouse_position_y < self.max_position_y
        )
        is_in_range = is_in_x_range and is_in_y_range
        if is_in_range:
            self.on_enter(main_gui, delta_time)
        elif self.current_size != 100:
            self.on_leave(main_gui, delta_time)

    def scale_button(self, main_gui: MainGui, target_size: int, delta_time: float):

        speed = 10.0
        alpha = np.clip(delta_time * speed, 0.0, 1.0) or min(delta_time * speed, 1.0)

        self.current_size = lerp(self.current_size, target_size, alpha)

        int_size = round(self.current_size)

        resized_file = self.selected_image_file.resize(
            (int_size, int_size),
        )

        self.selected_image = ImageTk.PhotoImage(resized_file, master=main_gui.root)
        main_gui.canvas.itemconfig(self.button, image=self.selected_image)

    def on_enter(self, main_gui: MainGui, delta_time: float):
        self.scale_button(main_gui, 125, delta_time)

    def on_leave(self, main_gui: MainGui, delta_time: float):
        self.scale_button(main_gui, 100, delta_time)


class SongDetails(TypedDict):
    song_file_path: str
    song_icon_path: str


SongInfo = dict[str, SongDetails]
