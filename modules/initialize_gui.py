import tkinter as tk
from get_asset_path import get_asset_path

# Images


class MainGui:
    def __init__(self):
        # Gui Initilization
        self.root = tk.Tk()
        self.root.title("Python-Music-Player v.0.0.1")
        self.root.geometry("750x500")  # Window size
        self.root.resizable(False, False)

        # Canvas
        self.canvas: tk.Canvas = tk.Canvas(
            self.root, width=750, height=500, highlightthickness=0
        )
        # Images
        self.play_image = tk.PhotoImage(
            file=get_asset_path("assets\\images\\play_button.png")
        )
        self.control_button: int = self.canvas.create_image(590, 300, self.play_image)
        # Gui Variablies
        self.playing = False
        # Start Loop
        self.root.mainloop()
        self.canvas.update()


def initialize_gui():
    return MainGui()
