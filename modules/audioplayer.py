import subprocess
import time
from threading import Event, Thread

import pyaudio

CHUNK = 1024


class AudioPlayer:
    def __init__(self) -> None:
        self.audio_playing: bool = False
        self.current_audio_thread_event: Event = Event()
        self.audio_main_thread = Thread(name="main_thread", target=self.audio_handler)
        self.audio_main_thread.start()
        self.song_data = None
        self.song = subprocess.Popen[bytes]
        self.audio_stream = None
        self.current_audio_path: str
        self.can_play: bool = False

    def start_audio(self, audio_path: str):
        self.current_audio_thread_event.set()
        if self.audio_stream == None:
            self.initialize_audio(audio_path)
            self.current_audio_path = audio_path

    def reset_audio(self):
        if hasattr(self, "song") and self.song:
            self.song.terminate()  # type: ignore
        if self.song.stdout:
            self.song_data = self.song.stdout.read(CHUNK)
        else:
            self.song_data = b""

        self.initialize_audio(self.current_audio_path)

    def pause_audio(self):
        self.current_audio_thread_event.clear()

    def change_audio(self, new_audio_path: str):
        if self.audio_stream:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
            self.audio_stream = None
            self.song.terminate()  # type: ignore
        self.initialize_audio(new_audio_path)

    def initialize_audio(self, audio_path: str):

        self.song = subprocess.Popen(
            [
                "ffmpeg.exe",
                "-i",
                audio_path,
                "-loglevel",
                "panic",
                "-vn",
                "-f",
                "s16le",
                "pipe:1",
            ],
            stdout=subprocess.PIPE,
        )

        p = pyaudio.PyAudio()

        # open stream (2)
        self.audio_stream = p.open(
            format=pyaudio.paInt16,
            channels=2,  # use ffprobe to get this from the file beforehand
            rate=44100,  # use ffprobe to get this from the file beforehand
            output=True,
        )
        self.song_data = self.song.stdout.read(CHUNK)  # type: ignore

    def audio_handler(self):
        while True:
            self.current_audio_thread_event.wait()
            # event is set is basically the the play button
            can_play = (
                self.song_data is not None
                and self.song.stdout is not None
                and len(self.song_data) > 0
                and self.audio_stream is not None
                and not self.audio_stream.is_stopped()
            )
            # Audio started
            if can_play:
                print("playing!")
                self.audio_stream.write(self.song_data)
                self.song_data = self.song.stdout.read(CHUNK)
            else:
                time.sleep(0.01)
