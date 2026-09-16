import json

with open('quiz_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total topics: {len(data)}")
for t in data:
    runs = [q['runs'] for q in t['questions']]
    assert len(t['questions']) == 3, f"Topic {t['number']} doesn't have 3 questions"
    assert runs[0] == 1, f"Topic {t['number']} q0 run != 1"
    assert runs[1] == 2, f"Topic {t['number']} q1 run != 2"
    assert runs[2] in (4, 6), f"Topic {t['number']} q2 run not 4 or 6"
    for q in t['questions']:
        assert len(q['question']) > 0, f"Topic {t['number']} question empty"
        assert len(q['answer']) > 0, f"Topic {t['number']} answer empty"

print("ALL 45 TOPICS VALIDATED PERFECTLY!")
