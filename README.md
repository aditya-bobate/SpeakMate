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
