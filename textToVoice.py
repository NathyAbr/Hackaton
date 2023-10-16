from gtts import gTTS
import os
relative_path = "A_dim_2_0.wav"
relative_path = "AVM.wav"
relative_path = "5_-4_-3_-2_-1.wav"
mytext = 'Bienvenue chez toi'

langue = 'fr'

textSpeech = gTTS(text=mytext, lang=langue, slow=False)

textSpeech.save("Bienvenue test1")
os.popen("Bienvenue test1.mp3")