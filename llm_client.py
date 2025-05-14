from transformers import pipeline
import json
import re

model_name = "gpt2"
generator = pipeline('text-generation', model=model_name, tokenizer=model_name)

def extract_json(text):
    """
    Try to extract a JSON array from the generated text using regex.
    """
    match = re.search(r"\[\s*{.*?}\s*\]", text, re.DOTALL)
    if match:
        try:
            cleaned_text = match.group(0).strip().replace("\n", " ").replace("’", "'")
            return json.loads(cleaned_text)
        except json.JSONDecodeError as e:
            print("⚠️ JSON parsing failed:", e)
            print("Failed text:", cleaned_text)
    return []


def call_model(prompt: str):
    outputs = generator(prompt, max_length=500, num_return_sequences=1, temperature=0.7)
    content = outputs[0]['generated_text']

    print("=== Raw Output ===")
    print(content)
    print("==================")

    insights = extract_json(content)
    if not insights:
        print("[Warning] Failed to parse model output as JSON.")
    return insights
