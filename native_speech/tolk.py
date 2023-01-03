import cytolk

from .base_speaker import BaseSpeaker

class Speaker(BaseSpeaker):
    def __init__(self, *, try_sapi: bool = True, prefer_sapi: bool = False, tolk_extended_search_path: bool = None, **kwargs):
        cytolk.try_sapi(try_sapi)
        cytolk.prefer_sapi(prefer_sapi)

        if tolk_extended_search_path is None: tolk_extended_search_path = "__compiled__" in globals()
        if not cytolk.load(tolk_extended_search_path):
            raise RuntimeError("Could not initialize cytolk")

    def __del__(self):
        cytolk.unload()

    def speak(self, text: str, interrupt: bool = True):
        cytolk.output(text, interrupt)

    def stop(self):
        cytolk.silence()
