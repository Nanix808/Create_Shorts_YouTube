from openpyxl import load_workbook
from text_to_audio.text_to_audio_elevenlabs import TextToAudioElevenlabs
from create_movie.movie_question_answer import CreateVideoMoviepy
from create_movie.movie_questions_animals import CreateVideoAnimalsMoviepy


from config import API_KEY

wb = load_workbook(filename="questions/questions.xlsx")

sheet_ranges = wb["Лист1"]
QUESTIONS = []
ANSWER = []


for n, q, a in sheet_ranges:
    if q.value and n.value and n.value != "№" and int(n.value) == 2:
        question = (
            TextToAudioElevenlabs(q.value, API_KEY).text_to_audio().save_audio_to_mp3()
        )
        answer = (
            TextToAudioElevenlabs(a.value, API_KEY).text_to_audio().save_audio_to_mp3()
        )

        CreateVideoAnimalsMoviepy(
            q.value,
            a.value,
            "download_audio\На овчарку.mp3",
            "download_audio\Волк.mp3",
            "sound_animals\Волк.mp3",
            "background_animals_pictures\Волк.jpg",
        ).create_video().save_video()
        # CreateVideoMoviepy(
        #     q.value, a.value, "download_audio\Корова..mp3", "download_audio\Корова..mp3"
        # ).create_video().save_video()
        # question.delete_audio()
        # answer.delete_audio()
