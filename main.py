# ============================================================
# PROJECT: INCLUSIVE EMOTION CHECK-IN BOT
# Environment: Google Colab
# Language: Python
#
# This is ONE file. The dataset is inside the code, so there is
# nothing to upload and no other file or database to set up.
# Paste it into a Colab cell and run it.
# ============================================================


# 1. IMPORTING LIBRARIES

import re      # Lets us search for and clean up elements in a text
import random  # Lets the bot pick between different replies


# 2. TEXT CLEANING FUNCTION

def preprocess_text(message):

    # Converts all characters to lowercase
    message = message.lower()

    # Removes punctuation marks (can't becomes "can t")
    message = re.sub(r"[^\w\s]", " ", message)

    # Removes extra spaces
    message = re.sub(r"\s+", " ", message).strip()

    # Returns the cleaned text
    return message


# 3. THE DATASET (our database of emotion words)
#
# The dataset is stored inside the code. Each emotion has a list of
# words and phrases that people use when they feel it.
# To teach the bot something new, add a phrase to a list.

emotion_dataset = {

    "joy": [
        "happy", "glad", "joyful", "delighted", "so good", "feeling great",
        "best day", "over the moon", "cheerful", "good", "great"
    ],

    "excitement": [
        "excited", "can't wait", "so pumped", "thrilled",
        "looking forward to", "stoked", "hyped", "buzzing", "energetic",
        "full of energy"
    ],

    "gratitude": [
        "grateful", "thankful", "appreciate", "thank you so much",
        "means a lot", "so lucky to have", "blessed"
    ],

    "pride": [
        "proud", "i did it", "nailed it", "accomplished", "finally finished",
        "proud of myself", "worked so hard and", "achieved"
    ],

    "calm": [
        "calm", "peaceful", "relaxed", "at peace", "content", "settled",
        "comfortable", "serene", "slow breathing"
    ],

    "hope": [
        "hopeful", "hope", "optimistic", "things will get better",
        "better tomorrow", "looking up", "i believe it will"
    ],

    "love": [
        "love", "adore", "care about", "cherish", "mean the world",
        "affection", "my favorite person", "so fond of"
    ],

    "relief": [
        "relieved", "what a relief", "finally over",
        "weight off my shoulders", "can breathe again", "phew",
        "glad that's over"
    ],

    "curiosity": [
        "curious", "wonder", "fascinated", "i want to know", "interested in",
        "intrigued", "i want to learn", "wondering how"
    ],

    "amusement": [
        "funny", "hilarious", "laughing", "made me laugh", "cracking up",
        "lol", "haha", "so silly"
    ],

    "sadness": [
        "sad", "unhappy", "feeling down", "feel down", "crying", "tears",
        "heartbroken", "feeling low", "depressed", "hurts so much",
        "bad day", "terrible", "awful", "horrible", "heavy"
    ],

    "loneliness": [
        "lonely", "alone", "no one to talk to", "no friends", "isolated",
        "nobody cares", "by myself all the time", "miss having someone"
    ],

    "grief": [
        "grieving", "passed away", "lost someone", "funeral",
        "miss them so much", "mourning", "they are gone", "died"
    ],

    "disappointment": [
        "disappointed", "let down", "expected more",
        "didn't go how i wanted", "not what i hoped", "bummed",
        "discouraged", "failed"
    ],

    "guilt": [
        "guilty", "my fault", "i shouldn't have", "i feel bad about",
        "i regret", "i let them down", "i should have"
    ],

    "shame": [
        "ashamed", "i hate myself", "worthless", "i'm a failure",
        "disgusted with myself", "something is wrong with me",
        "i'm too much", "i'm a burden"
    ],

    "embarrassment": [
        "embarrassed", "so awkward", "cringe", "humiliated", "everyone saw",
        "made a fool of myself", "mortified"
    ],

    "anger": [
        "angry", "furious", "mad", "so mad", "hate", "rage", "livid",
        "can't stand", "unfair", "outraged"
    ],

    "frustration": [
        "frustrated", "annoyed", "irritated", "fed up", "keeps happening",
        "nothing works", "so annoying", "ugh", "again and again"
    ],

    "jealousy": [
        "jealous", "envy", "envious", "wish i had", "why do they get",
        "comparing myself", "everyone else has"
    ],

    "anxiety": [
        "anxious", "nervous", "worried", "what if", "panic",
        "can't stop worrying", "on edge", "racing thoughts", "uneasy",
        "dread", "restless", "shaky", "jittery", "butterflies",
        "tight chest", "racing heart", "stomach hurts"
    ],

    "fear": [
        "scared", "afraid", "terrified", "frightened", "fear", "petrified",
        "i'm scared of"
    ],

    "stress": [
        "stressed", "pressure", "too much to do", "deadline", "so much work",
        "tense", "stretched too thin", "under pressure",
        "juggling too many things", "rough", "headache", "tight shoulders",
        "tight muscles"
    ],

    "confusion": [
        "confused", "don't understand", "feel lost", "makes no sense",
        "unclear", "mixed up", "what does that mean", "can't figure out",
        "puzzled"
    ],

    "boredom": [
        "bored", "nothing to do", "boring", "dull", "nothing is fun",
        "same thing every day", "so uninteresting"
    ],

    "exhaustion": [
        "tired", "exhausted", "drained", "no energy", "worn out", "sleepy",
        "wiped out", "running on empty", "sluggish", "heavy eyes",
        "low energy"
    ],

    "numbness": [
        "numb", "empty", "feel nothing", "nothing matters", "hollow", "flat",
        "don't care anymore", "blank inside", "can't feel anything"
    ],

    "surprise": [
        "surprised", "shocked", "wow", "can't believe", "unexpected",
        "out of nowhere", "didn't see that coming", "astonished"
    ],

    "overwhelm": [
        "overwhelmed", "too much", "can't handle", "everything at once",
        "meltdown", "melting down", "drowning", "too many things",
        "can't cope"
    ],

    "sensory_overload": [
        "too loud", "too bright", "lights hurt", "noise hurts",
        "sensory overload", "can't stand the noise", "too crowded",
        "scratchy", "smell is too strong", "hurts my ears",
        "my head is too loud", "too many sounds"
    ],

    "burnout": [
        "burned out", "burnt out", "burnout", "no spoons", "out of spoons",
        "can't do this anymore", "completely depleted",
        "nothing left to give"
    ],

    "masking_fatigue": [
        "masking", "pretending to be fine", "acting normal",
        "tired of pretending", "hiding who i am", "fake smile",
        "nobody sees the real me", "exhausting to act normal",
        "have to be someone else"
    ],

    "feeling_left_out": [
        "left me out", "didn't include me", "didn't invite me", "they excluded me",
        "left out", "excluded", "not invited", "they ignored me",
        "nobody talked to me", "don't fit in", "outsider", "don't belong",
        "nobody gets me", "misunderstood"
    ],

    "shutdown": [
        "can't talk", "can't speak", "went blank", "shut down",
        "shutting down", "nonverbal", "no words", "can't answer", "frozen",
        "my brain stopped"
    ],

    "unsure": [
        "don't know how i feel", "can't name it", "not sure what i feel",
        "hard to explain", "no words for it", "feel weird",
        "something is off", "feel off", "mixed feelings", "can't describe",
        "can't explain how i feel"
    ]
}


# Turns the dataset into a form that is easy to search:
# {"joy": [["happy"], ["so", "good"]], ...}
emotion_phrases = {}
for emotion, phrases in emotion_dataset.items():
    emotion_phrases[emotion] = []
    for phrase in phrases:
        words = preprocess_text(phrase).split()
        if words:
            emotion_phrases[emotion].append(words)


# 4. REPLIES ASSOCIATED WITH EMOTIONS
# Each emotion has more than one reply so the bot does not
# repeat itself. The replies use clear, literal language
# (no sarcasm or hidden meanings), never push the person to
# talk, and never tell them how they "should" feel.

emotion_replies = {

    "joy": [
        "That sounds really good! I'm glad something is going well for you. 😊 What made it feel good?",
        "I'm happy for you. It's lovely to hear good news. Would you like to tell me more about it?"
    ],

    "excitement": [
        "That sounds exciting! It sounds like this matters to you. What are you looking forward to the most?",
        "There is a lot of energy in that. I'd love to hear more about what's coming up. 🎉"
    ],

    "gratitude": [
        "That is a kind thing to feel. It sounds like someone or something made a real difference for you. 💛",
        "Thank you for sharing that. Appreciation like this is a nice thing to carry. Would you like to tell that person how you feel?"
    ],

    "pride": [
        "You should feel proud. It sounds like you put real effort in, and it shows. 🌟",
        "That is a real accomplishment. Thank you for sharing it with me. What was the hardest part?"
    ],

    "calm": [
        "That sounds peaceful. I'm glad you have a calm moment right now. 🌿",
        "It's good to feel settled. If you want, you can tell me what helped you get here."
    ],

    "hope": [
        "Hope is a strong thing to hold. It sounds like you can see something good ahead. 🌅",
        "I'm glad you're feeling hopeful. What are you hoping for?"
    ],

    "love": [
        "That is a warm feeling. It sounds like someone or something really matters to you. ❤️",
        "Caring about someone is a beautiful thing. Would you like to tell me about them?"
    ],

    "relief": [
        "That sounds like a big weight lifting. I'm glad the hard part is over. 😮‍💨",
        "Relief is a good feeling. You went through something stressful, and now you get to rest."
    ],

    "curiosity": [
        "Curiosity is a great feeling. Learning about the things you care about is worth your time. 🔎",
        "That sounds interesting! What would you like to find out? I can try to help."
    ],

    "amusement": [
        "That sounds funny! Laughing is a good thing to have in a day. 😄",
        "I'm glad something made you laugh. Would you like to share what it was?"
    ],

    "sadness": [
        "I'm sorry you're feeling sad. It's okay to feel this way, and you don't have to hide it here. 💙",
        "That sounds really hard. I'm here and I'm listening. You can tell me as much or as little as you like."
    ],

    "loneliness": [
        "Feeling alone can hurt a lot. Thank you for telling me. You matter, and I'm glad you reached out. 💙",
        "I'm sorry you feel lonely. You deserve people who understand you. Would you like to talk about what kind of connection you wish you had?"
    ],

    "grief": [
        "I'm so sorry for your loss. Grief has no right or wrong way to look. I'm here with you. 🕊️",
        "Missing someone this much shows how much they meant to you. You can talk about them here for as long as you like."
    ],

    "disappointment": [
        "I'm sorry it didn't turn out the way you hoped. It makes sense to feel let down when something matters to you.",
        "That sounds disappointing. The hope and effort you put in still count, even when the result is not what you wanted."
    ],

    "guilt": [
        "It sounds like you care a lot about doing right by other people. Guilt can feel heavy. Would you like to talk about what happened?",
        "Thank you for being honest about this. Making a mistake does not make you a bad person. Is there something you'd like to do to make it right?"
    ],

    "shame": [
        "I'm sorry you feel this way about yourself. You are not broken, and you are not too much. You deserve kindness, including from yourself. 💙",
        "Those feelings are painful, and they are not facts about who you are. I'm here, and I'm not judging you. Would you like to talk about it?"
    ],

    "embarrassment": [
        "That sounds uncomfortable. Almost everyone has had a moment like this, and most people forget about it quickly. 💛",
        "I'm sorry that happened. Feeling embarrassed means you care about how things go. It will get easier with time."
    ],

    "anger": [
        "It sounds like something really upset you. Anger makes sense when something feels unfair. What happened?",
        "I'm listening. You are allowed to be angry. We can talk about it, or you can just write it all out here."
    ],

    "frustration": [
        "That sounds really frustrating. When things keep not working, it is tiring. Do you want to talk it through?",
        "I'm sorry this is so annoying. It's hard when you try and it doesn't work. What has been the hardest part?"
    ],

    "jealousy": [
        "Jealousy is a very human feeling, and it often points to something you want. There is no shame in that.",
        "It can hurt to see other people have something you wish for. Your path is your own. What do you wish you had?"
    ],

    "anxiety": [
        "That sounds stressful. Worry can be loud. You don't have to solve it all right now. Would you like to tell me what is on your mind?",
        "I'm here with you. If your thoughts are racing, we can go one small piece at a time."
    ],

    "fear": [
        "That sounds scary. Thank you for telling me. You are not alone. What feels the most frightening?",
        "Being afraid is a hard feeling. Take your time. If you are in danger right now, please contact local emergency services or someone you trust."
    ],

    "stress": [
        "That sounds like a lot to carry. You don't have to do everything at once. Would it help to list what is on your plate?",
        "I'm sorry you are under so much pressure. It's okay to rest. What is the most urgent thing right now?"
    ],

    "confusion": [
        "That sounds confusing. It's okay not to understand yet. We can go slowly, one piece at a time.",
        "Not understanding something is not a failing. Which part is unclear? I'll try to explain it clearly and directly."
    ],

    "boredom": [
        "That sounds dull. Sometimes a mind needs something interesting. What are you curious about?",
        "Being bored is no fun. Would you like some ideas, or would you rather chat about something you enjoy?"
    ],

    "exhaustion": [
        "That sounds really tiring. Rest is not lazy. It is something your body and brain need. 💤",
        "I'm sorry you are so worn out. If you can, give yourself permission to slow down. Is there something that would help you rest?"
    ],

    "numbness": [
        "Feeling nothing can be strange and uncomfortable. It's okay not to feel anything specific. I'm here with you.",
        "Thank you for telling me. Feeling empty or flat is hard to explain. You don't have to explain it perfectly."
    ],

    "surprise": [
        "That sounds unexpected! How are you feeling about it? 😮",
        "That sounds like a surprise! Sometimes it takes time to know how to feel about something like that."
    ],

    # ---- Feelings that neurodivergent people often describe ----
    # (everyone is welcome to use them)

    "overwhelm": [
        "That sounds like too much at once. You don't have to handle everything right now. We can pick just one small thing. 🫶",
        "I'm sorry things feel so overwhelming. It's okay to pause. You can take your time to reply, or not reply at all."
    ],

    "sensory_overload": [
        "That sounds really uncomfortable. Loud, bright, or crowded places can be painful, and your reaction is real. If you can, move somewhere quieter or dimmer. 🎧",
        "I'm sorry your senses are overloaded. You don't need to push through it. Reducing noise, light, or touch can help, if that is possible for you."
    ],

    "burnout": [
        "That sounds like you have been giving more than you have. Running out of energy is not a personal failing. You deserve real rest. 🔋",
        "I'm sorry you are so depleted. It makes sense to need a break. What is one demand you could lower or pause?"
    ],

    "masking_fatigue": [
        "Pretending to be someone you are not is exhausting. You deserve to be accepted as you are. Do you have a place where you can be yourself? 🌈",
        "Thank you for telling me. Hiding parts of yourself takes a lot of energy. You don't have to mask here."
    ],

    "feeling_left_out": [
        "I'm sorry you felt left out. Wanting to belong is a normal need. How you were treated says more about the situation than about your worth. 💛",
        "That sounds painful. You deserve people who include you and understand you. Would you like to talk about what happened?"
    ],

    "shutdown": [
        "That's okay. You don't have to answer or explain. I'll be here whenever you want to type, even if it's just one word or an emoji.",
        "Thank you for letting me know. When words are hard, time in a quiet space can help. There is no rush and no pressure."
    ],

    "unsure": [
        "That's okay. Not knowing how you feel is common, and feelings can be hard to name. We can look for it together. Does your body feel tense, tired, restless, or heavy?",
        "There is no pressure to find the exact word. I can show you a list of feelings to choose from, or you can describe what is happening in your body or around you."
    ],

    # Used when no emotion is found
    "neutral": [
        "I'm listening. Tell me as much or as little as you want.",
        "Thank you for writing. Could you tell me a bit more? You can use your own words, short or long."
    ]
}


# 5. SAFETY MESSAGE
# If someone writes about hurting themselves, the bot stops
# guessing emotions and points to real people who can help.

crisis_phrases = [
    "kill myself", "want to die", "end my life", "hurt myself",
    "self harm", "suicide", "suicidal", "don t want to be here",
    "no reason to live", "better off without me"
]

crisis_reply = (
    "I'm really glad you told me. What you are feeling matters, and you "
    "deserve support from a real person right now. If you are in Canada, "
    "you can call or text 9-8-8 at any time. If you are somewhere else, "
    "please contact your local crisis line or emergency number. If you "
    "can, tell someone near you, like a family member, friend, or teacher. "
    "I'm here too. 💙"
)


# 6. WORDS THE BOT UNDERSTANDS

# Emojis the bot understands (people can answer with just an emoji)
emoji_map = {
    "😊": "joy", "😀": "joy", "😄": "joy", "🙂": "joy",
    "😢": "sadness", "😭": "sadness", "☹": "sadness", "🙁": "sadness", "😞": "sadness",
    "😡": "anger", "😠": "anger", "🤬": "anger",
    "😨": "fear", "😱": "fear", "😰": "anxiety", "😟": "anxiety",
    "😴": "exhaustion", "🥱": "exhaustion", "😩": "exhaustion",
    "😐": "numbness", "😶": "numbness",
    "🤔": "confusion", "😕": "confusion",
    "😍": "love", "🥰": "love",
    "😳": "embarrassment", "😮": "surprise", "😲": "surprise",
    "🥳": "excitement", "🤩": "excitement", "😌": "calm",
    "😖": "frustration", "😣": "frustration"
}

# Short answers the bot understands
skip_answers = {"skip", "pass", "next", "i d rather not", "rather not", "prefer not to say"}
none_answers = {"no", "nope", "nah", "n", "nothing", "none", "not really", "na", "n a"}
yes_answers = {"yes", "yeah", "yep", "y", "right", "correct", "that fits", "it does"}
no_answers = {"no", "nope", "nah", "n", "wrong", "not really", "that s wrong"}
partly_answers = {"partly", "kind of", "sort of", "somewhat", "a bit", "maybe"}

# Words that flip the meaning of a feeling ("not happy")
negations = {"not", "no", "never", "don", "didn", "isn", "aren", "wasn", "cannot", "hardly"}

# 7. HELPER FUNCTIONS

# Names that read better in a sentence
display_names = {"feeling_left_out": "left out"}


def label(emotion):
    # Turns "sensory_overload" into "sensory overload"
    return display_names.get(emotion, emotion.replace("_", " "))


def is_crisis(text):
    return any(phrase in text for phrase in crisis_phrases)


def emotion_from_label(text):
    # Lets the person type a feeling word by itself,
    # like "anxiety" or "sensory overload"
    for emotion in emotion_replies:
        if text in (label(emotion), emotion.replace("_", " ")) and emotion != "neutral":
            return emotion
    return None


def list_of_feelings():
    names = [label(e) for e in emotion_replies if e != "neutral"]
    return "Here are some feeling words. Type one, or describe it your own way:\n" + ", ".join(names)


# 8. EMOTION DETECTION FUNCTIONS

def score_message(message):

    # Cleans the message before analysis
    tokens = preprocess_text(message).split()

    # Sets the score of each emotion to zero
    scores = {emotion: 0 for emotion in emotion_phrases}

    for emotion, phrases in emotion_phrases.items():
        for phrase in phrases:
            size = len(phrase)

            # Looks for the phrase anywhere in the message (whole words only)
            for i in range(len(tokens) - size + 1):
                if tokens[i:i + size] == phrase:

                    # Skips the match if a negation comes just before it
                    before = tokens[max(0, i - 3):i]
                    if any(word in negations for word in before):
                        continue

                    # Longer phrases are stronger evidence
                    scores[emotion] += size

    # Looks for emojis in the original message
    for character in message:
        if character in emoji_map and emoji_map[character] in scores:
            scores[emoji_map[character]] += 1

    return scores


def rank_emotions(scores):

    # Sorts emotions from highest to lowest score
    ranked = sorted(scores, key=scores.get, reverse=True)
    top, second = ranked[0], ranked[1]

    # No emotion found
    if scores[top] == 0:
        return ["neutral"]

    # Two strong emotions at once: people can feel more than one thing
    if scores[second] > 0 and scores[second] >= 0.6 * scores[top]:
        return [top, second]

    return [top]


# WAYS TO HELP
# After the bot names a feeling, it offers a few gentle ideas.
# They are suggestions, never orders, and the person can ignore them.

ways_to_help = {

    "joy": [
        "Share the good news with someone you trust, or write it down so you can read it later.",
        "Notice what helped you feel this way, so you can do more of it.",
        "Enjoy it. You don't have to explain or earn good moments."
    ],

    "excitement": [
        "Write down what you're looking forward to, or tell someone about it.",
        "If your energy feels big, moving can help, like walking, stretching, or dancing.",
        "If it's hard to focus, pick one small thing to do first."
    ],

    "gratitude": [
        "Tell the person, or write them a short thank-you note.",
        "Write down one thing you're grateful for so you can keep it.",
        "Let yourself enjoy the feeling. It's okay to just feel good."
    ],

    "pride": [
        "Tell someone who will be happy for you, or write down what you did.",
        "Remember the effort behind it, not only the result.",
        "Reward yourself in a way you like, such as a favorite snack or activity."
    ],

    "calm": [
        "Notice what is helping you feel calm, like a place, a sound, or an activity.",
        "Write down how you got here, so you can find your way back later.",
        "Enjoy the quiet. You don't need to do anything with it."
    ],

    "hope": [
        "Write down what you're hoping for and one small step toward it.",
        "Share your hope with someone who supports you.",
        "Remember this feeling for harder days."
    ],

    "love": [
        "Tell the person, or show it in a way you both like, like a message or a small gift.",
        "Spend time doing something together that you both enjoy.",
        "Write down what you appreciate about them."
    ],

    "relief": [
        "Give yourself time to rest. Your body and mind worked hard.",
        "Do something small and pleasant to mark that it's over.",
        "Notice what helped you get through, in case you need it again."
    ],

    "curiosity": [
        "Write your questions down so you don't lose them.",
        "Pick one question to explore first, using a book, a video, or a person who knows.",
        "Follow your interest. Curiosity is a good reason to learn something."
    ],

    "amusement": [
        "Share the funny thing with a friend.",
        "Save it somewhere so you can come back to it when you need a smile.",
        "Enjoy the laugh."
    ],

    "sadness": [
        "Let yourself feel it. You don't have to hide it or fix it right now.",
        "Do something gentle: a warm drink, comforting music, a favorite show, or a soft blanket.",
        "Reach out to someone you trust, even with a short message like 'I'm having a hard day.'"
    ],

    "loneliness": [
        "Send a short message to someone you trust. It can be just one line.",
        "Look for a group about something you like, online or in person, such as a club or hobby group.",
        "Being near other people without needing to talk can also help, like in a library or a park."
    ],

    "grief": [
        "Be patient with yourself. Grief doesn't follow a schedule.",
        "Talk about the person, write to them, or look at photos, if that feels okay.",
        "Tell a trusted adult, friend, or counselor how you're doing. You don't have to carry this alone."
    ],

    "disappointment": [
        "Allow yourself to feel let down for a while.",
        "Write down what you learned, or what you're proud of for trying.",
        "When you're ready, pick one small next step or a plan B."
    ],

    "guilt": [
        "Think about whether you can repair something, like with a sincere apology.",
        "Remind yourself that mistakes are part of being human.",
        "If it's hard to let go, talk about it with someone you trust."
    ],

    "shame": [
        "Try talking to yourself the way you would talk to a good friend.",
        "Share how you feel with someone safe. Shame gets smaller when it is spoken.",
        "If these thoughts are strong or constant, a counselor or trusted adult can help."
    ],

    "embarrassment": [
        "Remember that most people forget these moments quickly.",
        "If it helps, laugh about it with a friend or write about it.",
        "Give yourself some space, then do something you enjoy."
    ],

    "anger": [
        "Give yourself some space before you respond, if you can.",
        "Move your body, like walking or stretching, or write everything down without sending it.",
        "When you're calmer, think about what you need and how to ask for it."
    ],

    "frustration": [
        "Take a short break and come back with fresh energy.",
        "Break the problem into smaller steps, or ask someone for help.",
        "Write down what is blocking you, so it's out of your head."
    ],

    "jealousy": [
        "Notice what you wish for. It can show you what matters to you.",
        "Remember that you only see parts of other people's lives.",
        "Pick one small step toward something you want."
    ],

    "anxiety": [
        "Try slowing your breathing, or press your feet into the floor and name 5 things you can see.",
        "Write down your worries, then circle the ones you can do something about.",
        "Talk to someone you trust. Saying a worry out loud often makes it smaller."
    ],

    "fear": [
        "If you are in danger, contact local emergency services or a trusted adult right away.",
        "Tell someone what you're afraid of. You don't have to face it alone.",
        "Look around and focus on what is safe right now."
    ],

    "stress": [
        "Write a short list and pick just one thing to do first.",
        "Take a short break: some water, a stretch, or a few minutes away from screens.",
        "If you can, ask for more time or for help with one thing."
    ],

    "confusion": [
        "Write down what is unclear, and ask one person one clear question.",
        "Break it into smaller pieces and do them one at a time.",
        "It's okay to say 'Can you explain that in a different way?'"
    ],

    "boredom": [
        "Try something small and new: a podcast, a drawing, a short walk, or a game.",
        "Pick something you're curious about and look it up.",
        "Message a friend and plan something to do."
    ],

    "exhaustion": [
        "Rest if you can: a nap, an early night, or quiet time away from screens.",
        "Drink some water and eat something if you haven't yet.",
        "Pick the one thing that truly needs doing today, and let the rest wait."
    ],

    "numbness": [
        "Try gentle things you like: warm water, a soft blanket, music, or a favorite taste.",
        "You don't have to force a feeling. Small routines can help you feel steady.",
        "If the numb feeling lasts a long time, talk to a trusted adult or counselor."
    ],

    "surprise": [
        "Give yourself time to take it in. You don't have to decide how you feel right away.",
        "Talk it over with someone you trust.",
        "Write down your thoughts if that helps you sort them out."
    ],

    "overwhelm": [
        "Pause. You have permission to stop for a few minutes.",
        "Choose just one thing, the smallest one, and let the rest wait for now.",
        "Go somewhere quieter if you can, or use headphones or a dimmer light."
    ],

    "sensory_overload": [
        "Move somewhere quieter or dimmer if you can.",
        "Use tools that help you: headphones, earplugs, sunglasses, a hat, or soft clothes.",
        "Give yourself time to recover afterwards, without having to talk or explain."
    ],

    "burnout": [
        "Lower or pause one demand if you can, even a small one.",
        "Plan real rest that is not another task: sleep, quiet, or a favorite easy activity.",
        "Tell someone you trust that you're running low, and ask for help with one thing."
    ],

    "masking_fatigue": [
        "Find a place or a person where you can be yourself, even for a short time.",
        "Give yourself quiet recovery time after situations where you had to mask.",
        "If you want to, tell one safe person what it is like for you."
    ],

    "feeling_left_out": [
        "Reach out to one person you feel comfortable with, even with a short message.",
        "Look for a group built around something you love. Shared interests make connection easier.",
        "Remember that being left out says more about the situation than about your worth."
    ],

    "shutdown": [
        "You don't have to talk or explain. Quiet time in a safe place can help.",
        "Reduce input: dim light, less noise, fewer people, a comfortable spot.",
        "When you're ready, use whatever way of communicating is easiest, like a short text, an emoji, or a gesture."
    ]
}


def help_text(emotions_found):

    # Takes the ideas for the main feeling (and one for the second feeling)
    tips = list(ways_to_help.get(emotions_found[0], []))
    if len(emotions_found) == 2:
        tips += ways_to_help.get(emotions_found[1], [])[:1]

    if not tips:
        return ""

    return "Here are some things that might help:\n" + "\n".join("  - " + tip for tip in tips)


# 9. THE CONVERSATION

opening_message = "Hey, how are you today? Tell me in your own words. You can use a word, a sentence, or an emoji."

greeting_words = {"hello", "hi", "hey", "hiya", "good morning", "good afternoon", "good evening"}
thanks_words = {"thanks", "thank you", "thx", "thank you so much"}
fine_words = {"fine", "okay", "ok", "alright", "all right", "so so", "meh"}

# Gentle questions that keep the conversation going
keep_talking = [
    "What else is on your mind?",
    "I'm still here. Do you want to tell me more?",
    "How are things feeling now?",
    "Is there anything else you'd like to talk about?"
]


def respond_to(emotions_found, state):

    main = emotions_found[0]
    state["guess"] = emotions_found
    reply = random.choice(emotion_replies.get(main, emotion_replies["neutral"]))

    # Nothing to confirm when the person is unsure
    if main == "unsure":
        state["stage"] = "choose"
        return reply + "\n\n" + list_of_feelings()

    # Says the guess gently and admits it might be wrong
    if len(emotions_found) == 2:
        intro = (f"It sounds like you might be feeling a mix of "
                 f"{label(emotions_found[0])} and {label(emotions_found[1])}.")
    else:
        intro = f"It sounds like you might be feeling {label(main)}."

    # Now the bot waits to hear if the guess fits (but the person can also just keep talking)
    state["stage"] = "confirm"

    parts = [
        f"{intro} I might be wrong, because I can only read your words.",
        reply,
        help_text(emotions_found),
        "Does that fit? You can answer yes, no, or partly. Or just keep talking to me."
    ]
    return "\n\n".join(part for part in parts if part)


def chatbot_reply(message, state):

    # Checks whether the user sent an empty message
    if not message.strip():
        return "There is no pressure to write. I'm here whenever you're ready."

    # Cleans the user's message
    text = preprocess_text(message)
    tokens = text.split()

    # Safety comes first, always
    if is_crisis(text):
        state["stage"] = "chat"
        return crisis_reply

    # Shows the list of feelings
    if text == "list":
        return list_of_feelings()

    stage = state["stage"]

    # ---- The bot asked "Does that fit?" ----
    if stage == "confirm":

        if text in yes_answers:
            state["stage"] = "chat"
            return "Thank you for telling me. I'm glad I understood. " + random.choice(keep_talking)

        if text in no_answers:
            state["stage"] = "choose"
            return ("Thank you for telling me, and sorry I got it wrong. "
                    "Only you know how you feel.\n\n" + list_of_feelings())

        if text in partly_answers:
            state["stage"] = "choose"
            return ("Thank you. Feelings are often mixed, and that is normal. "
                    "Which part does not fit? You can describe it, or pick from the list.\n\n"
                    + list_of_feelings())

    # ---- The person picks a feeling from the list ----
    if stage in ("confirm", "choose"):

        chosen = emotion_from_label(text)
        if chosen:
            state["stage"] = "chat"
            parts = [random.choice(emotion_replies[chosen]),
                     help_text([chosen]),
                     random.choice(keep_talking)]
            return "\n\n".join(part for part in parts if part)

    # ---- Normal conversation: any message can start a new topic ----

    # Short messages: greetings, thanks, yes, no
    if len(tokens) <= 4:

        if text in greeting_words:
            state["stage"] = "chat"
            return "Hi! I'm glad you're here. How are you feeling today?"

        if text in thanks_words:
            state["stage"] = "chat"
            return "You're welcome! " + random.choice(keep_talking)

        if text in fine_words:
            state["stage"] = "chat"
            return ("Thanks for telling me. Sometimes 'fine' has more to it, and sometimes "
                    "it really is fine. Either way is okay. If you want to say more, I'm listening.")

        if text in yes_answers:
            state["stage"] = "chat"
            return "I'm listening. Tell me more."

        if text in none_answers:
            state["stage"] = "chat"
            return "That's okay. I'm here whenever you want to talk."

    # Looks for feelings in the message
    found = rank_emotions(score_message(message))

    # No feeling found: keeps the conversation open
    if found == ["neutral"]:
        state["stage"] = "chat"
        return random.choice(emotion_replies["neutral"])

    return respond_to(found, state)


# 10. RUNNING THE CHATBOT
# The conversation keeps going until the person decides to leave.

print("===================================")
print("   INCLUSIVE EMOTION SUPPORT BOT")
print("===================================")
print("Hi! You can talk to me in your own words: a word, a sentence, or an emoji.")
print("I read what you write, tell you the feelings I notice,")
print("and suggest some ways to help. I can be wrong, and you can always correct me.")
print("Type 'list' to see feeling words. Type 'quit' when you want to leave.")
print("There is no rush.\n")

# The bot remembers what it is waiting for (chat, confirm, or choose)
state = {"stage": "chat", "guess": None}

print("Chatbot:", opening_message)

while True:

    try:
        # Waits for the person's message
        user_message = input("\nYou: ")
    except EOFError:
        break

    # The person decides when to leave
    if user_message.lower().strip() in ["quit", "exit", "stop", "bye", "goodbye"]:
        print("Chatbot: Goodbye! Take care of yourself. I'm here whenever you want to talk again.")
        break

    # Generates and displays the chatbot's reply
    print("Chatbot:", chatbot_reply(user_message, state))
