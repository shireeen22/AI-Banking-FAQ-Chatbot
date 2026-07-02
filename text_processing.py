import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def text_preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)