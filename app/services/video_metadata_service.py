import json
import subprocess
from pathlib import Path


class VideoMetadataService:

    @staticmethod
    def extract(path):

        path = Path(path)

        result = subprocess.run(
            [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        raw = json.loads(result.stdout)

        return VideoMetadataService._parse_metadata(raw)

    @staticmethod
    def _parse_metadata(data):

        video_stream = next(
            (
                stream
                for stream in data.get("streams", [])
                if stream.get("codec_type") == "video"
            ),
            {},
        )

        format_info = data.get("format", {})

        fps = VideoMetadataService._parse_frame_rate(
            video_stream.get("avg_frame_rate")
        )

        return {
            "duration": (
                float(format_info["duration"])
                if format_info.get("duration")
                else None
            ),
            "width": video_stream.get("width"),
            "height": video_stream.get("height"),
            "fps": fps,
            "codec": video_stream.get("codec_name"),
            "bitrate": (
                int(format_info["bit_rate"])
                if format_info.get("bit_rate")
                else None
            ),
        }

    @staticmethod
    def _parse_frame_rate(value):

        if not value or value == "0/0":
            return None

        numerator, denominator = value.split("/")

        return round(
            float(numerator) / float(denominator),
            2,
        )
