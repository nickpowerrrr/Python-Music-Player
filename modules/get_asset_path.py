import os
from pathlib import Path


def get_asset_path(relative_path: str) -> str:
    r"""Get absolute path to file, works for dev and for PyInstaller,
    Example = 'images\\player\\default_icon.png'(two backslashes)

    """

    file_path = Path(os.path.dirname(os.path.abspath(__file__)))
    base_path: Path = (
        file_path.parent.absolute()
    )  # Uses parent so assets dont have to be in modules
    new_path: str = os.path.join(os.fspath(base_path), relative_path)
    if os.path.exists(new_path):
        return new_path
    else:
        raise FileNotFoundError(
            f"[get_asset_path] Couldnt get the asset for : '{relative_path}!' "
        )
