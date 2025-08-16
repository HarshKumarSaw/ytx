import sys
from pathlib import Path
import subprocess


def print_banner():
    print("=" * 25)
    print("   YTX Downloader 🚀")
    print("   Powered by Zeno")
    print("=" * 25)


def get_url():
    return input("Enter YouTube video URL:\n> ").strip()


def get_quality_choice():
    print("Select quality:")
    print("1) 1080p")
    print("2) 720p")
    print("3) Audio only (MP3)")
    choice = input("> ").strip()
    while choice not in {"1", "2", "3"}:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("> ").strip()
    return choice


def construct_yt_dlp_cmd(url, quality, download_path):
    format_map = {
        "1": "bv*[height<=1080]+ba/bestvideo[height<=1080]+bestaudio",
        "2": "bv*[height<=720]+ba/bestvideo[height<=720]+bestaudio",
        "3": "bestaudio",
    }
    outtmpl = str(download_path / "%(title)s.%(ext)s")
    cmd = [
        "yt-dlp",
        "-o",
        outtmpl,
        "-f",
        format_map.get(quality, "bestaudio"),
        url,
    ]
    if quality == "3":
        cmd += ["--extract-audio", "--audio-format", "mp3"]
    return cmd


def check_ffmpeg():
    from shutil import which

    return which("ffmpeg") is not None


def get_downloads_folder():
    home = Path.home()
    if sys.platform == "win32":
        return home / "Downloads"
    elif sys.platform in ["linux", "darwin"]:
        return home / "Downloads"
    else:
        return home


def main():
    print_banner()
    url = get_url()
    quality = get_quality_choice()
    downloads = get_downloads_folder()

    if not check_ffmpeg():
        print("\n⚠️  ffmpeg not found! Install it for best performance:")
        print("Linux: sudo apt install ffmpeg")
        print("Windows/macOS: Download from https://ffmpeg.org/download.html\n")

    cmd = construct_yt_dlp_cmd(url, quality, downloads)
    print(f"\nDownloading to {downloads} ...\n")

    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Download complete!")
    except subprocess.CalledProcessError as e:
        print("\n❌ Error during download:")
        print(e)
        print("Please check the URL and try again.")


if __name__ == "__main__":
    main()
