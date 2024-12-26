import os
import subprocess
from datetime import datetime

# Parameters
frames_dir = "geoart_frames"
output_dir = "output"
frame_count = 60
fps = 24

# Create output directory for the video
os.makedirs(output_dir, exist_ok=True)

# Get today's date for video file naming
today_date = datetime.now().strftime("%Y-%m-%d")
output_video = os.path.join(output_dir, f"geoart_{today_date}.mp4")

# Combine frames into a video using FFmpeg
ffmpeg_command = [
    "ffmpeg",
    "-y",  # Overwrite output file
    "-framerate", str(fps),
    "-i", os.path.join(frames_dir, "frame_%03d.png"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output_video
]

subprocess.run(ffmpeg_command)

print(f"Video saved as {output_video}")
