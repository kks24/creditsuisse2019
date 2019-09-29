import logging
from flask import request, jsonify;
from codeitsuisse import app;
import nltk.classify.util
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


logger = logging.getLogger(__name__)

@app.route('/sentiment-analysis', methods=['POST'])
def Dependency_Manager_main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = request.get_json();
    result = solution(inputValue)
    return jsonify(result);

def solution(reviews):
    output = dict()
    output["response"] = []
    
    f = open('my_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    outlist=[]
    for i in range(len(reviews["reviews"])):
        text = ''+ reviews["reviews"][i]
        review_text = '''\+ text \+'''
        words = word_tokenize(review_text)
        words = create_word_features(words)
        outdict={}
        output["response"].append(classifier.classify(words))
        print(classifier.classify(words))
    
    return output

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict
