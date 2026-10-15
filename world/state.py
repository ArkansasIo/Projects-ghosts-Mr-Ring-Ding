from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class WorldObject:
    key: str
    name: str
    object_type: str
    x: float
    y: float
    interactive: bool = True
    state: Dict[str, Any] = field(default_factory=dict)


class WorldState:
    def __init__(self):
        self.objects = {
            "door": WorldObject("door", "Studio Door", "door", 760, 250, True, {"open": False}),
            "lamp": WorldObject("lamp", "Desk Lamp", "switch", 520, 330, True, {"on": False}),
            "chest": WorldObject("chest", "Idea Chest", "container", 680, 520, True, {"open": False}),
            "globe": WorldObject("globe", "World Globe", "prop", 930, 320, True, {"spinning": False}),
        }
        self.backdrop = "studio"
        self.character = {"x": 430.0, "y": 500.0, "emotion": "neutral", "gesture": "idle"}

    def describe(self) -> str:
        objects = []
        for obj in self.objects.values():
            objects.append({
                "key": obj.key,
                "name": obj.name,
                "type": obj.object_type,
                "position": {"x": obj.x, "y": obj.y},
                "state": obj.state,
            })
        return str({"backdrop": self.backdrop, "character": self.character, "objects": objects})

    def apply(self, action: str, target: str | None = None) -> bool:
        if action == "none":
            return True
        if action == "walk_to" and target in self.objects:
            obj = self.objects[target]
            self.character["x"] = obj.x - 70
            self.character["y"] = obj.y
            return True
        if action == "look_at" and target in self.objects:
            return True
        if action == "touch" and target in self.objects:
            return True
        if action in {"open", "activate"} and target in self.objects:
            obj = self.objects[target]
            if "open" in obj.state:
                obj.state["open"] = not obj.state["open"]
            elif "on" in obj.state:
                obj.state["on"] = not obj.state["on"]
            elif "spinning" in obj.state:
                obj.state["spinning"] = not obj.state["spinning"]
            return True
        return False
