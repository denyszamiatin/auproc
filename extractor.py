import glob
import base64
import json

import numpy as np
import soundfile as sf
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from pydub import AudioSegment


INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'


def get_filenames(dir_=INIT_DIR):
    return glob.glob(dir_)


def get_tags(filenames):
    return [EasyID3(filename) for filename in filenames]


def save_audiofile(filename, obj):
    obj['audio'] = base64.b64encode(obj['audio'])
    with open('%s.json' % filename, 'wt') as f:
        json.dump(obj, f)


def get_track_length(filename):
    return int(MP3(filename).info.length)


def get_audiodata_from_mp3(filename):
    sound = AudioSegment.from_mp3(filename)
    return np.frombuffer(sound.raw_data, np.uint8)


def get_volume(stream):
    return min(stream), max(stream)


def get_fft(filename):
    return [np.fft.fft(block) for block in sf.blocks(filename, blocksize=1024)]
