import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer  # tokenize words
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist

async def download_stopwords():
    
    nltk.download('stopwords')
download_stopwords()


def get_freq_dist(text_array):

    tk = TweetTokenizer().tokenize('\n'.join(text_array))
    tk = [word for word in tk if word not in set(stopwords.words(
        'english')) and word not in r".$/(){}!;',#$%^&*[]|\<>?+=*-_`\":;~"]
    return FreqDist(tk)
    
def get_sentiments(text_array):
    
    sent_a = SentimentIntensityAnalyzer()
    sents = [{'sent': sent_a.polarity_scores(
    text), 'text': text} for text in text_array]

    most_positive = max(sents, key=lambda x: x["sent"]["pos"])
    most_negative = max(sents, key=lambda x: x["sent"]["neg"])
    most_neutral = max(sents, key=lambda x: x["sent"]["neu"])
    
    return (most_positive, most_neutral, most_negative)
