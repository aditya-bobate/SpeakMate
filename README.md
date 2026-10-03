# 🗣️ SpeakMate

### A private Japanese conversation partner that runs locally.

SpeakMate is a local AI-powered Japanese conversation partner I built for my friend, who is preparing for an upcoming exchange program in Japan.

He needed a simple way to practice speaking Japanese, but didn't always have someone available to practice with.

So I built him one.

---

## 🎯 The Problem

Learning a language isn't just about memorizing vocabulary.

You need to actually **talk**.

My friend is learning Japanese for an upcoming exchange program, but finding someone to practice Japanese conversations with isn't always easy.

I wanted to build something that he could simply open, speak Japanese to, and immediately continue a natural conversation.

At the same time, I didn't want every conversation to be sent to a remote AI service.

That led to SpeakMate.

---

## 💡 What is SpeakMate?

SpeakMate is a **private Japanese conversation partner powered by open-source AI**.

It can:

- 🎙️ Listen to spoken Japanese
- 📝 Convert speech to text using local Whisper
- 🤖 Continue the conversation using Gemma 3 4B
- ✏️ Correct meaningful Japanese mistakes
- 💬 Explain corrections briefly in English
- 🔊 Speak responses back using browser text-to-speech
- 🧠 Maintain conversation context

The goal is simple:

> **Open it → Speak Japanese → Keep talking.**

---

## 🤖 Why Open-Source AI?

The most important part of SpeakMate is that the AI runs locally.

The conversation uses:

**Gemma 3 4B → Ollama → Local machine**

Speech recognition uses:

**Whisper → Local machine**

This provides several advantages:

### 🔒 Privacy

Language practice can contain personal conversations.

With local inference, those conversations don't need to be sent to a third-party AI API.

### 💰 No per-message API cost

The core AI runs on the user's own machine.

### 🌐 Local-first

The application doesn't depend on a hosted AI API for every conversation.

### 🔄 Model flexibility

Because the application communicates with Ollama, the underlying model can be changed without redesigning the entire application.

---

## 🏗️ How It Works

```text
                 ┌─────────────────────┐
                 │      Browser        │
                 │  SpeakMate UI       │
                 └──────────┬──────────┘
                            │
                     Voice / Text
                            │
                            ▼
                 ┌─────────────────────┐
                 │    FastAPI Backend  │
                 └───────┬─────┬───────┘
                         │     │
              Speech     │     │  Conversation
                         ▼     ▼
                 ┌──────────┐ ┌──────────────┐
                 │ Whisper  │ │ Ollama       │
                 │  Local   │ │              │
                 └──────────┘ │ Gemma 3 4B   │
                              └──────┬───────┘
                                     │
                                     ▼
                              Japanese Reply
                                     │
                                     ▼
                              Browser TTS


🛠️ Tech Stack
Component	Technology
AI Model	Gemma 3 4B
Model Runtime	Ollama
Speech Recognition	faster-whisper
Backend	Python + FastAPI
Frontend	HTML + CSS + JavaScript
Text-to-Speech	Browser Speech Synthesis API


🧠 AI Conversation Design
SpeakMate isn't designed to behave like a textbook.
The model is instructed to:
- Act like a friendly Japanese-speaking friend
- Use natural but beginner-friendly Japanese
- Ask one follow-up question
- Focus on practical situations
- Correct only meaningful mistakes
- Explain corrections briefly
- Encourage the learner instead of overwhelming them
Example:
Learner:
今日は大学に行きました。

SpeakMate:
それはいいですね！
どんなことを勉強しましたか？

The conversation can then continue naturally.
🎙️ Voice Interaction
SpeakMate supports microphone input using the browser's MediaRecorder.
The recorded audio is sent to the local FastAPI server:
Microphone
     ↓
MediaRecorder
     ↓
FastAPI /transcribe
     ↓
faster-whisper
     ↓
Japanese text
     ↓
Gemma 3 4B
     ↓
Japanese response
     ↓
Browser TTS

Everything in the AI pipeline is designed to run locally.
👨‍💻 Built for a Real Person
This wasn't built as a generic AI chatbot.
I built it specifically for my friend.
After using the working version, his feedback was:
"I loved it. It was easy to use."

That was especially important to me.
The goal wasn't to create another complicated AI interface.
It was to create something my friend could open and immediately start using.
🚀 Running SpeakMate Locally
1. Install Ollama
Install Ollama from:
https://ollama.com/
Then download Gemma:
ollama run gemma3:4b

2. Install Python dependencies
pip install fastapi uvicorn requests faster-whisper python-multipart

3. Start the backend
From the project directory:
uvicorn main:app --reload

The API will run at:
http://127.0.0.1:8000

4. Start the frontend
You can serve index.html using a simple local server:
python -m http.server 5500

Then open:
http://127.0.0.1:5500

📁 Project Structure
SpeakMate/
│
├── main.py
├── index.html
├── README.md
└── .gitignore

🔐 Privacy
SpeakMate was designed around a local-first architecture.
The core AI processing happens on the user's machine:
- Gemma → local
- Ollama → local
- Whisper → local
- Conversation processing → local FastAPI server
The project does not require a cloud AI API key.
🌱 What I'd Build Next
If I continue developing SpeakMate, I'd like to add:
- 🎭 Conversation scenarios
  - University
  - Restaurant
  - Train station
  - Shopping
  - Making friends
- 📈 Japanese learning progress tracking
- 🗣️ Better pronunciation feedback
- 🧠 Vocabulary memory
- 📱 Mobile-friendly interface
- ⚡ Faster speech recognition models
- 🔌 Support for swapping between different local models
❤️ Why I Built This
Technology is most useful when it solves a problem for a real person.
My friend didn't need another AI demo.
He needed someone to practice Japanese with.
So I built him one.
📜 License
MIT License
🔗 Links
GitHub:
https://github.com/aditya-bobate/SpeakMate
Built with ❤️, Python, Gemma, Whisper, and a lot of Japanese practice.

### Then push it

After replacing `README.md`, from `E:\speakmate` run:

```cmd
git add README.md && git commit -m "Improve project README" && git push
