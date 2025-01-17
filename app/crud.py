from sqlalchemy.orm import Session
from .models import File

def create_file(db: Session, filename: str, file_url: str):
    db_file = File(filename=filename, file_url=file_url)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_file(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()

def delete_file(db: Session, file_id: int):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file:
        db.delete(db_file)
        db.commit()
    return db_file
