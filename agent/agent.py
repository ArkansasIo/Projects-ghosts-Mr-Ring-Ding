import json
import uuid
import requests

from config import OLLAMA_URL, OLLAMA_MODEL, CHARACTER_NAME
from agent.personality import SYSTEM_PROMPT
from database.mysql import add_memory, recent_memory


class CartoonAgent:
    def __init__(self, session_id=None):
        self.name = CHARACTER_NAME
        self.session_id = session_id or str(uuid.uuid4())

    def chat(self, user_text, world_context=""):
        add_memory(self.session_id, "user", user_text)
        history = recent_memory(self.session_id)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        if world_context:
            messages.append({
                "role": "system",
                "content": f"Current animated-world state:\n{world_context}",
            })

        for role, content in history:
            messages.append({"role": role, "content": content})

        payload = {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
            "format": "json",
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        data = json.loads(response.json()["message"]["content"])

        add_memory(self.session_id, "assistant", data["text"])
        return data
