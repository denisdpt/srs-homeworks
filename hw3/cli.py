import json
import os

def load_roadmap(path="roadmap.json"):
    base = os.path.dirname(__file__)
    with open(os.path.join(base, path), encoding="utf-8") as f:
        return json.load(f)

def print_topic(topic):
    print(f"\n[{topic['id']}] {topic['title']}")
    print(f"  Описание: {topic['description']}")
    print(f"  Ключевые слова: {', '.join(topic['keywords'])}")
    for i, sub in enumerate(topic["subtopics"], 1):
        print(f"    {i}. {sub['title']} — {', '.join(sub['keywords'])}")
    print()

def main():
    data = load_roadmap()
    print(f"\n=== Роадмап: {data['domain']} ===")
    print(data["overview"], "\n")

    while True:
        print("Темы:")
        for t in data["topics"]:
            print(f"  {t['id']}. {t['title']}")
        choice = input("Выберите номер темы (q — выход): ").strip()
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            continue
        tid = int(choice)
        topic = next((t for t in data["topics"] if t["id"] == tid), None)
        if topic:
            print_topic(topic)

if __name__ == "__main__":
    main()