# Ring-A-Ding Test Suite

The tests are designed to catch regressions in the character's AI contract, MySQL persistence boundary, and animation/world directives.

## Run

From the repository root:

```bash
python -m unittest discover -s tests -v
```

## What is tested

- `test_character_agent.py`: mocks Ollama and verifies that a conversation returns text plus valid emotion, gesture, and world-action directives.
- `test_character_contract.py`: verifies that the character system prompt contains the supported behavior contract.
- `test_mysql.py`: verifies the MySQL persistence functions without requiring a live database connection.
- `test_world_contract.py`: checks valid directives and confirms unsupported directives are rejected by the contract.

These are deterministic unit tests; the live Ollama and MySQL services can be tested separately as integration tests.
