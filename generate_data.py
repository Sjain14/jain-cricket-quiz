import re
import json

with open('Jain_Cricket_Quiz_Complete.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Split or scan lines
lines = text.split('\n')

topics = []
current_sprint = "सामान्य"
topic_matches = list(re.finditer(r'\*\*विषय\s*(\d+)\s*:\s*([^*]+)\*\*', text))

# We can also detect which sprint each topic belongs to
sprint_matches = list(re.finditer(r'#\s*(Sprint\s*\d+:[^\n]+)', text))

def get_sprint_for_pos(pos):
    current = ""
    for sm in sprint_matches:
        if sm.start() < pos:
            current = sm.group(1).strip()
    return current

for idx, match in enumerate(topic_matches):
    num = int(match.group(1))
    title = match.group(2).strip()
    sprint = get_sprint_for_pos(match.start())
    
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
        'sprint': sprint,
        'questions': questions
    })

print(f"Total topics: {len(topics)}")
with open('quiz_data.json', 'w', encoding='utf-8') as out:
    json.dump(topics, out, ensure_ascii=False, indent=2)

with open('quiz_data.js', 'w', encoding='utf-8') as out:
    out.write("const QUIZ_DATA = " + json.dumps(topics, ensure_ascii=False, indent=2) + ";\n")

print("Generated quiz_data.json and quiz_data.js successfully.")
