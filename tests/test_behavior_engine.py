import unittest

from agent.behavior import BehaviorEngine
from world.state import WorldState


class BehaviorEngineTests(unittest.TestCase):
    def setUp(self):
        self.world = WorldState()
        self.engine = BehaviorEngine(self.world)

    def test_walk_to_door(self):
        result = self.engine.apply({
            "text": "Let's see what's behind the door!",
            "emotion": "curious",
            "gesture": "walk",
            "world_action": "walk_to",
            "target": "door",
        })
        self.assertEqual(result.emotion, "neutral")
        self.assertEqual(result.target, "door")
        self.assertTrue(result.applied)
        self.assertEqual(self.world.character["x"], 690)

    def test_activate_lamp(self):
        result = self.engine.apply({
            "text": "Let there be light!",
            "emotion": "happy",
            "gesture": "interact",
            "world_action": "activate",
            "target": "lamp",
        })
        self.assertTrue(result.applied)
        self.assertTrue(self.world.objects["lamp"].state["on"])

    def test_invalid_directives_are_safe(self):
        result = self.engine.apply({
            "text": "",
            "emotion": "telepathic",
            "gesture": "fly",
            "world_action": "rewrite_reality",
        })
        self.assertEqual(result.emotion, "neutral")
        self.assertEqual(result.gesture, "idle")
        self.assertEqual(result.world_action, "none")
        self.assertTrue(result.applied)


if __name__ == "__main__":
    unittest.main()
