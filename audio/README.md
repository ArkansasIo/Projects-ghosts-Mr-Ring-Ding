# Ring-A-Ding Voice

Ring-A-Ding's voice is designed as an original theatrical cartoon voice: bright, playful, expressive, and slightly bell-like.

## Local test

Install the project's Python dependencies and run:

```bash
python -m audio.tts
```

The adapter uses `pyttsx3`, so it can use a locally installed operating-system TTS voice without requiring a paid cloud service.

## Voice behavior

Emotion changes the delivery profile:

- `happy`: brighter and faster
- `neutral`: conversational
- `thinking`: slower and calmer
- `surprised`: higher and faster
- `sad`: lower and slower
- `angry`: faster and more forceful

The `voice_profile.json` file keeps these settings separate from the TTS engine so a future local neural TTS backend can use the same character voice design.
