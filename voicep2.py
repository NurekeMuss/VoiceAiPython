import pyttsx3

engine = pyttsx3.init()

# Set properties
engine.setProperty('rate', 150)  # Скорость
engine.setProperty('volume', 0.9)  # Громкость

# Voice IDs
voice_id_russian = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
voice_id_english = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Set and use the Russian voice
engine.setProperty('voice', voice_id_russian)
engine.say('Привет всем еще раз!')

# Set and use the English voice
engine.setProperty('voice', voice_id_english)
engine.say("Hello everyone again!")

engine.runAndWait()
