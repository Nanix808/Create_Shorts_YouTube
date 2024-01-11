from elevenlabs import generate, play, voices, set_api_key, save
from config import API_KEY

QUESTION = "Привет"
ANSWER = "Привет"


class TextToAudioElevenlabs:
    def __init__(self, questions: list, answers: list, api_key: str) -> None:
        self.questions = questions
        self.answers = answers
        self.api_key = api_key
        self.voices = voices()

    def text_to_audio(self):
        for question in self.questions:
            audio = generate(
                api_key=self.api_key,
                text=question,
                voice=self.voices[38],
                model="eleven_multilingual_v2",
            )
            name = "question_" + question[:5]
            self.save_audio_to_mp3(audio, name)

        for answer in self.answers:
            audio = generate(
                api_key=self.api_key,
                text=answer,
                voice=self.voices[38],
                model="eleven_multilingual_v2",
            )
            name = "answer_" + answer[:5]
            return self.save_audio_to_mp3(audio, name)

    def save_audio_to_mp3(self, audio, name):
        full_name = f"download_audio/{name}.mp3"
        save(audio, f"download_audio/{full_name}")
        return full_name

    def play_audio(self, audio):
        play(audio)


TextToAudioElevenlabs([QUESTION], [ANSWER], API_KEY).text_to_audio()
