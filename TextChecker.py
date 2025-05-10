from transformers import pipeline

# Initialize pipelines for sentiment and sarcasm detection
sentiment_analyzer = pipeline("sentiment-analysis")

# Sarcasm detector model - irony detection (Cardiff NLP)
sarcasm_detector = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-irony")

# Toxicity classifier using a community-trained model
toxicity_classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert",
    tokenizer="unitary/toxic-bert"
)

# Function for tracking conversational context (can be expanded)
def track_context(conversation_history, new_comment):
    return conversation_history + [new_comment]

# Rule-based filtering logic
def rule_based_filter(comment, sentiment_result, sarcasm_result):
    if sarcasm_result and sarcasm_result[0]['label'].lower() == 'irony' \
       and sentiment_result and sentiment_result[0]['label'] == 'NEGATIVE':
        return "Potential Indirect Toxicity (Sarcasm + Negative Sentiment)"
    return None

def detect_toxicity(comment, conversation_history=[]):
    print(f"\nAnalyzing comment: '{comment}'")

    # 1. Sentiment and Sarcasm Detection
    sentiment_result = sentiment_analyzer(comment)
    sarcasm_result = sarcasm_detector(comment)

    print(f"  Sentiment: {sentiment_result}")
    print(f"  Sarcasm: {sarcasm_result}")

    # 2. Context Tracking (placeholder logic)
    updated_history = track_context(conversation_history, comment)
    print(f"  Context: {updated_history}")

    # 3. Rule-based filtering
    rule_based_flag = rule_based_filter(comment, sentiment_result, sarcasm_result)
    if rule_based_flag:
        print(f"  Rule-based Flag: {rule_based_flag}")
        return rule_based_flag

    # 4. Toxicity Classification
    toxicity_result = toxicity_classifier(comment)
    print(f"  Toxicity Classification: {toxicity_result}")

    # Check if model flags the comment as toxic (threshold adjustable)
    for res in toxicity_result:
        if res['label'].lower() in ['toxic', 'insult', 'threat'] and res['score'] > 0.7:
            return f"Potential Toxicity ({res['label']})"

    return "Not flagged as overtly toxic"

# Example usage
comments = [
    "Oh, that's just brilliant. Another meeting.",
    "I absolutely loved waiting in line for three hours.",
    "You're so smart, you can't even tie your shoes.",
    "Have a great day!",
    "You're an idiot.",
    "I'm not saying you're wrong, I'm just saying...",
    "Well, aren't you special.",
]

conversation = []
for comment in comments:
    result = detect_toxicity(comment, conversation)
    print(f"→ Detection Result: {result}")
    conversation.append(comment)
