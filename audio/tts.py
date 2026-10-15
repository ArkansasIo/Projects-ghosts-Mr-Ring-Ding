"""Local text-to-speech adapter for Ring-A-Ding.

Uses pyttsx3 so the default implementation can run without a paid cloud API.
The selected system voice is intentionally treated as a configurable TTS voice;
the project does not attempt to clone a real person's voice.
"""

import json
from pathlib import Path

import pyttsx3


PROFILE_PATH = Path(__file__).with_name("voice_profile.json")


def load_profile():
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def speak(text: str, emotion: str = "neutral") -> None:
    profile = load_profile()
    engine = pyttsx3.init()

    engine.setProperty("volume", profile.get("volume", 1.0))
    engine.setProperty("rate", 180 * profile.get("rate", 1.0))

    emotion_profile = profile.get("preferred_emotion_profiles", {}).get(emotion, {})
    if "rate" in emotion_profile:
        engine.setProperty("rate", 180 * emotion_profile["rate"])

    # pyttsx3 does not expose a portable pitch control. Pitch remains part of
    # the project profile so richer TTS backends can use the same interface.
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    profile = load_profile()
    speak(profile["sample_line"], "happy")
