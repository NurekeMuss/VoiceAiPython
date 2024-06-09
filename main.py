from gtts import gTTS

import os

message = "check this message"

language = 'ru'

record = gTTS(text=message, lang=language, slow=False)

record.save("first.mp3")
os.system("first.mp3")