import yt_dlp
from datetime import datetime
from pathlib import Path

# Папка загрузки
DOWNLOAD_DIR = Path("download")
DOWNLOAD_DIR.mkdir(exist_ok=True)

async def download_tiktok_video(url: str) -> str | None:
    """Скачивает видео из TikTok и возвращает путь к файлу, либо None."""
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = DOWNLOAD_DIR / f"{date_str}.mp4"

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': str(output_path),
        'quiet': True,
        'noplaylist': True,
        'ignoreerrors': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
        return str(output_path) if output_path.exists() else None
    except Exception:
        return None
