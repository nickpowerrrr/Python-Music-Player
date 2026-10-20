import os
from PIL import Image, ImageTk 
import sys
import tkinter as tk

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# ADD LOCAL IMPORTS AFTER THIS
from get_asset_path import get_asset_path

#CONSTANTS
GUI_WIDTH = 750
GUI_HEIGHT = 500

CONTROL_BUTTON_SIZE = (100,100)


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
        # Images
        
        # --Control button
        self.play_image = Image.open(get_asset_path("assets\\images\\play_button.png"))
        self.play_image = self.play_image.resize(CONTROL_BUTTON_SIZE)
        self.play_image = ImageTk.PhotoImage(self.play_image,master=self.root)
        self.pause_image = Image.open(get_asset_path("assets\\images\\pauze_button.png"))
        self.pause_image = self.pause_image.resize(CONTROL_BUTTON_SIZE)
        self.pause_image = ImageTk.PhotoImage(self.pause_image,master=self.root)
        self.control_button :int = self.canvas.create_image(GUI_WIDTH /2, GUI_HEIGHT/2, image=self.play_image) #type :ignore
        # Variables
        self.playing = False