import os
from fastapi import UploadFile
from pathlib import Path

UPLOAD_DIRECTORY = Path(__file__).parent / "uploads"

if not UPLOAD_DIRECTORY.exists():
    os.makedirs(UPLOAD_DIRECTORY)

def save_file(upload_file: UploadFile) -> str:
    file_path = UPLOAD_DIRECTORY / upload_file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return str(file_path)

def delete_file(file_path: str):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
