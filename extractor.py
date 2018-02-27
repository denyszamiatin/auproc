from glob import glob

from mutagen.easyid3 import EasyID3

INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'


def get_filenames(dir_=INIT_DIR):
    return glob(dir_)


def get_tags(filenames):
    return [EasyID3(filename) for filename in filenames]

# TODO: get more clarity on objectives
# TODO: make decision what type get_tags should return
