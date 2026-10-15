import unittest


ALLOWED_EMOTIONS = {"happy", "neutral", "angry", "sad", "surprised", "thinking"}
ALLOWED_GESTURES = {"idle", "wave", "point", "shrug", "laugh", "think", "jump", "angry", "walk", "interact"}
ALLOWED_WORLD_ACTIONS = {"none", "look_at", "walk_to", "touch", "open", "activate"}


class WorldDirectiveTests(unittest.TestCase):
    def test_valid_directive(self):
        directive = {
            "emotion": "surprised",
            "gesture": "jump",
            "world_action": "activate",
        }
        self.assertIn(directive["emotion"], ALLOWED_EMOTIONS)
        self.assertIn(directive["gesture"], ALLOWED_GESTURES)
        self.assertIn(directive["world_action"], ALLOWED_WORLD_ACTIONS)

    def test_invalid_directive_is_rejected_by_contract(self):
        directive = {
            "emotion": "telepathic",
            "gesture": "fly",
            "world_action": "rewrite_reality",
        }
        self.assertNotIn(directive["emotion"], ALLOWED_EMOTIONS)
        self.assertNotIn(directive["gesture"], ALLOWED_GESTURES)
        self.assertNotIn(directive["world_action"], ALLOWED_WORLD_ACTIONS)


if __name__ == "__main__":
    unittest.main()
