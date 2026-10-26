import glob
import os
from pathlib import PurePath
from pathlib import Path


def find_file_type(relative_path: str, file_type: str):
    file_path = Path(os.path.dirname(os.path.abspath(__file__)))
    base_path: Path = file_path.parent.absolute()
    absolute_target = str(base_path / relative_path / "**" / f"*{file_type}")
    files = glob.glob(absolute_target, recursive=True)
    if len(files) > 1:
        raise ValueError("More then one music file!")
    elif len(files) == 1:
        absolute_path = Path(files[0])
        file_name = PurePath(absolute_path).name
        relative_path = str(Path(relative_path) / file_name)
        return absolute_path, relative_path
    else:
        return None, None
