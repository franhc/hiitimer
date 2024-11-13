import os
import time

from pydub import AudioSegment
from pydub.playback import play

SOUND_DIR = "assets"


if __name__ == '__main__':
    sfiles = [os.path.join(SOUND_DIR, f) 
                for f in os.listdir(SOUND_DIR) 
                if os.path.isfile(os.path.join(SOUND_DIR, f)) 
                and f[-3:] == "mp3"]

    for f in sfiles:
        print(f'Playing file: {f}')
        sound = AudioSegment.from_mp3(f)
        play(sound)
        time.sleep(1)