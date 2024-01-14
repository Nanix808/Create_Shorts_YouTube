from openpyxl import load_workbook
from text_to_audio.text_to_audio_elevenlabs import TextToAudioElevenlabs
from create_movie.movie import CreateVideoMoviepy
from config import API_KEY

wb = load_workbook(filename="questions/questions.xlsx")

sheet_ranges = wb["Лист1"]
QUESTIONS = []
ANSWER = []


for n, q, a in sheet_ranges:
    if q.value and n.value and n.value != "№" and int(n.value) > 47:
        question = TextToAudioElevenlabs(q.value, API_KEY)
        answer = TextToAudioElevenlabs(a.value, API_KEY)
        question_audio = question.text_to_audio()
        answer_audio = answer.text_to_audio()
        question_path = question.save_audio_to_mp3(question_audio)
        answer_path = answer.save_audio_to_mp3(answer_audio)
        QUESTIONS.append(q.value)
        ANSWER.append(a.value)
        CreateVideoMoviepy(q.value, a.value, question_path, answer_path).create_video()
# print(QUESTIONS, ANSWER)
# a = TextToAudioElevenlabs("Привет", API_KEY)
# s = a.text_to_audio()
# a.save_audio_to_mp3(s)
# from elevenlabs import generate, play, Voice, VoiceSettings


# audio = generate(
#     text="Что бывает один раз в минуту, два раза в момент, но никогда не в тысячу лет?",
#     api_key=API_KEY,
#     voice=Voice(
#         voice_id="pqHfZKP75CvOlQylNhV4",
#         settings=VoiceSettings(
#             stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True
#         ),
#     ),
#     model="eleven_multilingual_v2",
# )

# play(audio)
