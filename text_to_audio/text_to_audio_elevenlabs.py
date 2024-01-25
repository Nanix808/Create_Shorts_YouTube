from elevenlabs import generate, play, voices, save, VoiceSettings, Voice
from text_to_audio.interface_text_to_audio import TextToAudio
import os


class TextToAudioElevenlabs(TextToAudio):
    def __init__(self, text: str, api_key: str) -> None:
        self.text = text
        self.api_key = api_key
        self.voices = voices()
        self.audio = None
        self.path = None

    def text_to_audio(self):
        self.audio = generate(
            text=self.text,
            api_key=self.api_key,
            voice=Voice(
                voice_id="EXAVITQu4vr4xnSDxMaL",
                name="Aphrodite",
                settings=VoiceSettings(
                    stability=0.3,
                    similarity_boost=0.7,
                    style=0.0,
                    use_speaker_boost=True,
                ),
            ),
            model="eleven_multilingual_v2",
        )
        return self

    def delete_audio(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def save_audio_to_mp3(self):
        self.path = f"download_audio/{self.text[:10]}.mp3"
        save(self.audio, self.path)
        return self

    def play_audio(self):
        play(self.audio)
