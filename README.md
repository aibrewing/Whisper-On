# ⬡ Whisper On

> **Dictate into any app on Windows — instantly, for free.**\
> Hold `Alt+Q` anywhere on your PC. Speak. Release. Your words appear.

Built on [Groq's](https://groq.com) ultra-fast Whisper API, Whisper On gives you accurate, near-instant voice-to-text that types directly into whatever application you're using — a browser, Word, your IDE, a chat window, anything.

---
If you want to watch the demo on API key creation and how-to use the app, you can find it below:

<a href="https://www.youtube.com/watch?v=oB7g59blfwM">
  <img src="https://img.youtube.com/vi/oB7g59blfwM/hqdefault.jpg" width="140" alt="Watch the demo">
</a>

---

## A note on free vs paid voice-to-text

There are a wide range of voice-to-text apps available nowadays. I've personally been using [Wispr Flow](https://wisprflow.ai), which is genuinely excellent — particularly when it comes to polishing and normalising output. If you don't mind the monthly fee, it's a great piece of software and probably the better choice for most people. I wanted to replicate the convenience of a real-time dictation app well integrated in the flow of your daily routines.

Whisper On is a free alternative. The one difference worth knowing: because the transcript is more literal, you'll want to glance over the text once after dictating to catch anything that needs a quick edit. Far from being a drawback, I'd argue this is actually a good habit to build into your workflow.

When speaking aloud, it's easy to ramble — to add context that isn't needed, or to circle back and repeat yourself. That extra noise has a cost: it can confuse an AI model about what you actually want, and it consumes tokens. The quick review step that Whisper On's literal transcription encourages is, in practice, an opportunity to trim and sharpen your prompt before sending it. Research on the cognitive benefits of reading back what you've written supports this: the act of reviewing a short piece of text engages a different mode of thinking than the act of producing it — one that is more analytical and critical. [See Flower & Hayes (1981) on the revision process in writing, and more recent work on metacognition in AI-assisted writing workflows.]

So the trade-off looks like this: Whisper On gives you the speed and creative freedom of speaking your thoughts aloud, plus the discipline of a brief review pass that helps you think more clearly about what you're asking. You get the best of both worlds — way faster than typing, and more considered than unreviewed dictation.

---

## ✨ Features

- **Global push-to-talk hotkey** (`Alt+Q`) — works even when the app window is not in focus
- **Types directly into any app** — no copy-paste, no switching windows
- **Two recording modes** — hold `Alt+Q` to record (push-to-talk), or press once to start and again to stop
- **Near-instant transcription** — Groq's inference is fast enough to feel real-time
- **Smart formatting** — rule-based: converts symbols, units, currency, fractions, numbered lists (always on)
- **Language support** — 99+ languages transcribed; smart formatting available for English and Italian
- **Auto language detection** — Whisper detects language; formatting rules apply for English and Italian
- **Custom vocabulary** — teach it your names, acronyms and jargon (e.g. AIbrewing, AIOS); biases Whisper's spelling on every recording. Edit anytime via the UI — no rewriting, pure spelling bias
- **Deep clean** *(optional, off by default)* — sends transcript to Groq's Llama 3.3 for punctuation polish and list formatting; uses your existing Groq key. Output is guarded by a word-coverage check so it can never paste back an AI reply instead of your words
- **Hallucination filter** — strips common Whisper closing-phrase artefacts ("Thank you", "Grazie", etc.)
- **Clean web UI** — view history, switch models, manage your API key
- **Persistent history** — every transcript saved locally across sessions
- **Runs silently in the system tray** — launch once, forget about it
- **Free** — Groq's free tier gives you 7,200 seconds of audio per day (~2 hours)
- **Privacy-first** — audio goes directly from your mic to Groq; nothing stored in the cloud

---

## 🆚 Whisper-On vs Wispr-Flow

| Feature | Whisper On | Wispr Flow |
|---|---|---|
| **Price** | ✅ Free (Groq free tier, ~2hrs/day) | ⚠️ Free tier: 2,000 words/week; paid plans for more |
| **Works in any app** | ✅ Yes | ✅ Yes |
| **Transcription model** | ✅ OpenAI Whisper (open source) | ❌ Proprietary model |
| **Open source** | ✅ Fully open source (MIT) | ❌ Closed source |
| **Privacy** | ✅ Audio sent only to Groq | ⚠️ Proprietary cloud backend |
| **Smart text cleanup** | ✅ Rule-based: lists, symbols, units, currency (EN + IT) | ✅ Built-in, automatic |
| **Filler word removal** | ❌ Not available | ✅ Automatic |
| **List formatting** | ✅ Numbered lists (rule-based) - Bullet Lists (LLM-based, not always rendered) | ✅ Automatic |
| **Custom vocabulary** | ✅ Editable term list (biases spelling) | ✅ Personal dictionary |
| **Platform** | ⚠️ Windows only (currently) | ✅ Mac + Windows |

Whisper On handles the most common formatting needs reliably and instantly — numbered lists, symbols, units, currency — without any AI risk.

---

## 🔑 Getting Your Free Groq API Key

Groq provides free access to Whisper and other AI models. No credit card required.

**Step 1 — Create a Groq account**
1. Go to [console.groq.com](https://console.groq.com)
2. Click **Sign Up**
3. Sign up with Google, GitHub, or an email address
4. Verify your email if prompted

**Step 2 — Create an API key**
1. Once logged in, click **API Keys** in the left sidebar
2. Click **Create API Key**
3. Give it a name (e.g. "Whisper On")
4. Copy the key immediately — it is only shown once

**Step 3 — Add it to the app**
1. Open the Whisper On UI at `http://localhost:5000`
2. Paste the key into the **API Key** field
3. Click **Save** — stored locally in `config.json`, never shared

**Free tier limits:** 7,200 seconds of audio per day (~2 hours). Resets every 24 hours.

---

## 🚀 Quick Start

### Option A — Run the .exe (recommended, no Python needed)

1. Download `WhisperOn.exe` from [Releases](../../releases)
2. Double-click to launch — a browser tab opens automatically
3. Paste your Groq API key and click Save
4. Press and hold `Alt+Q` to start dictating into any app

### Option B — Run from source (Python)

For developers who prefer to run the Python script directly.

**1. Install dependencies**
```bash
pip install keyboard pyaudio flask flask-cors requests pystray pillow pynput pyperclip
```

> If `pyaudio` fails on Windows:
> ```bash
> pip install pipwin && pipwin install pyaudio
> ```

**2. Run**
```bash
python transcriber.py
```

The browser opens automatically at `http://localhost:5000`.

---

## 🎯 How It Works

```
Hold Alt+Q → microphone opens
           ↓
      Release Alt+Q → audio sent to Groq Whisper API
                    ↓
         Language detected automatically (EN / IT)
                    ↓
         Rule-based formatting applied
                    ↓
        Text pasted into your focused app
                    ↓
         Entry saved to local history
```

---

## 🤖 Whisper Models

| Model | Speed | Accuracy | Best for |
|---|---|---|---|
| `whisper-large-v3-turbo` | ⚡⚡⚡ | ★★★★ | **Default — best all-round** |
| `whisper-large-v3` | ⚡⚡ | ★★★★★ | Maximum accuracy |
| `distil-whisper-large-v3-en` | ⚡⚡⚡⚡ | ★★★ | English only, fastest |

---

## ⚙️ Requirements

- **OS:** Windows 10 or 11
- **Python:** 3.8+ (Option B only — not needed for .exe)
- **Browser:** Chrome or Edge (for standalone app window)
- **Internet:** Required for Groq API calls

---

## 🔁 Auto-start with Windows (optional)

1. Press `Win+R`, type `shell:startup`, press Enter
2. Create a shortcut to `WhisperOn.exe` (or `transcriber.py`) in that folder
3. Done — it starts silently in the tray every login

---

## 🛑 Closing the App

Always close via the **system tray icon → Quit**.
If a previous instance seems stuck, open Task Manager → Details → kill `WhisperOn.exe` or `python.exe` → relaunch. (The app auto-selects the next free port from 5000 upward, so a busy port no longer blocks startup.)

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `pyaudio` install fails | Use `pipwin install pyaudio` |
| Hotkey not responding | Try running as Administrator |
| "Service not reachable" in UI | Make sure the app is running |
| Network error on transcription | Check internet connection; retry |
| Text not appearing in target app | Click target app first, then use hotkey |
| Numbered lists on same line | Ensure target app accepts Ctrl+V paste |

---

## 🔐 Privacy & Security

- API key stored only in `config.json` on your local machine
- Audio is never stored — sent to Groq, then immediately deleted
- No telemetry — only network call is to `api.groq.com`
- Groq's privacy policy: [groq.com/privacy](https://groq.com/privacy)

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) — speech recognition model
- [Groq](https://groq.com) — ultra-fast inference API
- [keyboard](https://github.com/boppreh/keyboard) — global hotkey library
- [Flask](https://flask.palletsprojects.com) — local web server
- [pystray](https://github.com/moses-palmer/pystray) — system tray integration
- [pyperclip](https://github.com/asweigart/pyperclip) — clipboard management
