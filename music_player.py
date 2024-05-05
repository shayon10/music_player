import os
import pygame
from tkinter import filedialog, Tk, Button, Label, Listbox, Scrollbar


class MusicPlayer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("500x300")

        self.playlist = Listbox(self.root, width=50)
        self.playlist.pack(pady=20)

        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.playlist.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.playlist.config(yscrollcommand=self.scrollbar.set)

        self.play_button = Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.pause_button = Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)

        self.stop_button = Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)

        self.add_button = Button(self.root, text="Add Songs", command=self.add_songs)
        self.add_button.pack(pady=10)

        self.current_song = None

        pygame.init()

    def add_songs(self):
        songs = filedialog.askopenfilenames(initialdir="/", title="Select Songs",
                                             filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        for song in songs:
            self.playlist.insert("end", os.path.basename(song))

    def play(self):
        if self.playlist.curselection():
            song_index = self.playlist.curselection()[0]
            song_path = self.playlist.get(song_index)
            if self.current_song != song_path:
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                self.current_song = song_path

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song = None

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
