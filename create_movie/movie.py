from create_movie.interface_create_movie import CreateMovie
from moviepy.editor import *

# QUESTION = "У ног кузовок: Кто за ней ходит, того она и кормит. Два бодаста, четыре ходаста, Один хлестун"
# ANSWER = "Корова"


class CreateVideoMoviepy(CreateMovie):
    def __init__(
        self,
        question: str,
        answer: str,
        audio_question: str,
        audio_answer: str,
        background_video: str = "backgound/background.mp4",
        background_audio: str = "backgound/background.mp3",
        countback: int = 7,
        name_chanel: str = "@codecases808",
    ) -> None:
        self.question = question
        self.answer = answer
        self.audio_question = audio_question
        self.audio_answer = audio_answer
        self.countback = countback
        self.background_video = background_video
        self.background_audio = background_audio
        self.name_chanel = name_chanel

    def create_video(self):
        audioclip = AudioFileClip(f"{self.audio_question}")
        audioclip_answer = AudioFileClip(f"{self.audio_answer}")
        duration = audioclip.duration

        audioclip = audioclip.set_duration(duration - 0.1)

        video = (
            VideoFileClip(self.background_video)
            .fx(vfx.resize, width=1080)  # resize
            .fx(vfx.resize, height=1920)  # resize
            .fx(vfx.loop)  # loop
            .set_duration(duration + self.countback + 5)
            # .audio_fadeout(20)
        )
        video.audio = audioclip
        video.audio = AudioFileClip(self.background_audio).set_duration(
            duration + self.countback + 5
        )
        video = video.volumex(0.3)
        # Create countdown timer
        cliplist = []
        for time in range(self.countback, 0, -1):
            countdown_clip = TextClip(
                str(time),
                font="ArialUnicode",
                fontsize=200.0,
                color="white",
                method="caption",
                size=(1000, 200),
            )
            countdown_clip = (
                countdown_clip.set_position((40, 1500))
                .set_duration(1.0)
                .set_start(duration + 0.5 + self.countback - time)
            )
            cliplist.append(countdown_clip)

        # Make the text. Many more options are available.
        txt_question = (
            TextClip(
                self.question,
                font="Arial",
                fontsize=80,
                color="white",
                method="caption",
                size=(1000, 1400),
            )
            .set_position((40, 60))
            .set_duration(duration + 7)
        )
        txt_question.audio = audioclip.set_start(1)

        txt_chanel = (
            TextClip(
                self.name_chanel,
                font="Arial",
                fontsize=30,
                color="black",
                method="caption",
                size=(1000, 30),
            )
            .set_position((40, 1830))
            .set_duration(duration + self.countback + 5)
        )

        txt_answer = (
            TextClip(
                self.answer,
                font="Arial",
                fontsize=150,
                color="white",
                method="caption",
                size=(1000, 1400),
            )
            .set_position((40, 60))
            .set_duration(4.5)
            .set_start(duration + 7.5)
        )
        txt_answer.audio = audioclip_answer.set_start(duration + 7.5)

        result = CompositeVideoClip(
            [video, txt_question, txt_answer, txt_chanel] + cliplist
        )  # Overlay text on video
        # result.preview()
        result.write_videofile(f"download/{self.question[:99]}.mp4")  # Many options...


# CreateVideoMoviepy(QUESTION, ANSWER, "У ног кузо.mp3", "Корова..mp3").create_video()
