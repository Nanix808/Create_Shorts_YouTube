import os
from elevenlabs import generate, play, voices, set_api_key, save
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("ELEVEN_API_KEY")