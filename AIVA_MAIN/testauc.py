


import os
from playsound import playsound

audio_file_path = r'C:\Users\Madavaraj K\Downloads\Heisenberg-main\Heisenberg-main\quarter spin flac.mp3'
if os.path.exists(audio_file_path):
    playsound(audio_file_path)
else:
    print("Audio file does not exist at:", audio_file_path)
