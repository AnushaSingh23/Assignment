## Setup
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

## Output Format
```json
[
  {
    "theme": "Privacy Concerns",
    "quotes": [
      "Privacy is my biggest concern...",
      "Would love integrations, but only if theyre secure.",
      ...
    ],
    "sentiment": "neutral"
  }
]
```
