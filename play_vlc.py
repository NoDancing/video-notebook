
# This was my second attempt to make the video functionality work
# The movie plays properly, but it can't run simultaneously with the command line.
# I will continue working on it.

import vlc
import sys
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from os.path import join as joined
from ctypes import c_void_p, cdll

try:
    libtk = 'libtk%s.dylib' % (tk.TkVersion,)
    prefix = getattr(sys, 'base_prefix', sys.prefix)
    libtk = joined(prefix, 'lib', libtk)
    dylib = cdll.LoadLibrary(libtk)
    _getNSView = dylib.TkMacOSXGetRootControl
    _getNSView.restype = c_void_p
    _getNSView.argtypes = [c_void_p]
    del dylib

except (NameError, OSError):
    def _getNSView(unused):
        return None
    libtk = "N/A"



class VideoPlayer:
    def __init__(self, master, video_path):
        self.master = master
        self.video_path = video_path

        self.master.title("VLC Video Player")

        self.video_frame = ttk.Frame(self.master)
        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        self.vlc_instance = vlc.Instance()

        self.player = self.vlc_instance.media_player_new()
        self.media = self.vlc_instance.media_new(self.video_path)
        self.player.set_media(self.media)
        
        h = self.video_frame.winfo_id()
        v = _getNSView(h)
        self.player.set_nsobject(v)

        self.master.update_idletasks()
        self.player.set_xwindow(self.video_frame.winfo_id())

    def adjust_window_size(self):
        video_width = self.player.video_get_width()
        video_height = self.player.video_get_height()

        self.master.geometry(f"{video_width}x{video_height}")

    def play(self):
        self.player.play()
        self.master.after(1000, self.adjust_window_size)


def main():
    video_path = "testvideo.mkv"
    root = tk.Tk()
    player = VideoPlayer(root, video_path)
    player.play()
    root.mainloop()

if __name__ == "__main__":
    main()
