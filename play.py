import os
import glob
import time
import sys
import subprocess

FRAME_DIR = 'ascii_frames'
files = glob.glob("*.mp3")

def play_audio():
    if len(files) != 0:
        subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", files[0]])

def load_frames():
    frames = []
    files = sorted(os.listdir(FRAME_DIR))
    for f in files:
        with open(os.path.join(FRAME_DIR, f), 'r', encoding='utf-8') as f:
            frames.append(f.read())
    return frames

def move_cursor_top():
    print("\033[H", end='')

def main():
    frames = load_frames()
    delay = 1/30
    play_audio()
    
    try:
        for frame in frames:
            move_cursor_top()
            print(frame)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[Stopped]")
        sys.exit()

if __name__ == "__main__":
    main()