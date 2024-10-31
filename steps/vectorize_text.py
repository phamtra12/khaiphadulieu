import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(input_file_labeled):
    # Đọc dữ liệu từ file labeled_data.csv
    data = pd.read_csv(input_file_labeled)

    # Khởi tạo TfidfVectorizer với max_features = 1000
    vectorizer = TfidfVectorizer(max_features=1000)

    # Vector hóa văn bản trong cột 'Lý do đến khám/điều trị'
    X = vectorizer.fit_transform(data['Lý do đến khám/điều trị']).toarray()

    # Chuyển đổi ma trận thành DataFrame với các tên cột vector
    vectorized_data = pd.DataFrame(X, columns=vectorizer.get_feature_names_out())

    # Lưu trữ các giá trị vector hóa dưới dạng list để thêm vào cột 'vector'
    data['vector'] = X.tolist()  # Thêm cột 'vector' vào DataFrame gốc

    # Lưu lại dữ liệu đã vector hóa vào file mới
    vectorized_file = "data/vectorized_data.csv"
    data.to_csv(vectorized_file, index=False)

    return vectorized_file
