import pickle

# load vectorizer
vectorizer = pickle.load(open('../model/vectorizer.pickle', 'rb'))
print(vectorizer)

# load model
clf = pickle.load(open('../model/model.pickle', 'rb'))
print(clf)