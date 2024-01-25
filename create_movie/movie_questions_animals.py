from create_movie.interface_create_movie import CreateMovie
from moviepy.editor import *


class CreateVideoAnimalsMoviepy(CreateMovie):
    def __init__(
        self,
        question: str,
        answer: str,
        audio_question: str,
        audio_answer: str,
        audio_promting: str,
        answer_image: str = None,
        background_video: str = "background_animals/background.mp4",
        background_audio: str = "background/background.mp3",
        countback: int = 7,
        name_chanel: str = "@codecases808",
    ) -> None:
        self.question = question
        self.answer = answer
        self.audio_question = audio_question
        self.audio_answer = audio_answer
        self.audio_promting = audio_promting
        self.answer_image = answer_image
        self.countback = countback
        self.background_video = background_video
        self.background_audio = background_audio
        self.name_chanel = name_chanel
        self.countainer_movie = []
        self.path = None

    def create_video(self):
        # Create audioclips questions and answer
        audioclip_question = AudioFileClip(self.audio_question)
        audioclip_answer = AudioFileClip(self.audio_answer)
        audioclip_promting = AudioFileClip(self.audio_promting)

        # find out the duration of the question
        duration = audioclip_question.duration
        image = (
            ImageClip(self.answer_image)
            .set_duration(5)
            .set_start(duration + self.countback + 0.5)
        )

        # Set the frames per second
        image.fps = 30
        image = image.set_position(lambda t: ("center", 50 + t))
        # remove artifact audio of the questions
        audioclip_question = audioclip_question.set_duration(duration - 0.1)

        # create backround videoclip
        video = (
            VideoFileClip(self.background_video)
            .fx(vfx.resize, width=1080)
            .fx(vfx.resize, height=1920)
            .fx(vfx.loop)
            .set_duration(duration + self.countback + 5)
        )

        # add backround audio
        video.audio = AudioFileClip(self.background_audio).set_duration(
            duration + self.countback + 5
        )

        # make background music quieter
        video = video.volumex(0.3)

        # Create countdown timer
        cliplist = []
        for time in range(self.countback, 0, -1):
            countdown_clip = TextClip(
                str(time),
                font="ArialUnicode",
                fontsize=200.0,
                color="green",
                method="caption",
                size=(920, 200),
            )
            countdown_clip = (
                countdown_clip.set_position((80, 1500))
                .set_duration(1.0)
                .set_start(duration + 0.5 + self.countback - time)
            )
            cliplist.append(countdown_clip)

        # Make the text of question
        txt_question = (
            TextClip(
                self.question,
                font="Arial",
                fontsize=80,
                color="green",
                method="caption",
                size=(920, 1400),
            )
            .set_position((80, 60))
            .set_duration(duration + self.countback)
        )

        # add audioclip_question
        txt_question.audio = audioclip_question.set_start(1)

        # Make the text of answer
        txt_answer = (
            TextClip(
                self.answer,
                font="Arial",
                fontsize=150,
                color="green",
                method="caption",
                size=(920, 1400),
            )
            .set_position((80, 60))
            .set_duration(4.5)
            .set_start(duration + self.countback + 0.5)
        )
        txt_answer.audio = audioclip_answer.set_start(duration + self.countback + 0.5)

        # Make the text of chanel
        txt_chanel = (
            TextClip(
                self.name_chanel,
                font="Arial",
                fontsize=30,
                color="black",
                method="caption",
                size=(920, 30),
            )
            .set_position((80, 1830))
            .set_duration(duration + self.countback + 5)
        )
        if audioclip_promting.duration >= 2:
            audioclip_promting = audioclip_promting.set_duration(2)
        txt_chanel.audio = audioclip_promting.set_start(
            duration + self.countback / 2 + 1
        )

        self.countainer_movie = CompositeVideoClip(
            [video, txt_question, txt_answer, txt_chanel, image] + cliplist
        )

        return self

    def save_video(self):
        self.path = f"download/{self.question[:99]}.mp4"
        self.countainer_movie.write_videofile(self.path)
        return self
