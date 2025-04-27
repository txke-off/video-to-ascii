import cv2
import glob
import os

FRAME_DIR = 'frames'
os.makedirs(FRAME_DIR, exist_ok=True)

files = glob.glob("*.mp4")
vidcap = cv2.VideoCapture(files[0])
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite(os.path.join(FRAME_DIR, f'frame{count:04d}.png'), image)
    success, image = vidcap.read()
    count += 1

vidcap.release()