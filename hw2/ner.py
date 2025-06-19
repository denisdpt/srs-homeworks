import spacy
import re

nlp = spacy.load("ru_core_news_md")

ALLOWED_LABELS = {"PER", "ORG", "LOC"}

NOISE_RE = re.compile(r'^[\W_]+$')

def extract_entities(text: str) -> list[tuple[str, str]]:
    #Выделяем именованные сущности (PER, ORG, LOC), отбрасываем шум (например, '→' и тд)
    doc = nlp(text)
    ents = []
    for ent in doc.ents:
        label = ent.label_
        text_ = ent.text.strip()
        if (
            label in ALLOWED_LABELS
            and not NOISE_RE.match(text_)
            and "→" not in text_
        ):
            ents.append((text_, label))
    return ents
