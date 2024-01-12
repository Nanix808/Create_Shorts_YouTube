from abc import ABC, abstractmethod


class TextToAudio(ABC):
    @abstractmethod
    def text_to_audio(self):
        pass

    @abstractmethod
    def save_audio_to_mp3(self):
        pass

    @abstractmethod
    def play_audio(self):
        pass