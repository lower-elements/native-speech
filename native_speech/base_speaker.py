from abc import ABC, abstractmethod

class BaseSpeaker(ABC):
    """
    An abstract base class that defines the interface for all Speaker objects.

    When implementing this interface, Speakers must emulate or otherwise silently ignore features they don't support.
    This allows the user of the library to use these features without having to worry about if they're supported. Users
    who wish to determine if features are supported can use the supports_* family of properties.
    """

    __slots__ = []

    def __init__(self, **kwargs):
        """
        Initialize the Speaker object.

        All implementations must accept arbitrary keyword arguments, and only take action based on the arguments they
        support.
        """
        pass

    @abstractmethod
    def speak(self, text: str, interrupt: bool = True):
        """
        Synthesize the given text.

        If interrupt is True, the text should be spoken immediately, cancelling any speaking or queued messages.
        """
        pass

    @abstractmethod
    def speak_char(self, character: str, interrupt: bool = True):
        """
        Speak the given character, as if it was echoed while reviewing text with the caret.

        If interrupt is True, the text should be spoken immediately, cancelling any speaking or queued messages.
        
        Implementations may choose to speak only the first unicode character in the passed string.
        
        If the implementation does not support this feature, it must emulate it as a call to the speak() method.
        """
        pass

    @abstractmethod
    def speak_key(self, key: str, interrupt: bool = True):
        """
        Speak the given key, as if it was echoed in response to the user pressing the key.

        If interrupt is True, the text should be spoken immediately, cancelling any speaking or queued messages.

        If the implementation does not support this feature, it must emulate it as a call to the speak_char() method, or
        as a call to the speak() method if speak_char() is also not supported.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Silence all speaking and queued messages from this client.

        Implementations may choose to silence messages from all currently running clients, however this is discouraged.

        If the implementation does not support this feature, it must silently ignore a call to this method.
        """
        pass

    @property
    def supports_rate(self) -> bool:
        """ Returns a boolean indicating whether the Speaker supports getting and setting the speech rate. """
        return False

    @property
    @abstractmethod
    def rate(self) -> float:
        """
        Get the current speech rate.

        The returned value is a float between 0.0 (slowest) and 1.0 (fastest)

        If the implementation does not support this feature, it must return 0.5, indicating an average rate.
        """
        pass

    @rate.setter
    @abstractmethod
    def rate(self, val: float):
        """
        Set the speech rate.

        val should be a float between 0.0 (slowest) and 1.0 (fastest)

        Implementations must transparently clamp the value between 0.0 and 1.0 (inclusive), and must not raise an
        exception when an out-of-bounds rate is passed.

        If the implementation does not support this feature, it must silently ignore the request.
        """
        pass

    @property
    def supports_pitch(self) -> bool:
        """ Returns a boolean indicating whether the Speaker supports getting and setting the speech pitch. """
        return False

    @property
    @abstractmethod
    def pitch(self) -> float:
        """
        Get the current speech pitch.

        The returned value is a float between 0.0 (lowest) and 1.0 (highest)

        If the implementation does not support this feature, it must return 0.5, indicating an average pitch.
        """
        pass

    @pitch.setter
    @abstractmethod
    def pitch(self, val: float):
        """
        Set the speech pitch.

        val should be a float between 0.0 (lowest) and 1.0 (highest)

        Implementations must transparently clamp the value between 0.0 and 1.0 (inclusive), and must not raise an
        exception when an out-of-bounds pitch is passed.

        If the implementation does not support this feature, it must silently ignore the request.
        """
        pass

    @property
    def supports_volume(self) -> bool:
        """ Returns a boolean indicating whether the Speaker supports getting and setting the speech volume. """
        return False

    @property
    @abstractmethod
    def volume(self) -> float:
        """
        Get the current speech volume.

        The returned value is a float between 0.0 (quietest) and 1.0 (loudest)

        If the implementation does not support this feature, it must return 1.0, indicating full volume.
        """
        pass

    @volume.setter
    @abstractmethod
    def volume(self, val: float):
        """
        Set the speech volume.

        val should be a float between 0.0 (quietest) and 1.0 (loudest)

        Implementations must transparently clamp the value between 0.0 and 1.0 (inclusive), and must not raise an
        exception when an out-of-bounds pitch is passed.

        If the implementation does not support this feature, it must silently ignore the request.
        """
        pass
