import pandas as pd

def tokenize_text(input_file):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(input_file)
    
    # Kiểm tra xem cột 'Normalized_Text' có tồn tại trong dữ liệu không
    if 'Normalized_Text' not in data.columns:
        raise ValueError("Cột 'Normalized_Text' không tồn tại trong dữ liệu.")
    
    # Token hóa văn bản từ cột 'Normalized_Text'
    data['Tokens'] = data['Normalized_Text'].apply(lambda x: x.split())
    
    # Lưu dữ liệu đã token hóa vào file CSV
    tokenized_file = "data/tokenized_data.csv"
    data.to_csv(tokenized_file, index=False)
    
    return tokenized_file
