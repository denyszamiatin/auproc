import glob
import base64
import json

import numpy as np
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from pydub import AudioSegment

INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'


def get_filenames(dir_=INIT_DIR):
    return glob.glob(dir_)


musical_instruments = {'violin': 'musical_instruments_audio/violin.mp3',
                       'hautboy': 'musical_instruments_audio/goboj.mp3',
                       'elektrogitara': 'musical_instruments_audio/elektrogitara.mp3'}


def match_target_amplitude(sound):
    return sound.apply_gain(sound.max_dBFS)


class AudioData:

    BLOCK_SIZE = 1024

    def __init__(self, filename):
        sound = AudioSegment.from_mp3(filename)
        self.tags = EasyID3(filename)
        self.track_length = int(MP3(filename).info.length)
        self.audio_data = np.frombuffer(sound.raw_data, np.uint8)
        self.min_volume = min(self.audio_data)
        self.max_volume = max(self.audio_data)
        self.fft = [np.fft.fft(block) for block in np.array_split(
            self.audio_data,
            len(self.audio_data) // self.BLOCK_SIZE
        )]

    def save_audiofile(self, filename):
        obj = dict(self.tags)
        obj['audio'] = base64.b64encode(self.audio_data)
        with open('%s.json' % filename, 'wt') as f:
            json.dump(obj, f)
