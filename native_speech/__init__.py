import sys

from .base_speaker import BaseSpeaker

match sys.platform:
    case "linux": from .speech_dispatcher import Speaker
    case other: raise RuntimeError(f"Unsupported platform: {other}")
