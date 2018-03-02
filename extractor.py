from glob import glob

from mutagen.easyid3 import EasyID3
import json

INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'


def get_filenames(dir_=INIT_DIR):
    return glob(dir_)


def get_tags(filenames):
    return [EasyID3(filename) for filename in filenames]


def save_audio(filename, audio):
    with open('%s_audio.json' % filename, 'wb') as f:
        json.dump(audio, f)


def save_tags(filename, tags):
    with open('%s_tags.json' % filename, 'wt') as f:
        json.dump(tags, f)

# TODO: get more clarity on objectives
# TODO: make decision what type get_tags should return
