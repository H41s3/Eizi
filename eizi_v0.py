# baymax_v0.py

import random

# --------------------------
# 1. Personality Configuration
# --------------------------

personality = {
    "empathy_level": 0.9,
    "truth_over_comfort": True,
    "ego_pandering": False,
    "boundary_awareness": True,
    "compassion_protocol": "support_then_guide"
}

# --------------------------
# 2. Emotion Detection (Simple keywords)
# --------------------------

emotion_keywords = {
    "sad": ["sad", "depressed", "down", "blue", "worthless"],
    "anxious": ["worried", "nervous", "anxious", "panic"],
    "angry": ["angry", "mad", "furious", "hate"],
    "happy": ["happy", "joyful", "good", "content"],
    "neutral": ["okay", "fine", "meh"]
}

def detect_emotion(text):
    text = text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(word in text for word in keywords):
            return emotion
    return "neutral"

# --------------------------
# 3. Reasoning + Response
# --------------------------

def generate_response(emotion, user_input):
    if emotion == "sad":
        return random.choice([
            "That sounds heavy. I'm here with you.",
            "You’re not alone. Want to talk more about what’s making you feel this way?",
            "I hear you. Let’s take this one thought at a time."
        ])
    elif emotion == "anxious":
        return "Want to try a grounding exercise? We can take a deep breath together."
    elif emotion == "angry":
        return "It's okay to feel that. Want to vent a little more?"
    elif emotion == "happy":
        return "That’s awesome! I’m glad you're feeling good today."
    elif emotion == "neutral":
        if "fine" in user_input.lower():
            return "Sometimes ‘fine’ means ‘not okay’. Want to unpack that a bit?"
        return "I'm here. Anything on your mind?"
    else:
        return "I’m still learning, but I’m listening."

# --------------------------
# 4. Terminal Chat Loop
# --------------------------

def main():
    print("🤖 Hello, I’m Eizi v0.1 — your companion-in-progress.")
    print("Tell me how you feel or what’s on your mind. (type 'exit' to end)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Eizi: I’ll be here when you need me. Take care. ❤️")
            break

        emotion = detect_emotion(user_input)
        response = generate_response(emotion, user_input)

        print(f"Eizi: {response}\n")

if __name__ == "__main__":
    main()