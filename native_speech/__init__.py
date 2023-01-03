import sys

from .base_speaker import BaseSpeaker

clamp = lambda x, min, max: min if x < min else max if x > max else x

match sys.platform:
    case "darwin": from .ns_speech import Speaker
    case "linux": from .speech_dispatcher import Speaker
    case "win32": from .tolk import Speaker
    case other: raise RuntimeError(f"Unsupported platform: {other}")
