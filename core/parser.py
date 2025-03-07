import re


def parse_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            return re.findall(r'\w+', text.lower())
    except Exception:
        return []
