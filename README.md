# YTX Downloader 🚀

A simple, interactive, cross-platform YouTube downloader CLI powered by yt-dlp and Python.

---

## Features

- Download videos in 1080p or 720p quality.
- Extract audio as MP3.
- Interactive prompts — no need to remember complicated commands.
- Saves files to your system's Downloads folder.
- Cross-platform support: Android (Termux), Linux, macOS, Windows.

---

## Installation

Make sure you have Python 3.6+ installed.

Install via pip:

```
pip install ytx
```

---

## Usage

Run the downloader from your terminal:

```
ytx
```

Follow prompts to enter the YouTube URL and select quality.

---

## Dependencies

- Python 3
- yt-dlp (installed automatically with ytx)
- ffmpeg (required for audio extraction and best performance)

### Installing ffmpeg

- **Linux:**  
```
sudo apt install ffmpeg
```

- **Windows/macOS:**  
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

---

## Troubleshooting

- If the download fails, verify your internet connection.
- Check that the YouTube URL is correct.
- Ensure ffmpeg is installed for audio downloads.