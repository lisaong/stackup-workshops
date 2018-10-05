import sys
import pickle

# load models
vectorizer = pickle.load(open('../model/vectorizer.pickle', 'rb'))
model = pickle.load(open('../model/model.pickle', 'rb'))

# read input from stdin, return predictions to stdout
line = sys.stdin.readline()
while line:
    Z_text = vectorizer.transform([line])
    prediction = model.predict(Z_text.toarray())
    print(prediction[0])
    line = sys.stdin.readline()
