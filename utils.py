from typing import List

def preprocess_feedback(feedback: List[str]) -> List[str]:
    seen = set()
    cleaned = []
    for f in feedback:
        f_clean = f.strip()
        if f_clean and f_clean not in seen:
            seen.add(f_clean)
            cleaned.append(f_clean)
    return cleaned
