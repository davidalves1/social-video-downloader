# Social Video Downloader

## Requirements
- Python 3
- Pip
- Venv (native on Python > 3.3)

## Running

1. Create a Virtual Environment with inside venv dir with `venv`: `python -m venv ./venv`
2. Start the Virtual Environment: `source venv/bin/activate`
3. Install all dependencies: `pip install -r requirements.txt`
4. Start the API: `flask run`
5. Access by GET (For now only linkedin is available): `http://localhost:5000/linkedin?video_url={a valid linkedin video url}`