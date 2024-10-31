import pandas as pd
import random

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data/cleaned_data.csv')  # Thay đường dẫn tới file đã được gán nhãn

# Từ điển từ đồng nghĩa cho các lý do khám
synonyms = {
    "Kiểm tra thai kỳ": ["Kiểm tra sức khỏe thai", "Khám thai"],
    "Khám tổng quát": ["Khám sức khỏe tổng quát", "Khám định kỳ"],
    "Đau bụng": ["Cảm thấy đau bụng", "Đau dạ dày"],
    "Khám bệnh nhi": ["Khám cho trẻ em", "Khám sức khỏe trẻ nhỏ"]
}

# Hàm mở rộng dữ liệu
def augment_data(reason):
    if reason in synonyms:
        return random.choice(synonyms[reason])
    return reason

# Áp dụng mở rộng cho cột "Lý do đến khám/điều trị"
df['Lý do đến khám/điều trị'] = df['Lý do đến khám/điều trị'].apply(augment_data)

# Lưu lại dữ liệu đã mở rộng
df.to_csv('data/augmented_data.csv', index=False)  # Lưu vào file augmented_data.csv trong thư mục data
