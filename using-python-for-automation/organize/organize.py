# use the os module to make new folders
import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# maps the extension to the category
def pickCategory(file_type):
    for category, extensions in SUBDIRECTORIES.items():
        for suffix in extensions:
            if suffix == file_type:
                return category
    # if can't find category, return MISC
    return 'MISC'

# organize the directory and make the folders
def organizeDirectory():
    # get all items in current dir
    for item in os.scandir():
        # precautions
        if item.is_dir():
            continue
        filePath = Path(item)
        # isolate suffix
        filetype = filePath.suffix.lower()
        directory_assignment = pickCategory(filetype)
        # if MISC, don't touch/move it
        if directory_assignment == 'MISC':
            continue
        # cast the assignment to the path
        dir_path = Path(directory_assignment)
        # if the folder doesn't exist, then make it
        if not dir_path.is_dir():
            dir_path.mkdir()
        # move the file into the directory
        filePath.rename(dir_path.joinpath(filePath))

if __name__ == '__main__':
    organizeDirectory()