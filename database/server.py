from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database.mysql import connect, lookup_word

app = FastAPI(title="Mr. Ring-Ding MySQL Server")


class DictionaryEntry(BaseModel):
    word: str
    definition: str
    part_of_speech: str = ""
    example_sentence: str = ""


@app.get("/health")
def health():
    try:
        db = connect()
        db.close()
        return {"status": "ok", "database": "mysql"}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@app.get("/dictionary/{word}")
def dictionary(word: str):
    result = lookup_word(word)
    if result is None:
        return {"found": False, "word": word}
    result["found"] = True
    return result


@app.post("/dictionary")
def add_dictionary(entry: DictionaryEntry):
    db = connect()
    try:
        cur = db.cursor()
        cur.execute(
            "INSERT INTO dictionary(word, definition, part_of_speech, example_sentence) "
            "VALUES (%s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE definition=VALUES(definition), "
            "part_of_speech=VALUES(part_of_speech), example_sentence=VALUES(example_sentence)",
            (entry.word.lower(), entry.definition, entry.part_of_speech, entry.example_sentence),
        )
        return {"saved": entry.word.lower()}
    finally:
        db.close()
