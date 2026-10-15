import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
CHARACTER_NAME = os.getenv("CHARACTER_NAME", "Ring-A-Ding")

MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "ringding")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "change-me")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "ringding")
