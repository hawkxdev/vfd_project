import os
import shutil
from pathlib import Path
from zipfile import ZipFile

from config.config import get_share_folder
from libs.utils.files import file_name_without_ext, move_file, directory_path, delete_directory


def correct_xlsx_from_1c(filepath):
    # https://ru.stackoverflow.com/a/1329702

    file_name_no_ext = file_name_without_ext(filepath)
    dir_name = directory_path(filepath)

    # Создаем временную папку
    tmp_folder = get_share_folder() / 'tmp' / 'convert_wrong_excel'
    os.makedirs(tmp_folder, exist_ok=True)

    # Распаковываем excel как zip в нашу временную папку
    with ZipFile(filepath) as excel_container:
        excel_container.extractall(tmp_folder)

    # Переименовываем файл с неверным названием
    wrong_file_path = os.path.join(tmp_folder, 'xl', 'SharedStrings.xml')
    correct_file_path = os.path.join(tmp_folder, 'xl', 'sharedStrings.xml')
    os.rename(wrong_file_path, correct_file_path)

    # Запаковываем excel обратно в zip
    archive_path = shutil.make_archive(file_name_no_ext, 'zip', tmp_folder)

    # Удаляю временную папку 'convert_wrong_excel и удаляю исходный файл (на его место запишется пересобранный)'
    delete_directory(tmp_folder)
    os.remove(filepath)

    # Переношу собранный архив в исходную папку
    move_file(archive_path, dir_name)

    # Переименовывая zip в исходный файл xlsx
    path_no_ext = str(Path(dir_name) / file_name_no_ext)
    os.rename(f'{path_no_ext}.zip', f'{path_no_ext}.xlsx')
