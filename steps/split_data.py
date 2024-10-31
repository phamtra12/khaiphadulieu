import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_file):
    data = pd.read_csv(input_file)
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    train_file = "data/train_data.csv"
    test_file = "data/test_data.csv"
    train.to_csv(train_file, index=False)
    test.to_csv(test_file, index=False)
    return train_file, test_file
