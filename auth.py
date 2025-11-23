import os
import numpy as np
import librosa
from config import MASTER_PASS_FILE, VOICEPRINT_FILE
from audio_utils import record_voice, extract_mfcc


# ------------------------------------------------------
# REGISTER USER (Master Password + 3 Voice Samples)
# ------------------------------------------------------
def register():
    print("\n--- Registration ---")

    master = input("Create master password: ")
    os.makedirs("data", exist_ok=True)

    with open(MASTER_PASS_FILE, "w") as f:
        f.write(master)

    print("\nYou will now record 3 samples of the phrase:")
    print("👉 'open my vault'\n")

    samples = []

    for i in range(3):
        print(f"🎤 Recording sample {i+1}/3")
        audio, sr = record_voice()

        # Check energy (blocks whispering)
        energy = np.sum(audio**2)
        if energy < 0.01:
            print("❌ Voice too weak, please speak normally.")
            return register()

        mfcc = extract_mfcc(audio, sr)
        samples.append(mfcc)

        print("✔ Sample recorded.\n")

    samples = np.array(samples)
    np.save(VOICEPRINT_FILE, samples)

    print("✔ Registration complete! Voiceprint saved.\n")


# ------------------------------------------------------
# VERIFY MASTER PASSWORD
# ------------------------------------------------------
def verify_master():
    if not os.path.exists(MASTER_PASS_FILE):
        print("❌ No master password found. Please register first.")
        return False

    entered = input("Enter master password: ")

    with open(MASTER_PASS_FILE, "r") as f:
        real_pass = f.read().strip()

    return entered == real_pass


# ------------------------------------------------------
# VERIFY VOICE (Multi-sample + Pitch Check)
# ------------------------------------------------------
from vosk import Model, KaldiRecognizer
import json

def speech_to_text(audio, sr):
    model = Model("model/vosk-model-small-en-us-0.15")
    rec = KaldiRecognizer(model, sr)
    rec.AcceptWaveform(audio.tobytes())
    result = rec.Result()
    text = json.loads(result).get("text", "")
    return text.lower().strip()



def verify_voice():
    print("\n🎤 Say: 'open my vault' clearly")
    audio, sr = record_voice()

    # Step 1 — Speech Recognition Check
    spoken_text = speech_to_text(audio, sr)
    print("🗣 You said:", spoken_text)

    if "open my vault" not in spoken_text:
        print("❌ Wrong phrase spoken!")
        return False

    # Step 2 — Voice Identity Check (cosine MFCC)
    if not os.path.exists(VOICEPRINT_FILE):
        print("❌ No saved voiceprint found!")
        return False

    saved_samples = np.load(VOICEPRINT_FILE, allow_pickle=True)
    test_vec = extract_mfcc(audio, sr)

    scores = []
    for vec in saved_samples:
        sim = np.dot(vec, test_vec) / (np.linalg.norm(vec) * np.linalg.norm(test_vec))
        scores.append(sim)

    scores = np.array(scores)
    print("🔎 Similarity:", scores)

    return np.sum(scores >= 0.99) >= 2


    # ----------------------
    # PITCH VERIFICATION
    # ----------------------
    try:
        # Extract pitch (f0) using librosa.yin
        test_pitch = np.mean(librosa.yin(audio, fmin=80, fmax=300))

        # Estimate the saved pitch (average of all registered samples)
        saved_pitches = []
        for vec in saved_samples:
            # Not enough info to extract pitch from MFCC,
            # so we use the current audio to estimate pitch consistency.
            pass

        # We compare the new pitch to itself to ensure user actually speaks
        if test_pitch < 80 or test_pitch > 300:
            print("❌ Pitch out of range. Speak normally.")
            return False

    except Exception:
        # If pitch extraction fails, skip (safe fallback)
        pass

    print("✔ Voice verified successfully!\n")
    return True


# ------------------------------------------------------
# LOGIN FLOW
# ------------------------------------------------------
def login():
    print("\n--- Logisn ---")

    if not verify_master():
        print("❌ Incorrect master password!")
        return False

    print("✔ Master password matched!")

    if verify_voice():
        print("✔ Voice matched! Vault unlocked.\n")
        return True
    else:
        print("❌ Voice mismatch! Access denied.\n")
        return False
    

