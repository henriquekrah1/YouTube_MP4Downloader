import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
from pathlib import Path
import os
import time

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x480")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.last_log_time = 0  # For throttling log updates

        self.set_style()
        self.setup_gui()

    def set_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", foreground="white", background="#3c3c3c", padding=6, relief="flat")
        style.map("TButton", background=[("active", "#5a5a5a")])
        style.configure("Vertical.TScrollbar", background="#333")

    def setup_gui(self):
        tk.Label(self.root, text="📺 YouTube MP4 Downloader", font=("Helvetica", 16),
                 bg="#1e1e1e", fg="#ffffff").pack(pady=10)

        tk.Label(self.root, text="Enter YouTube Video Link:", bg="#1e1e1e", fg="#cccccc").pack()
        self.link_entry = tk.Entry(self.root, width=70)
        self.link_entry.pack(pady=5)

        self.download_btn = ttk.Button(self.root, text="Download Video", command=self.download_video)
        self.download_btn.pack(pady=10)

        self.status_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=18, width=70,
                                                    font=("Consolas", 9), bg="#2d2d2d", fg="#ffffff",
                                                    insertbackground="white", borderwidth=0)
        self.status_box.pack(pady=10)

    def log(self, text):
        self.status_box.insert(tk.END, text + "\n")
        self.status_box.see(tk.END)
        self.root.update_idletasks()

    def download_video(self):
        link = self.link_entry.get().strip()
        if not link:
            messagebox.showwarning("Missing Link", "Please enter a valid YouTube link.")
            return

        script_dir = Path(os.path.abspath(os.path.dirname(__file__)))
        downloads_dir = script_dir / "Downloads"
        downloads_dir.mkdir(parents=True, exist_ok=True)

        output_template = str(downloads_dir / "%(title)s.%(ext)s")
        cookie_path = script_dir / "cookies.txt"

        def progress_hook(d):
            if d['status'] == 'downloading':
                current_time = time.time()
                if current_time - self.last_log_time >= 4:
                    total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
                    downloaded_bytes = d.get('downloaded_bytes', 0)
                    if total_bytes:
                        percent = int(downloaded_bytes / total_bytes * 100)
                        self.log(f"⏳ Download progress: {percent}%")
                        self.last_log_time = current_time

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': output_template,
            'merge_output_format': 'mp4',
            'cookiefile': str(cookie_path),
            'quiet': True,
            'no_warnings': True,
            'progress_hooks': [progress_hook],
        }

        try:
            self.log(f"🔽 Downloading from: {link}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            self.log(f"✅ Download completed! Saved to: {downloads_dir}")
            messagebox.showinfo("Download Complete", f"✅ Download complete!\nSaved to: {downloads_dir}")
        except Exception as e:
            self.log(f"❌ Download failed: {e}")
            messagebox.showerror("Error", f"❌ Download failed:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
