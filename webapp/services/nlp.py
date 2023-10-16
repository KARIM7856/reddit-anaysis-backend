from nltk.probability import FreqDist
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize, RegexpTokenizer  # tokenize words
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


async def download_stopwords():

    nltk.download('stopwords')
download_stopwords()

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
             "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def get_freq_dist(text_array):

    tk = TweetTokenizer().tokenize('\n'.join(text_array))
    tk = [word for word in tk if word not in set(
        stopwords) and word not in r".$/(){}!;',#$%^&*[]|\<>?+=*-_`\":;~"]
    return FreqDist(tk)


def get_sentiments(text_array):
    # nltk.download('vader_lexicon')
    #sent_a = SentimentIntensityAnalyzer()
    sents = [{'sent': {'pos': 0, 'neg': 0, 'neu': 0}, 'text': text} for text in text_array]

    most_positive = max(sents, key=lambda x: x["sent"]["pos"])
    most_negative = max(sents, key=lambda x: x["sent"]["neg"])
    most_neutral = max(sents, key=lambda x: x["sent"]["neu"])

    return (most_positive, most_neutral, most_negative)
