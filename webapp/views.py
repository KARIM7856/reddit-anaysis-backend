from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import json

# reddit

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer  # tokenize words
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist

import requests

from webapp.services import nlp
from webapp.services import reddit_api as reddit



# Create your views here.
@ csrf_exempt
def hot_topics(request):
    """
    List all code snippets, or create a new snippet.
    """
    return JsonResponse({'data': 'test data'}, safe=False)


@ csrf_exempt
def hashtags(request):
    """
    List all code snippets, or create a new snippet.
    """
    return JsonResponse({'data': ['1', '2', '3']}, safe=False)


class TestList(APIView):

    def get(self, request, format=None):
        return JsonResponse({'testlistdata': "get"})

    def post(self, request, format=None):
        return JsonResponse({'testlistdata': 'post'})


class HashTag(APIView):

    def get(self, request, format=None):

        return JsonResponse({'testlistdata': "get"})

    def post(self, request, format=None):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        hashtag = body['hashtag']

        if hashtag == "":
            return JsonResponse({"data": []})

        all_threads = reddit.get_threads(hashtag)
        all_threads_comments = reddit.get_all_threads_comments(hashtag, all_threads)

        all_subreddit = []

        for th in all_threads_comments:
            all_subreddit.append(th['post'])
            all_subreddit = all_subreddit + th['comments']
            
            all_data_preprocessed = [word.lower().replace(
            '[^\w\s]', '') for word in all_subreddit]

        fdist = nlp.get_freq_dist(all_data_preprocessed)
        (most_positive, most_neutral, most_negative) = nlp.get_sentiments(all_data_preprocessed)

        print(most_positive, most_negative, most_neutral)

        print(len(all_data_preprocessed))
        print(hashtag)
        return JsonResponse({'data': [{"text": word, "value": freq} for word, freq in fdist.items()], 
                             "most_positive": most_positive["text"], 
                             "most_negative": most_negative["text"], 
                             "most_neutral": most_neutral["text"]})
