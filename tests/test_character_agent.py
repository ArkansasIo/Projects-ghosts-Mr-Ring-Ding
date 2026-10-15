import json
import unittest
from unittest.mock import patch

from agent.agent import CartoonAgent


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "message": {
                "content": json.dumps({
                    "text": "Ring-a-ding! Test successful.",
                    "emotion": "happy",
                    "gesture": "wave",
                    "world_action": "look_at",
                })
            }
        }


class CharacterAgentTests(unittest.TestCase):
    @patch("agent.agent.add_memory")
    @patch("agent.agent.recent_memory", return_value=[])
    @patch("agent.agent.requests.post", return_value=FakeResponse())
    def test_chat_returns_animation_directives(self, mock_post, mock_history, mock_memory):
        agent = CartoonAgent(session_id="test-session")
        result = agent.chat("Hello Ring-a-Ding", "A blue cartoon studio.")

        self.assertEqual(result["text"], "Ring-a-ding! Test successful.")
        self.assertIn(result["emotion"], {"happy", "neutral", "angry", "sad", "surprised", "thinking"})
        self.assertIn(result["gesture"], {"idle", "wave", "point", "shrug", "laugh", "think", "jump", "angry", "walk", "interact"})
        self.assertIn(result["world_action"], {"none", "look_at", "walk_to", "touch", "open", "activate"})
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
