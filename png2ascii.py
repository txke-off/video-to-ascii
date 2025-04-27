from PIL import Image
import os

ASCII_CHARS = '@%#*+=-:. '
WIDTH = 100
HEIGHT_SCALE = 0.5

def image_to_ascii(path):
    img = Image.open(path).convert('L')
    w, h = img.size
    new_h = int(h*HEIGHT_SCALE*WIDTH/w)
    img = img.resize((WIDTH, new_h))
    pixels = img.getdata()
    ascii_str = ''.join(ASCII_CHARS[(255-p)*len(ASCII_CHARS) // 256] for p in pixels)
    lines = [ascii_str[i:i+WIDTH] for i in range(0, len(ascii_str), WIDTH)]
    return '\n'.join(lines)

FRAME_DIR = 'frames'
ASCII_DIR = 'ascii_frames'
os.makedirs(ASCII_DIR, exist_ok = True)

frame_files = sorted(f for f in os.listdir(FRAME_DIR))
for i, file in enumerate(frame_files):
    ascii_art = image_to_ascii(os.path.join(FRAME_DIR, file))
    with open(os.path.join(ASCII_DIR, f'frame{i:04d}.txt'), 'w', encoding='utf-8') as f:
        f.write(ascii_art)