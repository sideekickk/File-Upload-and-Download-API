from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models, crud, utils

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI setup
app = FastAPI()

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_file(upload_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save the file to the disk
    file_path = utils.save_file(upload_file)
    
    # Save file metadata to the database
    db_file = crud.create_file(db, upload_file.filename, file_path)
    
    return {"file_id": db_file.id, "filename": db_file.filename}

@app.get("/download/{file_id}")
async def download_file(file_id: int, db: Session = Depends(get_db)):
    db_file = crud.get_file(db, file_id)
    
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(db_file.file_url)

@app.delete("/delete/{file_id}")
async def delete_file(file_id: int, db: Session = Depends(get_db)):
    db_file = crud.get_file(db, file_id)
    
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Delete the file from the disk
    utils.delete_file(db_file.file_url)
    
    # Delete the file metadata from the database
    crud.delete_file(db, file_id)
    
    return {"message": "File deleted successfully"}
