import subprocess
import glob

files = glob.glob("*.mp4")

def extract_audio_from_video(video_file, output_audio_file):
    command = [
        "ffmpeg",
        "-i", video_file,
        "-q:a", "0",
        "-map", "a",
        output_audio_file
    ]
    subprocess.run(command, check=True)

extract_audio_from_video(files[0], "audio_extracted.mp3")