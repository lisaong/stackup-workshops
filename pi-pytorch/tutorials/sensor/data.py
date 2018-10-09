import pandas as pd
from sklearn.model_selection import train_test_split
import torch

def get_data(sequence_length):
    """Reads the dataset and reshapes it for training with RNN
    Arguments:
        sequence_length: length of the sequence to produce
    Returns:
        X_train: training sequence of shape batch, seq_len, input_size
        X_test: test sequence of shape batch, seq_len, input_size
        y_train: training labels
        y_test: test labels
        X_train, X_test, y_train, y_test datasets
    """
    df = pd.read_csv('iot_sensor_dataset.csv')
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)

    # unfold on first dimension, window by sequence_length
    # shift window by 1 step each time
    X_train = torch.tensor(X_train.values).unfold(0, sequence_length, 1)

    # batch, input_size, seq_len => batch, seq_len, input_size
    X_train = torch.transpose(X_train, 1, 2)

    # left slide the labels to line up with X
    y_train = y_train[len(y_train)-X_train.shape[0]:]

    # Repeat above for test set
    X_test = torch.tensor(X_test.values).unfold(0, sequence_length, 1)
    X_test = torch.transpose(X_test, 1, 2)
    y_test = y_test[len(y_test)-X_test.shape[0]:]

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = get_data(sequence_length=10)
    print(X_train.shape)
    print(y_train.shape)
    print(y_train.value_counts())

    print(X_test.shape)
    print(y_test.shape)
    print(y_test.value_counts())
