import re
import json

with open('Jain_Cricket_Quiz_Complete.md', 'r', encoding='utf-8') as f:
    text = f.read()

topic_matches = list(re.finditer(r'\*\*विषय\s*(\d+)\s*:\s*([^*]+)\*\*', text))

print(f"Found {len(topic_matches)} topics")

topics = []
for idx, match in enumerate(topic_matches):
    num = int(match.group(1))
    title = match.group(2).strip()
    
    start_pos = match.end()
    end_pos = topic_matches[idx + 1].start() if idx + 1 < len(topic_matches) else len(text)
    block_text = text[start_pos:end_pos].strip()
    
    lines = [l.strip() for l in block_text.split('\n') if l.strip()]
    questions = []
    curr_q = None
    
    for l in lines:
        if l.startswith('#') or l.startswith('---'):
            continue
        m_run = re.match(r'^(\d+)\s*रन\s*:\s*(.*)', l)
        if m_run:
            if curr_q:
                questions.append(curr_q)
            curr_q = {
                'runs': int(m_run.group(1)),
                'question': m_run.group(2).strip(),
                'answer': ''
            }
        elif curr_q:
            if 'उत्तर' in l or 'Ans' in l:
                ans = re.sub(r'^\(?(?:उत्तर|Ans)\s*:\s*', '', l, flags=re.IGNORECASE)
                ans = re.sub(r'\)?$', '', ans).strip()
                curr_q['answer'] = ans
            else:
                if not curr_q['answer']:
                    curr_q['question'] += ' ' + l
                else:
                    curr_q['answer'] += ' ' + l
    if curr_q:
        questions.append(curr_q)
    
    topics.append({
        'number': num,
        'title': title,
        'questions': questions
    })

print(f"Parsed {len(topics)} topics successfully.")
for t in topics:
    runs = [q['runs'] for q in t['questions']]
    if len(t['questions']) != 3 or any(not q['answer'] for q in t['questions']):
        print(f"WARNING on Topic {t['number']} ({t['title']}): {len(t['questions'])} questions, runs={runs}")

with open('quiz_data.json', 'w', encoding='utf-8') as out:
    json.dump(topics, out, ensure_ascii=False, indent=2)

print("Saved to quiz_data.json")
