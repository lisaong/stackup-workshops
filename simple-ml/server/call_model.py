import sys
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Sms input (e.g. "hello :)").'
    'If not provided, reads from STDIN')
args = parser.parse_args()

# load models
vectorizer = pickle.load(open('../model/vectorizer.pickle', 'rb'))
model = pickle.load(open('../model/model.pickle', 'rb'))

def classify(input):
    Z_text = vectorizer.transform([input])
    prediction = model.predict(Z_text.toarray())
    print(prediction[0])

if args.input:
    classify(args.input)
else:
    line = sys.stdin.readline()
    while line:
        classify(line)
        line = sys.stdin.readline()
