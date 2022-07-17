import os
import shutil
import subprocess
import sys
from datetime import datetime
from glob import glob
from pathlib import Path


# DIRECTORIES #


def directory_path(filepath: str) -> str:
    # D:/Share/temp/2021-06-11.xlsx -> D:/Share/temp
    return os.path.dirname(filepath)


def directory_name(path):
    # D:\Share\temp\invoices -> invoices
    # but!: D:/Share/temp/2021-06-11.xlsx -> 2021-06-11.xlsx
    return os.path.basename(path)


def directory_name_above_file(filepath: str) -> str:
    # D:/Share/temp/2021-06-11.xlsx -> temp
    # but!: D:\Share\temp\invoices -> temp
    return os.path.basename(os.path.dirname(filepath))


def list_subfolders_with_paths(path):
    return [f.path for f in os.scandir(path) if f.is_dir()]


def delete_directory(filepath):
    # deletes a directory and all its contents.
    shutil.rmtree(filepath)


# FILES #


def get_file_paths(path_to_folder, pattern='**/*') -> list[Path]:
    p = Path(path_to_folder).glob(pattern)
    files = [x for x in p if x.is_file()]
    files.sort()
    return files


def list_of_files(folder: any, mask: str = '*') -> list[str]:
    # * means all, if it needs specific format then *.csv # example: mask='abb_acs*'
    return glob(str(Path(folder) / mask))


def most_recent_file_in_folder(folder: any, mask: str) -> str:
    files_list = list_of_files(folder, mask)
    return max(files_list, key=os.path.getmtime)


def move_file(filepath: str, dest_folder: str) -> None:
    """
    The directory in which the new file is being created must already exist.
    On Windows, a file with that name must not exist or an exception will be raised.
    source: https://stackoverflow.com/a/8858026
    """
    filename = file_name_with_ext(filepath)
    shutil.move(filepath, Path(dest_folder) / filename)


def copy_file(filepath: str, dest_folder: str, new_name: str) -> None:
    filename = new_name if new_name else file_name_with_ext(filepath)
    shutil.copy(filepath, Path(dest_folder) / filename)


def is_file_today(filepath) -> bool:
    today = datetime.now().date()
    try:
        filetime = datetime.fromtimestamp(os.path.getmtime(filepath))
        if filetime.date() == today:
            return True
        else:
            return False
    except FileNotFoundError:
        raise FileNotFoundError


def file_name_with_ext(filepath: str) -> str:
    return os.path.basename(filepath)


def file_name_without_ext(filepath: str) -> str:
    return os.path.splitext(os.path.basename(filepath))[0]


def file_extension(filepath: str) -> str:
    return os.path.splitext(filepath)[1]


def file_extension_without_dot(filepath: str) -> str:
    return os.path.splitext(filepath)[1][1:]


def start_file_if_not_mac(filename):
    if not is_mac():
        os.startfile(filename)


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def incrementing_filename(folder, filename):
    fn = file_name_without_ext(filename)
    ext = file_extension_without_dot(filename)
    i = 0
    while os.path.exists(Path(folder) / f'{fn}{i}.{ext}'):
        i += 1
    return Path(folder) / f'{fn}{i}.{ext}'
