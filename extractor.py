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
        self.sound = AudioSegment.from_mp3(filename)
        self.audio_stream = self._get_audio_stream()
        self.tags = EasyID3(filename)
        self.track_length = int(MP3(filename).info.length)
        self.min_volume = min(self.audio_stream)
        self.max_volume = max(self.audio_stream)

    def save_audiofile(self, filename):
        obj = dict(self.tags)
        obj['audio'] = base64.b64encode(self._get_audio_stream())
        with open('%s.json' % filename, 'wt') as f:
            json.dump(obj, f)

    def _get_audio_stream(self):
        return np.frombuffer(self.sound.raw_data, np.uint8)

    def _get_fft(self):
        return [np.fft.fft(block) for block in np.array_split(
            self.audio_stream,
            len(self.audio_stream) // self.BLOCK_SIZE)]


m = AudioData(musical_instruments['violin'])
n = m.audio_stream
print(n)
