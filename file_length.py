from mutagen.mp3 import MP3


def file_time(filename):
    return int(MP3(filename).info.length)
