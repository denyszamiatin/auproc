import glob
import base64
import json


from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'


def get_filenames(dir_=INIT_DIR):
    return glob.glob(dir_)


def get_tags(filenames):
    return [EasyID3(filename) for filename in filenames]


def save_audiofile(filename, obj):
    obj['audio'] = base64.b64encode(obj['audio'])
    with open('%s.json' % filename, 'wt') as f:
        json.dump(obj, f)

def audio_track_length(filename):
    return int(MP3(filename).info.length)

def volume_level(filename):
	sound = AudioSegment.from_file(filename, format="mp3")
    return sound.max


# TODO: get more clarity on objectives
# TODO: make decision what type get_tags should return
# TODO: add extraction minimal volume level of a track to the function volume_level
