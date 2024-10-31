import pandas as pd

def normalize_text(input_file):
    data = pd.read_csv(input_file)
    
    # Sử dụng cột "Lý do đến khám/điều trị" để chuẩn hóa
    if 'Lý do đến khám/điều trị' in data.columns:
        data['Normalized_Text'] = data['Lý do đến khám/điều trị'].str.lower()
    else:
        raise ValueError("Cột 'Lý do đến khám/điều trị' không tồn tại trong file đầu vào.")
    
    normalized_file = "data/normalized_data.csv"
    data.to_csv(normalized_file, index=False)
    return normalized_file
