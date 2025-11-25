import sounddevice as sd
import numpy as np
import librosa
from config import MFCC_N_MFCC

DURATION = 5  
FS = 16000    

def record_voice():
    print("\n🎤 Recording... Speak now.")
    audio = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, dtype=np.float32)
    sd.wait()
    audio = audio.flatten()

    print("✔ Recording complete\n")
    return audio, FS

def extract_mfcc(audio, sr):
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)
    averaged = np.mean(mfcc, axis=1)  
    return averaged

def verify_voice():
    print("\n🎤 Say again: 'open my vault'")
    audio, sr = record_voice()
    test_vec = extract_mfcc(audio, sr)

    if not os.path.exists(VOICEPRINT_FILE):
        print("❌ No saved voiceprint found. Register first.")
        return False

    saved_vec = np.load(VOICEPRINT_FILE)

    dot = np.dot(saved_vec, test_vec)
    normA = np.linalg.norm(saved_vec)
    normB = np.linalg.norm(test_vec)

    similarity = dot / (normA * normB)

    print(f"🔎 Similarity Score: {similarity:.3f}")

    return similarity >= 0.97
