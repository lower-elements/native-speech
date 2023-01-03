import speechd

clamp = lambda x, min, max: min if x < min else max if x > max else x

class Speaker:
    __slots__ = ["_speaker"]

    def __init__(self, name: str):
        self._speaker = speechd.Speaker(name)

    def speak(self, text: str, interrupt: bool = True):
        if interrupt: self._speaker.cancel()
        self._speaker.speak(text)

    def speak_char(self, character: str, interrupt: bool = True):
        if interrupt: self._speaker.cancel()
        self._speaker.char(character)

    def speak_key(self, key: str, interrupt: bool = True):
        if interrupt: self._speaker.cancel()
        self._speaker.key(key if key != ' ' else 'space')

    def stop(self):
        self._speaker.cancel()

    @property
    def rate(self) -> float:
        return (int(self._speaker.get_rate()) + 100) / 200.0

    @rate.setter
    def rate(self, val: float):
        val = clamp(val, 0.0, 1.0)
        self._speaker.set_rate(int((val * 200) - 100))

    @property
    def pitch(self) -> float:
        return (int(self._speaker.get_pitch()) + 100) / 200.0

    @pitch.setter
    def pitch(self, val: float):
        val = clamp(val, 0.0, 1.0)
        self._speaker.set_pitch(int((val * 200) - 100))

    @property
    def volume(self) -> float:
        return (int(self._speaker.get_volume()) + 100) / 200.0

    @volume.setter
    def volume(self, val: float):
        val = clamp(val, 0.0, 1.0)
        self._speaker.set_volume(int((val * 200) - 100))
