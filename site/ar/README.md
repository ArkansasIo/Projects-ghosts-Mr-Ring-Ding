# Ring-A-Ding Augmented Reality

This folder adds an experimental browser AR layer for the original Ring-A-Ding character.

## Modes

1. **WebXR immersive AR** — requests an `immersive-ar` session when the browser/device supports it.
2. **Camera demo** — uses the device camera as a background and overlays the 2D Ring-A-Ding character.
3. **Behavior controls** — wave, happy, think, dream, and follow animations demonstrate how the existing AI behavior directives can drive the AR character.

## Architecture

```text
AI / Ollama
    |
    v
CharacterAgent
    |
    v
Behavior Directive
    |-- emotion
    |-- gesture
    |-- world_action
    |-- target
    v
AR Controller
    |
    +--> 2D character overlay
    +--> WebXR session
    +--> camera demo
    +--> future 3D/world renderer
```

## Important deployment note

GitHub Pages can host this browser client, but it cannot host the Python AI service, Ollama model server, or MySQL database. Those services must remain on a local computer or separate HTTPS server.

Camera and immersive-AR access also require browser permission and appropriate secure-context/device support.

## Future integration

The next AR stage should replace the simple CSS character with the project's animation renderer and connect AR hit-test/plane information to `world_action` targets. Voice output can then synchronize with facial animation and spatial movement.
