import unittest

from agent.personality import SYSTEM_PROMPT


class CharacterContractTests(unittest.TestCase):
    def test_system_prompt_defines_json_contract(self):
        required_fields = ["text", "emotion", "gesture", "world_action"]
        for field in required_fields:
            self.assertIn(field, SYSTEM_PROMPT)

    def test_prompt_defines_supported_animation_states(self):
        for value in ["happy", "neutral", "angry", "sad", "surprised", "thinking"]:
            self.assertIn(value, SYSTEM_PROMPT)
        for value in ["idle", "wave", "point", "shrug", "laugh", "think", "jump", "angry", "walk", "interact"]:
            self.assertIn(value, SYSTEM_PROMPT)
        for value in ["none", "look_at", "walk_to", "touch", "open", "activate"]:
            self.assertIn(value, SYSTEM_PROMPT)


if __name__ == "__main__":
    unittest.main()
