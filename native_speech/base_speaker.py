from abc import ABC, abstractmethod

class BaseSpeaker(ABC):
    __slots__ = []

    def __init__(self, program_name: str):
        pass

    @abstractmethod
    def speak(self, text: str, interrupt: bool = True):
        pass

    @abstractmethod
    def speak_char(self, character: str, interrupt: bool = True):
        pass

    @abstractmethod
    def speak_key(self, key: str, interrupt: bool = True):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def rate(self) -> float:
        pass

    @rate.setter
    @abstractmethod
    def rate(self, val: float):
        pass

    @property
    @abstractmethod
    def pitch(self) -> float:
        pass

    @pitch.setter
    @abstractmethod
    def pitch(self, val: float):
        pass

    @property
    @abstractmethod
    def volume(self) -> float:
        pass

    @volume.setter
    @abstractmethod
    def volume(self, val: float):
        pass
