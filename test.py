from langdetect import detect
relative_path = "A_dim_2_0.wav"
relative_path = "AVM.wav"
relative_path = "5_-4_-3_-2_-1.wav"
def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return str(e)

# Exemple d'utilisation :
text_to_analyze = "Salut"
detected_language = detect_language(text_to_analyze)
print(f"La langue détectée est : {detected_language}")