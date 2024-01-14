from elevenlabs import generate, play, voices, save, VoiceSettings, Voice
from text_to_audio.interface_text_to_audio import TextToAudio


QUESTION = "Привет"
ANSWER = "Привет"


class TextToAudioElevenlabs(TextToAudio):
    def __init__(self, text: str, api_key: str) -> None:
        self.text = text
        self.api_key = api_key
        self.voices = voices()

    def text_to_audio(self):
        audio = generate(
            text=self.text,
            api_key=self.api_key,
            voice=Voice(
                voice_id="pqHfZKP75CvOlQylNhV4",
                settings=VoiceSettings(
                    stability=0.71,
                    similarity_boost=0.5,
                    style=0.0,
                    use_speaker_boost=True,
                ),
            ),
            model="eleven_multilingual_v2",
        )

        # audio = generate(
        #     api_key=self.api_key,
        #     text=self.text,
        #     voice=self.voices[38],
        #     model="eleven_multilingual_v2",
        # )
        # print(self.voices[38])
        return audio

    def save_audio_to_mp3(self, audio):
        name = self.text[:5]
        full_name = f"download_audio/{name}.mp3"
        save(audio, f"{full_name}")
        return full_name

    def play_audio(self, audio):
        play(audio)


# a = TextToAudioElevenlabs("Привет", "999d59e05fbe9884cf868f80fc58f66e")
# s = a.text_to_audio()
# a.save_audio_to_mp3(s)
