from sklearn import tree
from sklearn.model_selection import train_test_split

from utils import normalisation, accuracy


class Service:
    def __init__(self, repository):
        self.repository = repository
        self.inputs = repository.getInputs()
        self.outputs = repository.getOutputs()
        self.word2Vec = repository.getWord2Vec()
        self.solve()

    def solve(self):
        x_train, x_test, y_train, y_test = train_test_split(self.inputs, self.outputs, test_size=0.3, random_state=1)

        x_train_numeric = self.getFeatures(x_train, self.repository.numericCols)
        x_train_string = self.getFeatures(x_train, self.repository.stringCols)
        x_test_numeric = self.getFeatures(x_test, self.repository.numericCols)
        x_test_string = self.getFeatures(x_test, self.repository.stringCols)

        x_train_numeric, x_test_numeric = normalisation(x_train_numeric, x_test_numeric)  # normalise the numeric features

        x_train_string = self.vectorizeStringFeatures(x_train_string)  # convert string features to float
        x_test_string = self.vectorizeStringFeatures(x_test_string)

        x_train = self.unionFeatures(x_train_numeric, x_train_string)
        x_test = self.unionFeatures(x_test_numeric, x_test_string)

        clf_tree = tree.DecisionTreeClassifier(criterion='gini', random_state=1)
        clf_tree.fit(x_train, y_train)

        y_computed = clf_tree.predict(x_test)

        acc = accuracy(y_computed, y_test)
        print("accuracy:", acc)

    def vectorizeStringFeatures(self, alist):
        inputs = []
        for i in range(len(alist)):
            featureList = []
            for j in range(len(alist[0])):
                sentence = []
                for word in alist[i][j].split():
                    try:
                        sentence.append(self.word2Vec.get_vector(word))
                    except Exception:
                        sentence.append([0.0] * self.word2Vec.vector_size)
                featureList.append([sum(i) / len(sentence) for i in zip(*sentence)])
            inputs.append(featureList)
        return inputs

    def getFeatures(self, alist, adict):
        numericFeatures = []
        for featureList in alist:
            features = []
            for key in adict:
                features.append(featureList[adict[key]])
            numericFeatures.append(features)
        return numericFeatures

    def unionFeatures(self, x_numeric, x_string):
        x = []
        for i in range(len(x_numeric)):
            featureSentences = list(x_numeric[i])
            for j in range(len(x_string[i])):
                featureSentences += x_string[i][j]
            x.append(featureSentences)
        return x
