import settings
import sys, os, re
from math import ceil
from pathlib import Path
from multiprocessing.pool import Pool
from shutil import move, copytree

SONG_PATH = Path(os.path.expandvars(settings.PATH_TO_SONG_FOLDER))
EXPUNGED_PATH = Path(os.path.expandvars(settings.PATH_TO_EXPUNGED_FOLDER))

# Filters beatmap sets
def scanFile(path):
    for line in path.open(encoding="utf-8"):
        if line.lower().startswith("tags:"):
            line = line.replace('\n', '').replace(':', '')
            tags = line[len("tags:")-1:len(line)].split(" ")
            for tag in tags: #Ignore tags take priority over everything else
                if tag.lower() in settings.TAGS_IGNORE:
                    return False
            for tag in tags:
                if tag.lower() in settings.ANY_TAGS_BLACKLIST:
                    return True
            for tagList in settings.ALL_TAGS_BLACKLIST:
                if all(tag in tags for tag in tagList):
                    return True
            return False

# Recursively scans a directory tree for osu files
def scanDirectory(path):
    path = Path(path)
    if not path.exists() or not path.is_dir():
        return
    for entry in path.iterdir():
        if entry.is_dir():
            scanDirectory(entry)
        elif entry.is_file() and entry.suffix.lower() in settings.SUFFIX_WHITELIST:
            if scanFile(entry):
                if settings.OPERATION == "move":
                    try:
                        move(path, EXPUNGED_PATH / path.stem)
                        print('\"' + path.stem + "\" was moved.")
                    except AttributeError:
                        print('\"' + path.stem + "\" could not be moved.\nIs a copy of the beatmap already in the expunged songs folder?")
                    except:
                        print('\"' + path.stem + "\" could not be moved.")
                elif settings.OPERATION == "copy":
                    try:
                        copytree(path, EXPUNGED_PATH / path.stem, dirs_exist_ok=True)
                        print('\"' + path.stem + "\" was copied.")
                    except:
                        print('\"' + path.stem + "\" could not be copied.")
                else:
                    print("Nothing was done to \"" + path.stem + "\".")
                return


if __name__ == "__main__":
    SONG_PATH = Path(os.path.expandvars(settings.PATH_TO_SONG_FOLDER))
    EXPUNGED_PATH = Path(os.path.expandvars(settings.PATH_TO_EXPUNGED_FOLDER))
    if not SONG_PATH.exists():
        sys.exit("Song folder does not exist")
    print("Scanning " + str(SONG_PATH) + "...")
    if settings.MULTIPROCESSING:
        with Pool() as p:
            p.map(scanDirectory, SONG_PATH.iterdir())
    else:
        scanDirectory(SONG_PATH)
    