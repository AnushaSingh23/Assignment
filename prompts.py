INSIGHT_PROMPT_TEMPLATE = """
You are an AI assistant helping summarize user survey feedback into clear insights for product managers.

Given the following list of feedback responses:
{feedback_list}

Create 3 insight cards. Each insight card should contain:
- A concise theme title
- Up to 12 supporting quotes
- An optional sentiment label (positive, neutral, negative)

Respond only in valid JSON format as follows:
[
  {{
    "theme": "Theme Title",
    "quotes": ["quote1", "quote2", "..."],
    "sentiment": "positive"
  }},
  ...
]
"""
