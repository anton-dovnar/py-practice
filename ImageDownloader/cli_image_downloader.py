import pathlib
from datetime import date
from io import BytesIO

import requests
from PIL import Image
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import (
    BarColumn,
    Progress,
    TimeRemainingColumn,
)

BASE_DIR = pathlib.Path.cwd()

VALID_IMAGE_EXTENSIONS = [
    '.jpg',
    '.jpeg',
    '.png',
    '.gif',
]


def validate_url(url: str, extension: str) -> bool:
    if url.startswith('https://') and extension:
        return True

    return False


def download(url: str, extension: str):
    today = date.today().strftime('%d-%m-%Y')
    file_path = BASE_DIR.joinpath('downloaded', f'{today}{extension}')
    response = requests.get(url)

    if response.status_code == 200:
        with Image.open(BytesIO(response.content)) as img:
            img.save(file_path)

        print(f'Dowloading form: {url} saving to: {file_path}')


if __name__ == '__main__':
    files = []
    valid = False

    console = Console()

    with open('README.md') as readme:
        markdown = Markdown(readme.read())

    console.print(markdown)

    while not valid:
        urls = input('Enter URL address: ')

        for url in urls.split(','):
            suffix = pathlib.PurePath(url).suffix
            extension = suffix if suffix in VALID_IMAGE_EXTENSIONS else False
            valid = validate_url(url, extension)
            if valid:
                files.append((url, extension))

    progress = Progress(
        '[progress.description]{task.description}',
        BarColumn(),
        '[magenta]{task.completed} of {task.total} files downloaded',
        TimeRemainingColumn()
    )

    with progress:
        task = progress.add_task("Downloading files...", total=len(files))
        for image_url, extension in files:
            download(image_url, extension)
            progress.update(task, advance=1)
