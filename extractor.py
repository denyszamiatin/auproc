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


def convert_from_mp3(filename):
    sound = AudioSegment.from_mp3(filename)
    name_song = filename.split(".")[0]
    sound.export('{0}.wav'.format(name_song), format="wav")
    return '{0}.wav'.format(name_song)


def get_volume_song(filename):
    rms = [np.sqrt(np.mean(block ** 2)) for block in
           sf.blocks(filename, blocksize=1024, overlap=512)]

    min_volume, max_volume = (min(rms), max(rms))
    return min_volume, max_volume
