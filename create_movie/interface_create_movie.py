from abc import ABC, abstractmethod


class CreateMovie(ABC):
    @abstractmethod
    def create_video(self):
        pass

   
