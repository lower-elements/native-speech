import sys

match sys.platform:
    case "linux": from .speech_dispatcher import *
    case other: raise Warning(f"Unsupported platform: {other}")
