from transformers import pipeline

summarizer = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-783M", tokenizer="MBZUAI/LaMini-Flan-T5-783M")
sentiment_analyzer = pipeline("sentiment-analysis")

def generate_insight_cards(feedback_list):
    prompt = "Summarize the following feedback into 3 themes with quotes and sentiment:\n"
    prompt += "\n".join(f"- {feedback}" for feedback in feedback_list)
    
    response = summarizer(prompt, max_length=512, do_sample=True)[0]["generated_text"]
    
    print("Raw summary from model:\n", response)
    
    sentiment_result = sentiment_analyzer(response)
    sentiment = sentiment_result[0]['label'].lower() 
    
    insights = [{
        "theme": "Example Theme",
        "quotes": feedback_list[:3], 
        "sentiment": sentiment
    }]
    
    return insights
