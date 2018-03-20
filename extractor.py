import glob
import base64
import json

import numpy as np
import soundfile as sf
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from pydub import AudioSegment


class AudioData:

    INIT_DIR = '/Users/sergii/Downloads/mp3/*.mp3'

    def get_filenames(self, dir_=INIT_DIR):
        return glob.glob(dir_)

    def get_tags(self, filenames):
        return [EasyID3(filename) for filename in filenames]

    def save_audiofile(self, filename, obj):
        obj['audio'] = base64.b64encode(obj['audio'])
        with open('%s.json' % filename, 'wt') as f:
            json.dump(obj, f)

    def get_track_length(self, filename):
        return int(MP3(filename).info.length)

    def get_audiodata_from_mp3(self, filename):
        sound = AudioSegment.from_mp3(filename)
        return np.frombuffer(sound.raw_data, np.uint8)

    def get_volume(self, stream):
        return min(stream), max(stream)

    def get_fft(self, filename):
        sound = AudioSegment.from_mp3(filename)
        name_song = filename.split(".")[0]
        sound.export('{0}.wav'.format(name_song), format="wav")
        return [np.fft.fft(block) for block in sf.blocks('{0}.wav'.format(name_song), blocksize=1024)]
