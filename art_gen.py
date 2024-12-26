import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Parameters
frames_dir = "geoart_frames"
frame_count = 60
frame_width = 464  # Even width
frame_height = 462  # Even height

# Create frames directory if it doesn't exist
os.makedirs(frames_dir, exist_ok=True)

# Geometric Art Generation Function
def generate_geometric_art(frame_index):
    """Generate a single frame of geometric art."""
    plt.figure(figsize=(6, 6))
    plt.axis("off")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Example: Draw dynamic geometric shapes (editable part)
    t = np.linspace(0, 2 * np.pi, 100)
    radius = 0.8 * np.abs(np.sin(frame_index * np.pi / frame_count))  # Changing radius
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    plt.plot(x, y, color=np.random.rand(3), linewidth=2)
    
    # Save the frame
    frame_path = os.path.join(frames_dir, f"frame_{frame_index:03d}.png")
    plt.savefig(frame_path, dpi=100, bbox_inches="tight", pad_inches=0)
    plt.close()

    # Resize the saved frame to even dimensions
    image = Image.open(frame_path)
    image = image.resize((frame_width, frame_height), Image.ANTIALIAS)
    image.save(frame_path)

# Generate all frames
for i in range(frame_count):
    generate_geometric_art(i)

print(f"Frames saved in {frames_dir}")
