# File Upload and Download API

This is a simple **FastAPI** application that allows users to upload, download, and delete files. It stores file metadata in an **SQLite** database and handles the actual file storage on the server.

## Features:
- **Upload**: Upload files to the server.
- **Download**: Retrieve files by their unique ID.
- **Delete**: Delete files from the server and the database.

## Requirements:
- FastAPI
- Uvicorn
- SQLAlchemy
- python-multipart

## Setup Instructions:

1. Clone the repository:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```


## API Endpoints:

- **POST /upload/**: Upload a file.
  - Request body: `multipart/form-data` with the file.
  - Response: JSON with `file_id` and `filename`.

- **GET /download/{file_id}**: Download a file.
  - Response: File download.

- **DELETE /delete/{file_id}**: Delete a file.
  - Response: JSON message with success.
