# Problem Statement



Storing passwords in plain text or relying solely on a master password poses significant security risks. Traditional password managers can be vulnerable if the master password is compromised. This project aims to enhance authentication security by integrating **local voice biometrics** with a master password, creating a dual-layer protection mechanism. The system ensures that even if someone knows the master password, they cannot access the vault without matching the registered voice.



# Scope of the Project



* Implement a **local password vault** using Python.
* Enable users to store, retrieve, and manage login credentials securely.
* Integrate **voice-based authentication** using MFCC feature extraction and cosine similarity.
* Use **offline speech recognition** to validate the spoken phrase (“open my vault”).
* Provide a fully offline solution without requiring any cloud APIs.
* Ensure compatibility with standard computer hardware (microphone, CPU).
* Deliver a simple CLI-based interface suitable for academic and practical use.



# Target Users



* Individuals who want enhanced security for local password storage.
* Students learning about biometrics, signal processing, and authentication systems.
* Users seeking offline password management without relying on cloud-based services.
* Developers exploring Python-based audio processing and security techniques.
* Academia/institutions requiring demonstrable projects integrating multiple Python libraries.



# High-Level Features



* **Dual Authentication System**

  * Master password verification.
  * Voice authentication using MFCC + cosine similarity.

* **Offline Speech Recognition**

  * Vosk model validates the spoken phrase.

* **Biometric Voiceprint System**

  * Three-sample enrollment for accurate voice pattern storage.
  * Similarity threshold ensures secure access.

* **Secure Local Vault**

  * Store website URLs, usernames, and passwords.
  * Data saved in encrypted or structured formats locally.

* **Audio Safety Filters**

  * Low-volume/whisper detection.
  * Basic pitch validation.

* **Fully Offline Architecture**

  * No data sent outside the user’s device.
