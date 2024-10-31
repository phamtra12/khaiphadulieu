# import pandas as pd

# def label_data(input_file):
#     # Đọc dữ liệu từ file CSV
#     data = pd.read_csv(input_file)
    
#     # Gán nhãn dựa trên giá trị của cột 'Trung bình Cộng'
#     data['Nhãn dữ liệu'] = data['Trung bình Cộng'].apply(
#         lambda x: "Hài lòng" if x > 3 else "Không hài lòng" if x < 3 else "Bình thường"
#     )
    
#     # Lưu lại dữ liệu đã gán nhãn vào file mới
#     labeled_file = "data/labeled_data.csv"
#     data.to_csv(labeled_file, index=False)
    
#     return labeled_file
import pandas as pd

def label_data(input_file):
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(input_file)
    
    # Gán nhãn mới dựa trên giá trị của cột 'Nhãn'
    data['Nhãn số'] = data['Nhãn'].apply(
        lambda x: 1 if x == "Hài lòng" else 2 if x == "Không hài lòng" else 3
    )
    
    # Lưu lại dữ liệu đã gán nhãn vào file mới
    labeled_file = "data/labeled_data.csv"
    data.to_csv(labeled_file, index=False)
    
    return labeled_file