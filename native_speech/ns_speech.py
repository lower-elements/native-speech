# Inspired by and adapted from Steel TTS code <http://sourceforge.net/projects/steeltts/>

try:
    from AppKit import NSSpeechSynthesizer
except ImportError:
    from Cocoa import NSSpeechSynthesizer

from . import clamp
from .base_speaker import BaseSpeaker

class Speaker(BaseSpeaker):
    __slots__ = ["_tts"]

    def __init__(self, **kwargs):
        self._tts = NSSpeechSynthesizer.alloc().initWithVoice_(None)

    def speak(self, text: str, interrupt: bool =True):
        if interrupt: self._tts.stopSpeaking()
        self._tts.startSpeakingString_(text)

    def speak_char(self, character: str, interrupt: bool =True):
        if interrupt: self._tts.stopSpeaking()
        self._tts.startSpeakingString_(character)

    def speak_key(self, key: str, interrupt: bool =True):
        if interrupt: self._tts.stopSpeaking()
        self._tts.startSpeakingString_(key)

    def stop(self):
        self._tts.stopSpeaking()

    @property
    def supports_rate(self) -> bool:
        return True

    @property
    def rate(self) -> float:
            return clamp((self._tts.rate() - 50) / 600.0, 0.0, 1.0)

    @rate.setter
    def rate(self, val: float):
        val = clamp(val, 0.0, 1.0)
        self._tts.setRate_((val * 600.0) + 50)

    @property
    def supports_volume(self) -> bool:
        return True

    @property
    def volume(self) -> float:
            return self._tts.volume()

    @volume.setter
    def volume(self, val: float):
        val = clamp(val, 0.0, 1.0)
        self._tts.setVolume_(val)
