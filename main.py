import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pygame
import os

class MusicPlaylistOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Playlist Organizer")

        pygame.mixer.init()

        self.playlist = []

        self.playlist_box = tk.Listbox(root, width=60, height=20)
        self.playlist_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.grid(row=1, column=0, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Song", command=self.remove_song)
        self.remove_button.grid(row=1, column=1, padx=10, pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.grid(row=1, column=2, padx=10, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.grid(row=1, column=3, padx=10, pady=5)

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def remove_song(self):
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            selected_song_index = selected_song_index[0]
            self.playlist_box.delete(selected_song_index)
            self.playlist.pop(selected_song_index)

    def play_song(self):
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            selected_song_index = selected_song_index[0]
            selected_song = self.playlist[selected_song_index]
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlaylistOrganizer(root)
    root.mainloop()
