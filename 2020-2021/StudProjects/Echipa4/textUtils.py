from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re


def removeNonAscii(s):
    return "".join(i for i in s if ord(i) < 128)


def make_lower_case(text):
    return text.lower()


def remove_stop_words(text):
    stops = set(stopwords.words("english"))
    text = [w for w in text.split() if not w in stops]
    return " ".join(text)


def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    return " ".join(text)


def split_words(text):
    result = []
    for word in text.split():
        match = re.match(r"([0-9]+)([a-z]+)|([a-z]+)([0-9]+)", word, re.I)
        if match:
            [result.append(group) for group in match.groups() if group is not None]
        else:
            result.append(word)
    return " ".join(result)


def cleanAll(text):
    text = removeNonAscii(text)
    text = make_lower_case(text)
    text = remove_stop_words(text)
    text = remove_punctuation(text)
    text = split_words(text)
    return text


def getTFIDF_vectors(words, wordsCorpus, google_model):
    tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=5, stop_words='english')
    tfidf.fit(words)
    tfidf_list = dict(zip(tfidf.get_feature_names(), list(tfidf.idf_)))
    tfidf_feature = tfidf.get_feature_names()
    tfidf_vectors = []
    line = 0
    totalLines = str(len(wordsCorpus))
    for corp in wordsCorpus:
        tfidf_vectors.append(getVector(corp, tfidf_feature, tfidf_list, google_model))
        line += 1
        print(str(line) + "/" + totalLines, end='\r')

    return tfidf_feature, tfidf_list, tfidf_vectors


def getVector(desc, tfidf_feature, tfidf_list, google_model):
    sent_vec = np.zeros(300)
    weight_sum = 0
    for word in desc:
        if word in google_model.wv.vocab and word in tfidf_feature:
            vec = google_model.wv[word]
            tf_idf = tfidf_list[word] * (desc.count(word) / len(desc))
            sent_vec += (vec * tf_idf)
            weight_sum += tf_idf
    if weight_sum != 0:
        sent_vec /= weight_sum
    return sent_vec
