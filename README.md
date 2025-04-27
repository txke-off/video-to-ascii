# video-to-ascii
An mp4 to black-and-white ascii-animation converter (audio included)

## Dependencies

Install requirements:

```bash
pip install -r requirements.txt
```

Install [FFmpeg](https://ffmpeg.org/)

## How to use

1. Place the single .mp4 file in the project folder.
2. Run the scripts in the next order:
   ```bash
   python vid2png.py
   python png2ascii.py
   python vid2audio.py #optional if audio isnt needed
   python play.py

Any video is supported, but works best with black-and-white or high-contrast clips.

## Demo

[![demo_ig](https://img.youtube.com/vi/VibqVyuH_0A/0.jpg)](https://www.youtube.com/watch?v=VibqVyuH_0A)
