# 🎬 YouTube Video Downloader (MP4) — GUI App

A sleek, portable GUI application that downloads YouTube videos in the **highest available resolution** (video + audio combined) and saves them as `.mp4` files locally. Designed to be user-friendly, fast, and simple — just paste the link and hit download.

> Built with `Python`, `yt-dlp`, and `tkinter`.

---

## 💡 Features

- ✅ Download **YouTube videos** with **audio** in maximum quality
- ✅ Graphical user interface (no terminal needed)
- ✅ Live status updates (including download progress)
- ✅ Works offline after setup (just keep your `cookies.txt` with you)
- ✅ Automatically saves to a local `Downloads/` folder
- ✅ Fully portable across devices — no need to reconfigure paths

---

## 📁 How to Use

1. **Install Python 3.10+** (https://www.python.org/)
2. Install `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```
3. Download or clone this repository
4. Make sure `cookies.txt` is in the same folder as the script (optional but recommended for age-restricted/private videos)
5. Run the app:
   ```bash
   python ytb_Downloader_gui_app.pyw
   ```
6. Paste a valid YouTube video link and hit **Download Video**
7. Find your `.mp4` file in the automatically created `Downloads/` folder

---

## 🍪 Cookie Support

To download age-restricted/private videos:

- Export your YouTube browser cookies (via [this guide](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp))
- Save the file as `cookies.txt`
- Place it in the **same directory** as the script

---

## 📝 Requirements

- Python 3.10+
- Packages:
  ```bash
  pip install yt-dlp
  ```
- No extra dependencies — `tkinter` comes with Python on most systems

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**.

It uses `yt-dlp` to access publicly available content. Please ensure you have the legal right to download and use any video content. This tool does **not circumvent DRM** and **does not support downloading from paid services** like YouTube Premium.

The developer assumes **no liability** for misuse of this software.

---

## 📜 License

This project is open-sourced under the **MIT License**.

Special thanks to [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the backend engine.

---
