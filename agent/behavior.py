from dataclasses import dataclass
from typing import Optional

from world.state import WorldState


@dataclass
class BehaviorResult:
    text: str
    emotion: str
    gesture: str
    world_action: str
    target: Optional[str] = None
    applied: bool = False


class BehaviorEngine:
    ALLOWED_EMOTIONS = {"happy", "neutral", "angry", "sad", "surprised", "thinking"}
    ALLOWED_GESTURES = {"idle", "wave", "point", "shrug", "laugh", "think", "jump", "angry", "walk", "interact"}
    ALLOWED_ACTIONS = {"none", "look_at", "walk_to", "touch", "open", "activate"}

    def __init__(self, world: WorldState):
        self.world = world

    def apply(self, result: dict) -> BehaviorResult:
        emotion = result.get("emotion", "neutral")
        gesture = result.get("gesture", "idle")
        action = result.get("world_action", "none")
        target = result.get("target")

        if emotion not in self.ALLOWED_EMOTIONS:
            emotion = "neutral"
        if gesture not in self.ALLOWED_GESTURES:
            gesture = "idle"
        if action not in self.ALLOWED_ACTIONS:
            action = "none"

        if target is None and action in {"walk_to", "look_at", "touch", "open", "activate"}:
            target = self._infer_target(action)

        self.world.character["emotion"] = emotion
        self.world.character["gesture"] = gesture
        applied = self.world.apply(action, target)
        return BehaviorResult(
            text=result.get("text", ""),
            emotion=emotion,
            gesture=gesture,
            world_action=action,
            target=target,
            applied=applied,
        )

    def _infer_target(self, action: str) -> Optional[str]:
        candidates = {
            "open": ["door", "chest"],
            "activate": ["lamp", "globe"],
            "walk_to": ["door", "lamp", "chest", "globe"],
            "look_at": ["globe", "chest", "door", "lamp"],
            "touch": ["lamp", "globe", "chest"],
        }
        for key in candidates.get(action, []):
            if key in self.world.objects:
                return key
        return None
