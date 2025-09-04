from transformers import pipeline

def analyze_sentiment(texts):
    classifier = pipeline("sentiment-analysis")
    results = []
    for text in texts:
        result = classifier(text)[0]
        results.append({
            "text": text,
            "label": result['label'],
            "score": round(result['score'], 2)
        })
    return results

if __name__ == "__main__":
    # Example usage
    sample_texts = [
        "I love my new MacBook, it's blazing fast!",
        "The weather is terrible today.",
        "I feel okay, not too bad, not too good."
    ]

    analysis = analyze_sentiment(sample_texts)
    for res in analysis:
        print(f"Text: {res['text']}")
        print(f"Prediction: {res['label']} (Confidence: {res['score']})\n")
