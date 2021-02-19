import logging.config
import os

logger = logging.getLogger(__name__)

DEBUG = True
DEBUG_AUDIO_AS_TEXT = True

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.abspath(os.path.join(PROJECT_PATH, "data"))
STYLE_FILENAME = os.path.join(DATA_PATH, "style.kv")
