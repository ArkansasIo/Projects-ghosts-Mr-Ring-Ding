# Projects Ghosts — Mr. Ring-Ding

A local-first, interactive 2D cartoon AI character project.

## What this project contains

- Original blue cartoon character inspired by theatrical/rubber-hose animation.
- AI conversation agent with a local Ollama-compatible model interface.
- MySQL database server for conversation memory, dictionary entries, generated text, character identities, quotes, and world state.
- English dictionary support for generating sentences and paragraphs.
- Character emotions and gesture directives that can drive animation.
- A world/backdrop state model so the character can react to and interact with its environment.
- Text-to-speech integration point for spoken dialogue.

## Local AI

The default design uses Ollama as a local model server. No paid AI API is required.

Example:

```bash
ollama pull llama3.2
```

## MySQL

Create a MySQL database named `ringding` and set the connection environment variables:

```text
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=ringding
MYSQL_PASSWORD=change-me
MYSQL_DATABASE=ringding
```

Then apply `database/schema.sql`.

## Install

```bash
python -m pip install -r requirements.txt
```

Run the database/API service:

```bash
python -m uvicorn database.server:app --reload --port 8000
```

Run the character agent:

```bash
python main.py
```

## Important note

The character, dialogue, identities, and artwork in this repository are original project material. They are not intended to reproduce Doctor Who footage, audio, scripts, or copyrighted production artwork.
