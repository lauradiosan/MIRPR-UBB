import os

from gensim.models import KeyedVectors

from utils import loadData


class Repository:
    def __init__(self):
        self.__word2vecPath = './data/GoogleNews-vectors-negative300.bin'
        self.__filename = './data.csv'
        self.__inputs = []
        self.__outputs = []
        self.numericCols = {'average_rate_per_night': 0, 'bedrooms_count': 1}
        self.stringCols = {'description': 2}
        self.outputCol = {'city': 3}
        self.__word2Vec = self.loadWord2Vec()
        self.loadData()

    def loadWord2Vec(self):
        if not os.path.isfile(self.__word2vecPath):
            print("download from: https://www.kaggle.com/sandreds/googlenewsvectorsnegative300/download")
        return KeyedVectors.load_word2vec_format(self.__word2vecPath, binary=True, limit=100)

    def loadData(self):
        rawInputs, rawOutputs = loadData(self.__filename, list(self.numericCols.keys()) + list(self.stringCols.keys()), list(self.outputCol.keys())[0])

        priceAverage = 0
        for i in range(len(rawInputs)):
        # for i in range(1000):
            containsNA = False
            for j in range(len(rawInputs[0])):
                if rawInputs[i][j] == "NA":
                    containsNA = True
                    break
            if len(rawInputs[i][self.stringCols['description']]) < 5:
                containsNA = True
            if containsNA:
                continue
            rawInputs[i][0] = rawInputs[i][0].replace('$', "")
            if rawInputs[i][0] != "":
                priceAverage += float(rawInputs[i][0])
            if rawInputs[i][1] == "Studio":
                rawInputs[i][1] = 1
            self.__inputs.append(rawInputs[i])
            self.__outputs.append(rawOutputs[i])
        priceAverage = priceAverage / len(self.__inputs)
        for i in range(len(self.__inputs)):
            if self.__inputs[i][0] == "":
                self.__inputs[i][0] = priceAverage

    def getInputs(self):
        return self.__inputs

    def getOutputs(self):
        return self.__outputs

    def getWord2Vec(self):
        return self.__word2Vec


