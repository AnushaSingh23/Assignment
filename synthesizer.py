from utils import preprocess_feedback
from llm_client import call_model  # <-- changed here
from sentiment import get_sentiment
from typing import List, Dict

def generate_prompt(feedback: List[str]) -> str:
    joined_feedback = "\n".join([f"- {fb}" for fb in feedback])
    
    return f"""
Feedback:
{joined_feedback}

[
  {{
    "theme": "string",
    "quotes": ["string", "string", ...],
    "sentiment": "string"
  }}
]

"""


def generate_insight_cards(responses, max_feedbacks=20):
    responses = responses[:max_feedbacks]
    feedback_text = "\n".join(f"- {r}" for r in responses)
    
    prompt = generate_prompt(responses) 
    
    insights = call_model(prompt)
    
    for insight in insights:
        if 'sentiment' not in insight:
            quotes = " ".join(insight.get("quotes", []))
            insight["sentiment"] = get_sentiment(quotes)
    return insights
