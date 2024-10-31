import pandas as pd

def clean_data(data):
    # Ví dụ làm sạch dữ liệu
    data = data.dropna()  # Loại bỏ các dòng có giá trị NaN
    cleaned_file = "data/cleaned_data.csv"
    data.to_csv(cleaned_file, index=False)
    return cleaned_file
