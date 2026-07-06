from pathlib import Path
import subprocess

from app.services.video_metadata_service import (
    VideoMetadataService,
)


def create_video(path):

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "color=c=black:s=320x240:d=1",
            "-c:v",
            "libx264",
            str(path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_extract_video_metadata(tmp_path):

    video = tmp_path / "sample.mp4"

    create_video(video)

    metadata = VideoMetadataService.extract(video)
    print(metadata)
    assert isinstance(metadata, dict)

    assert metadata["duration"] is not None

    assert metadata["width"] == 320

    assert metadata["height"] == 240

    assert metadata["fps"] > 0

    assert metadata["codec"] is not None

    assert "bitrate" in metadata
