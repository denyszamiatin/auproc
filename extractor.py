

def extract_dir(dir = '/Users/sergii/Downloads/mp3/*.mp3'):
    from glob import glob
    from mutagen.easyid3 import EasyID3

    d = {EasyID3(track) for track in glob(dir)}
    return d


# TODO: get more clarity on objectives