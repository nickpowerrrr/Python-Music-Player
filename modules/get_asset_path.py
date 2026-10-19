import os



def get_asset_path(relative_path: str) -> str:
    r"""Get absolute path to file, works for dev and for PyInstaller,
    Example = 'images\\player\\default_icon.png'(two backslashes)
    """
    base_path :str = os.path.dirname(os.path.abspath(__file__))
    new_path :str = os.path.join(base_path, relative_path)
    if os.path.exists(new_path):
        return new_path
    else:
        raise FileNotFoundError(f"[get_asset_path] Couldnt get the asset for : '{relative_path}!' ")
