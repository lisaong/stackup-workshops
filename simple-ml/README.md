## SMS Spam Detector

### Slides
[http://bit.ly/sms-spam-nodejs](http://bit.ly/sms-spam-nodejs)

### Dataset

[SMS Spam Collection v.1](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

Original source: http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/ 

### Training

This trains a classifier using scikit-learn to label messages as 'ham' or 'spam'.

Training is optional, as the model files are already stored under the `model/` subfolder.

Download [Anaconda](https://www.anaconda.com/download/), select the Python 3.x version.

```
conda create -n simple-ml python=3
conda activate simple-ml
conda install pandas jupyter scikit-learn
jupyter notebook
```

Download dataset from the link above, and extract the files into the `data/` sub-folder.

Run through simple-sms-spam-classifier.ipynb. If all goes well, the model files under the `model/` subfolder will be updated.

### Server

Requires: [NodeJS](https://nodejs.org/en/download/) v8 or later

```
# Run from the simple-ml anaconda environment
npm install
npm start
```

1. Open browser to http://localhost:3000
2. Input a SMS string (up to 160 characters)

![input](assets/input.png)

3. Click 'Spam or Ham?'

![result](assets/result.png)
