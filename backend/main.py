from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# NEW imports
from faster_whisper import WhisperModel
from fastapi import File, UploadFile
import tempfile
import os


app = FastAPI(title="SpeakMate")


# Whisper model
whisper_model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Models
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[Message] = []


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "SpeakMate API is running",
        "model": "Gemma 3 4B",
        "mode": "local"
    }


# ==========================================
# NEW: SPEECH → TEXT
# ==========================================

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1] or ".webm"

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await file.read())
        audio_path = temp.name

    try:

        segments, info = whisper_model.transcribe(
            audio_path,
            language="ja",
            beam_size=5
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return {
            "text": text
        }

    finally:

        os.remove(audio_path)


# ==========================================
# EXISTING: CHAT → GEMMA
# ==========================================

@app.post("/chat")
def chat(request: ChatRequest):

    conversation = ""

    for msg in request.history[-10:]:

        if msg.role == "user":
            conversation += f"Learner: {msg.content}\n"

        else:
            conversation += f"SpeakMate: {msg.content}\n"

    prompt = f"""
You are SpeakMate, a private Japanese conversation partner built for a
university student preparing for an upcoming exchange program in Japan.

PURPOSE:
The learner understands some Japanese but does not have anyone to
practice speaking with. Your job is to make them comfortable having
real conversations before their exchange program.

LEARNER PROFILE:
- University student
- Preparing for an exchange program
- Learning Japanese
- Interested in technology, programming, gaming, and music
- Wants practical conversational Japanese

CONVERSATION STYLE:
- Act like a friendly Japanese-speaking friend, not a textbook.
- Use natural but beginner-friendly Japanese.
- Ask exactly ONE follow-up question.
- Prefer situations they may encounter during an exchange program:
  university, introductions, food, shopping, transport, hobbies,
  making friends, asking for help, daily life.
- Occasionally use their interests to make conversations engaging.
- Keep responses concise.
- Encourage them rather than judging mistakes.

CORRECTIONS:
- Only correct meaningful mistakes.
- Do not correct perfectly natural Japanese.
- Explain corrections briefly in English.
- Focus on mistakes that would matter in a real conversation.
- Never overwhelm the learner with multiple corrections.

PREVIOUS CONVERSATION:
{conversation}

CURRENT LEARNER MESSAGE:
{request.message}

Return EXACTLY:

REPLY:
<Japanese conversational response>

CORRECTION:
<one useful correction, or None>

EXPLANATION:
<short English explanation, or None>
"""

Previous conversation:
{conversation}

Current learner message:
{request.message}

Return EXACTLY:

REPLY:
<Japanese conversational response>

CORRECTION:
<one useful correction, or None>

EXPLANATION:
<short English explanation, or None>
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    raw = response.json()["response"]

    reply = ""
    correction = ""
    explanation = ""

    if "REPLY:" in raw:

        reply = raw.split("REPLY:", 1)[1]

        if "CORRECTION:" in reply:
            reply, correction = reply.split(
                "CORRECTION:", 1
            )

        if "EXPLANATION:" in correction:
            correction, explanation = correction.split(
                "EXPLANATION:", 1
            )

    else:
        reply = raw

    return {
        "reply": reply.strip(),
        "correction": correction.strip(),
        "explanation": explanation.strip()
    }