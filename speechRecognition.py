import speech_recognition as sr

# Créez une instance du recognizer (reconnaissance vocale)
recognizer = sr.Recognizer()

# Spécifiez le chemin vers votre fichier audio (remplacez "audio.wav" par le chemin de votre fichier)
audio_file_path = "C:/Users/mathy/OneDrive - Ynov/Mathys/ynov/Prog/Hackaton/ili toi + moi.wav"

# Ouvrez le fichier audio
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)  # Enregistrez l'audio depuis le fichier

try:
    # Utilisez un moteur de reconnaissance vocale approprié
    text = recognizer.recognize_google(audio_data, language="fr-FR")
    print("Texte transcrit : " , text)
except sr.UnknownValueError:
    print("Impossible de comprendre l'audio.")
except sr.RequestError as e:
    print("Impossible de demander des résultats ; {0}".format(e))
