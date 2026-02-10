# JARV-X 🤖🎙️

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/AI-Offline-success" />
  <img src="https://img.shields.io/badge/LLM-Ollama-black" />
  <img src="https://img.shields.io/badge/Platform-Windows-informational" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

JARV-X is a fully offline, voice-controlled AI assistant built with Python.  
It uses speech recognition, text-to-speech, and local LLMs via Ollama to deliver fast, private, and internet-free AI interactions.

Designed for students, developers, and hackers who want a Jarvis-style assistant running entirely on their own machine.

---

## ✨ Features

- 🎤 Voice input using your laptop’s default microphone  
- 🗣️ Natural text-to-speech responses  
- 🧠 Runs **100% offline** using Ollama (no API, no billing)  
- 🔐 Privacy-first (your data never leaves your system)  
- ⚡ Fast responses with local LLMs  
- 🖥️ Works on Windows (Mac/Linux adaptable)

---

## 🧰 Tech Stack

- **Python 3.10+**
- **SpeechRecognition** – Speech to text  
- **PyAudio** – Microphone access  
- **pyttsx3** – Text to speech  
- **Ollama** – Local LLM runtime  
- **Qwen / LLaMA / Mistral models** (your choice)

---

## 📦 Requirements

- Python installed  
- Ollama installed and running  
- A working microphone  

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/JARV-X.git
cd JARV-X
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Install Ollama
- Download and install from:
- 👉 https://ollama.com
- Restart your system once after installation.
### 5️⃣ Pull a Model
```bash
ollama pull qwen2.5-coder:7b
(You can use any Ollama-supported model.)
```
### ▶️ Run JARV-X
---
### 🧪 Troubleshooting

#### 🎙️ Mic not working?
- Check Windows microphone permissions
- Set correct default input device
#### 🤖 Ollama not responding?
- Run `ollama list`
- Ensure Ollama service is running
#### 🔁 Model error
- Make sure model name matches exactly
---
## 📁 Project Structure
```bash
JARV-X/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
```
---
## Future Scope
- Wake-word detection (“Hey Jarvis”)
- GUI dashboard
- App control & automation
- Multi-language support
- Packaging into `.exe`
---
### 🧠 Inspiration

Inspired by Jarvis (Iron Man), built for real-world use by students who want to learn AI systems hands-on — without paying for APIs.

### 📜 License

MIT License — free to use, modify, and distribute.

### ⭐ Support

If you like this project:

### Star ⭐ the repo

### Fork 🍴 it
-Build your own JARV-X
-Let’s make local AI powerful.

---
