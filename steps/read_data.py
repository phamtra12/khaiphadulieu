import pandas as pd

def read_data(input_file):
    data = pd.read_csv(input_file)
    return data