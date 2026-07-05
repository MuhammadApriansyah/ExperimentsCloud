from hashlib import sha256
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
from mutagen import File as MutagenFile


class MetadataGenerator:

    @staticmethod
    def checksum(path):

        path = Path(path)

        digest = sha256()

        with path.open("rb") as file:

            while True:

                chunk = file.read(8192)

                if not chunk:
                    break

                digest.update(chunk)

        return digest.hexdigest()


    @staticmethod
    def image_size(path):

        path = Path(path)

        with Image.open(path) as image:

            return (
                image.width,
                image.height,
            )


    @staticmethod
    def pdf_page_count(path):

        path = Path(path)

        reader = PdfReader(path)

        return len(reader.pages)


    @staticmethod
    def audio_duration(path):

        path = Path(path)

        audio = MutagenFile(path)

        if (
            audio is None
            or not hasattr(audio, "info")
            or audio.info is None
        ):
            return None

        return int(audio.info.length)
