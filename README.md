### system-wide dependencies
Ensure that ffmpeg is installed systemwide, this is required for handling audio files and tts.

FOR WINDOWS
```
winget install ffmpeg
```

FOR MACOS
```
homebrew install ffmpeg
```

FOR DEBIAN 
```
sudo apt install ffmpeg
```

### how to run it?
```bash
flask run
```

### install dependencies
```bash
pip install -r requirements.txt
```

### env variables
name of file: .flaskenv

```
PYTHONUNBUFFERED=1
FLASK_DEBUG=1
FLASK_APP=app.py
FLASK_ENV=development
```
