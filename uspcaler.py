import os
import subprocess

# Supported video formats
VIDEO_EXTS = (".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv")

def upscale_to_4k(input_file, output_file):
    """Upscale a single video to 4K using FFmpeg"""
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vf", "scale=3840:2160:flags=lanczos",  # upscale with lanczos filter
        "-c:a", "copy",  # copy audio without re-encoding
        output_file
    ]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f" Converted: {input_file} → {output_file}")
    except subprocess.CalledProcessError:
        print(f" Failed to convert {input_file}")

def batch_upscale(folder_path):
    """Find and upscale all videos in a folder"""
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(VIDEO_EXTS):
            input_path = os.path.join(folder_path, file_name)
            base, ext = os.path.splitext(file_name)
            output_path = os.path.join(folder_path, f"{base}_4k{ext}")
            
            if os.path.exists(output_path):
                print(f"️ Skipping (already exists): {output_path}")
            else:
                upscale_to_4k(input_path, output_path)

if __name__ == "__main__":
    folder = input("Enter the folder path containing videos: ").strip()
    if os.path.isdir(folder):
        batch_upscale(folder)
    else:
        print(" Invalid folder path")
