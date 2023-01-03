from cytolk import tolk

from .base_speaker import BaseSpeaker

class Speaker(BaseSpeaker):
    def __init__(self, *, try_sapi: bool = True, prefer_sapi: bool = False, tolk_extended_search_path: bool = None, **kwargs):
        tolk.try_sapi(try_sapi)
        tolk.prefer_sapi(prefer_sapi)

        if tolk_extended_search_path is None: tolk_extended_search_path = "__compiled__" not in globals()
        tolk.load(tolk_extended_search_path)

    def __del__(self):
        tolk.unload()

    def speak(self, text: str, interrupt: bool = True):
        tolk.output(text, interrupt)

    def speak_char(self, character: str, interrupt: bool = True):
        tolk.output(character, interrupt)

    def speak_key(self, key: str, interrupt: bool = True):
        tolk.output(key, interrupt)

    def stop(self):
        tolk.silence()
