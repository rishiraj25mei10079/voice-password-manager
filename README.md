# Voice-Protected Password Manager
### Python-based local password vault secured with offline voice authentication

This project implements a two-factor authentication system combining a master password with a voice-based biometric check.
All processing is done locally using Python libraries, ensuring full privacy and security.

## Features

### 1. Dual Authentication
- Master password
- Voice verification using MFCC features and cosine similarity

### 2. Offline Speech Recognition
Uses the Vosk speech-to-text engine to verify that the user speaks the correct phrase (“open my vault”).

### 3. Voiceprint Biometrics
- Captures three enrollment samples
- Extracts MFCC vectors
- Requires at least two matches
- Includes energy and pitch checks

### 4. Local Password Vault
Encrypted vault file storing website, username, and password.
Fully offline.

## Project Structure

```
voice_password_manager/
│ main.py
│ auth.py
│ vault.py
│ audio_utils.py
│ db.py
│ config.py
│
├── data/
│     ├── master.pass
│     └── voiceprint.npy
│
└── model/
      └── vosk-model-small-en-us-0.15/
```

## Installation

### 1. Install Python Packages

```
pip install sounddevice
pip install vosk
pip install librosa
pip install numpy
pip install scipy
```

### 2. Download the Vosk Model

Download:  
https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

Extract to:

```
voice_password_manager/model/
```

## Usage

### Registration

```
python main.py
```

### Login

```
python main.py
```

## Technology Stack

| Functionality | Library |
|---------------|---------|
| Voice recording | sounddevice |
| Speech recognition | Vosk |
| Feature extraction | Librosa |
| Similarity metric | Cosine similarity |
| Data storage | JSON + NumPy |

## Author
Rishiraj Singh
