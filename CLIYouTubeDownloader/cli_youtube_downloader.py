import pathlib
from dataclasses import dataclass
from typing import Union

import ffmpeg
from pytube import YouTube
from rich.console import Console
from rich.table import Table

# TODO: Playlist download

BASE_DIR = pathlib.Path.cwd()


@dataclass
class Downloader:
    url: str

    def __post_init__(self):
        self.file_size = 0
        self.youtube = YouTube(
            self.url, on_progress_callback=Downloader.progress)
        self.display_info()

    def display_info(self):
        self.stream_number = 1
        self.streams = self.youtube.streams.filter(adaptive=True)

        console = Console()

        table = Table(
            show_header=True,
            header_style='bold',
            title=f'\n[bold]{self.youtube.title}'
        )
        table.add_column('Number', justify='right')
        table.add_column('Mime Type', justify='center')
        table.add_column('FPS', justify='center')
        table.add_column('Resolution', justify='center')

        for stream in self.streams:
            table.add_row(
                f'{self.stream_number}', f'[orange1]{stream.mime_type}',
                f'{stream.fps}', f'[green]{stream.resolution}'
            )
            self.stream_number += 1

        console.print(table)

        self.choose_stream()

    def choose_stream(self):
        choice = int(input('\nPlease select one of the above: '))
        self.validate_choose_val(choice)

    def validate_choose_val(self, choice: int):
        if choice in range(1, self.stream_number):
            self.get_stream(choice)
        else:
            print('Invalid option. Choose correct one.')
            self.choose_stream()

    def get_stream(self, choice: int):
        self.video_stream = self.streams[choice - 1]
        mime_type_ext = self.video_stream.mime_type.split('/')[-1]
        self.audio_stream = self.streams.filter(
            mime_type=f'audio/{mime_type_ext}')[0]

        global file_size
        file_size = (self.video_stream.filesize + self.audio_stream.filesize) / 10**6

        self.get_permission(mime_type_ext)

    def get_permission(self, mime_type_ext: str):
        print('\n\tTitle: {0} \n\tAuthor: {1} \n\tSize: {2:.2f}MB \n\tResolution: {3} \n\tFPS: {4}'.format(
            self.youtube.title, self.youtube.author,
            file_size, self.video_stream.resolution,
            self.video_stream.fps)
        )

        if input('\nDo you want to continue? (yes / no)') == 'yes':
            self.download(mime_type_ext)
        else:
            self.display_info()

    def download(self, mime_type_ext: str):
        self.video_stream.download(output_path='tmp', filename='video')
        self.audio_stream.download(output_path='tmp', filename='audio')

        video_path = BASE_DIR.joinpath('tmp', f'video.{mime_type_ext}')
        audio_path = BASE_DIR.joinpath('tmp', f'audio.{mime_type_ext}')

        input_video = ffmpeg.input(video_path)
        input_audio = ffmpeg.input(audio_path)

        ffmpeg.concat(
            input_video, input_audio,
            v=1, a=1
        ).output(f'{self.youtube.title}.mp4').run()

    @staticmethod
    def progress(stream=None, chunk=None, remaining=None):
        file_downloaded = (file_size - (remaining / 10**6))
        print(f"downloading ... {file_downloaded/file_size*100:0.2f} % [{file_downloaded:.1f}MB of {file_size:.1f}MB]", end="\r")


def validate(url: str) -> Union[str, bool]:
    path = pathlib.PurePath(url)

    if path.parent == pathlib.PurePath('https://music.youtube.com'):
        return f'https://www.youtube.com/{path.parts[-1]}'
    elif path.parent == pathlib.PurePath('https://www.youtube.com'):
        return url

    return False


if __name__ == "__main__":
    valid = False
    url = None

    while not valid:
        user_input = str(input("Enter the url of video: "))
        url = validate(user_input)

        if url:
            valid = True

    Downloader(url)
