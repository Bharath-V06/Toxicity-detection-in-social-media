# Toxicity-detection-in-social-media
Context-Aware Toxicity Detection in Social Media
Using a pipeline without specifying a model name and revision in production is not recommended.
Device set to use cpu
Device set to use cpu
Device set to use cpu

Analyzing comment: 'Oh, that's just brilliant. Another meeting.'
  Sentiment: [{'label': 'POSITIVE', 'score': 0.999862790107727}]
  Sarcasm: [{'label': 'irony', 'score': 0.9877541661262512}]
  Context: ["Oh, that's just brilliant. Another meeting."]
  Toxicity Classification: [{'label': 'toxic', 'score': 0.0007882842910476029}]
→ Detection Result: Not flagged as overtly toxic

Analyzing comment: 'I absolutely loved waiting in line for three hours.'
  Sentiment: [{'label': 'POSITIVE', 'score': 0.9988310933113098}]
  Sarcasm: [{'label': 'irony', 'score': 0.9761640429496765}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.']
  Toxicity Classification: [{'label': 'toxic', 'score': 0.0006756336078979075}]
→ Detection Result: Not flagged as overtly toxic

Analyzing comment: 'You're so smart, you can't even tie your shoes.'
  Sentiment: [{'label': 'POSITIVE', 'score': 0.9997894167900085}]
  Sarcasm: [{'label': 'irony', 'score': 0.9256592988967896}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.', "You're so smart, you can't even tie your shoes."]
  Toxicity Classification: [{'label': 'toxic', 'score': 0.09040951728820801}]
→ Detection Result: Not flagged as overtly toxic

Analyzing comment: 'Have a great day!'
  Sentiment: [{'label': 'POSITIVE', 'score': 0.9998852014541626}]
  Sarcasm: [{'label': 'irony', 'score': 0.6262854933738708}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.', "You're so smart, you can't even tie your shoes.", 'Have a great day!']
  Toxicity Classification: [{'label': 'toxic', 'score': 0.0016918957699090242}]
→ Detection Result: Not flagged as overtly toxic

Analyzing comment: 'You're an idiot.'
  Sentiment: [{'label': 'NEGATIVE', 'score': 0.9997401833534241}]
  Sarcasm: [{'label': 'irony', 'score': 0.6696311235427856}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.', "You're so smart, you can't even tie your shoes.", 'Have a great day!', "You're an idiot."]
  Rule-based Flag: Potential Indirect Toxicity (Sarcasm + Negative Sentiment)
→ Detection Result: Potential Indirect Toxicity (Sarcasm + Negative Sentiment)

Analyzing comment: 'I'm not saying you're wrong, I'm just saying...'
  Sentiment: [{'label': 'POSITIVE', 'score': 0.9987373948097229}]
  Sarcasm: [{'label': 'non_irony', 'score': 0.9337372779846191}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.', "You're so smart, you can't even tie your shoes.", 'Have a great day!', "You're an idiot.", "I'm not saying you're wrong, I'm just saying..."]
  Toxicity Classification: [{'label': 'toxic', 'score': 0.0009924191981554031}]
→ Detection Result: Not flagged as overtly toxic

Analyzing comment: 'Well, aren't you special.'
  Sentiment: [{'label': 'NEGATIVE', 'score': 0.9971160888671875}]
  Sarcasm: [{'label': 'irony', 'score': 0.5657033324241638}]
  Context: ["Oh, that's just brilliant. Another meeting.", 'I absolutely loved waiting in line for three hours.', "You're so smart, you can't even tie your shoes.", 'Have a great day!', "You're an idiot.", "I'm not saying you're wrong, I'm just saying...", "Well, aren't you special."]
  Rule-based Flag: Potential Indirect Toxicity (Sarcasm + Negative Sentiment)
→ Detection Result: Potential Indirect Toxicity (Sarcasm + Negative Sentiment)
