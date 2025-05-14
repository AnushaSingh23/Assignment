import json
from insights_generator import generate_insight_cards
import matplotlib.pyplot as plt
import seaborn as sns

def load_feedback(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def save_output(insights, output_path):
    with open(output_path, "w") as f:
        json.dump(insights, f, indent=2)

def plot_insights(insights):
    themes = [card["theme"] for card in insights]
    quote_counts = [len(card["quotes"]) for card in insights]

    plt.figure(figsize=(10, 5))
    sns.barplot(x=themes, y=quote_counts, palette="viridis")
    plt.title("Number of Supporting Quotes per Theme")
    plt.ylabel("Quote Count")
    plt.xlabel("Insight Theme")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    sentiments = [card.get("sentiment", "unknown") for card in insights]
    sentiment_counts = {s: sentiments.count(s) for s in set(sentiments)}

    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Sentiment Distribution")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    feedback = load_feedback("C:/Users/Akshansh Sourabh/Downloads/insight_synthesizer_gpt35/insight_synthesizer/responses.json")
    insights = generate_insight_cards(feedback)
    save_output(insights, "output.json")
    plot_insights(insights)
