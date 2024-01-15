from abc import ABC, abstractmethod


class CreateMovie(ABC):
    @abstractmethod
    def create_video(self):
        pass

    @abstractmethod
    def save_video(self):
        pass
