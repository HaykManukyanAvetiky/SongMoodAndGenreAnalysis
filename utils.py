
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, RegexpTokenizer
import re
from nltk.corpus import stopwords



stemmer = SnowballStemmer("english")
tokenizer = RegexpTokenizer("[\w’]+", flags=re.UNICODE)

def tokenize(s):
    s = s.lower()
    tokens = tokenizer.tokenize(s)
    tokens = [stemmer.stem(t) for t in tokens]
    return tokens

class Vectorizer(TfidfVectorizer):
    def __init__(self):
        super(Vectorizer, self).__init__(tokenizer = tokenize ,  stop_words =stopwords.words('english'))

