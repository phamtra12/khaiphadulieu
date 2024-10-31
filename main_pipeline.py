import os
import pandas as pd
from tkinter import Tk, Button, Label, Toplevel, Scrollbar, Frame
from tkinter import ttk
from steps.read_data import read_data
from steps.clean_data import clean_data
from steps.normalize_text import normalize_text
from steps.tokenize_text import tokenize_text
from steps.label_data import label_data
from steps.vectorize_text import vectorize_text
from steps.handle_missing_noise import handle_missing_noise
from steps.split_data import split_data
from steps.augment_data import augment_data

class DataPipelineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Processing Pipeline")
        self.input_file = 'data/khaosat.csv'
        self.data = None

        Label(root, text="Data Processing Pipeline", font=("Arial", 16)).pack(pady=10)
        Button(root, text="1. Read Data", command=self.step_read_data).pack(pady=5)
        Button(root, text="2. Clean Data", command=self.step_clean_data).pack(pady=5)
        Button(root, text="3. Normalize Text", command=self.step_normalize_text).pack(pady=5)
        Button(root, text="4. Tokenize Text", command=self.step_tokenize_text).pack(pady=5)
        Button(root, text="5. Label Data", command=self.step_label_data).pack(pady=5)
        Button(root, text="6. Vectorize Text", command=self.step_vectorize_text).pack(pady=5)
        Button(root, text="7. handle missing noise", command=self.step_handle_missing_noise).pack(pady=5)
        Button(root, text="8. split data", command=self.step_split_data).pack(pady=5)
        Button(root, text="9. Data Augmentation", command=self.step_augment_data).pack(pady=5)

    def show_data_in_table(self, data, title="Data"):
        top = Toplevel(self.root)
        top.title(title)
        
        # Frame chứa Treeview và Scrollbars
        frame = Frame(top)
        frame.pack(expand=True, fill='both')
        
        # Tạo Treeview
        tree = ttk.Treeview(frame, columns=list(data.columns), show='headings')

        # Thiết lập tiêu đề và chiều rộng cho các cột
        for column in data.columns:
            tree.heading(column, text=column)
            tree.column(column, width=100)  # Điều chỉnh chiều rộng cột tùy ý

        # Thêm dữ liệu vào Treeview
        for row in data.itertuples(index=False):
            tree.insert('', 'end', values=row)

        # Thanh kéo ngang
        h_scrollbar = Scrollbar(frame, orient="horizontal", command=tree.xview)
        h_scrollbar.pack(side='bottom', fill='x')
        tree.configure(xscrollcommand=h_scrollbar.set)

        # Thanh kéo dọc
        v_scrollbar = Scrollbar(frame, orient="vertical", command=tree.yview)
        v_scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=v_scrollbar.set)

        # Đặt Treeview vào frame
        tree.pack(expand=True, fill='both')

    def step_read_data(self):
                if os.path.exists('data/cleaned_data.csv'):
                    self.data = pd.read_csv('data/cleaned_data.csv')
                else:
                    self.data = read_data(self.input_file)
                    self.data.to_csv('data/khaosat.csv', index=False)
                self.show_data_in_table(self.data, "Step 1: Read Data")

    def step_clean_data(self):
                if os.path.exists('data/cleaned_data.csv'):
                    self.data = pd.read_csv('data/cleaned_data.csv')
                else:
                    cleaned_file = clean_data(self.data)
                    self.data = pd.read_csv(cleaned_file)
                    self.data.to_csv('data/cleaned_data.csv', index=False)
                self.show_data_in_table(self.data, "Step 2: Clean Data")

    def step_normalize_text(self):
                # Nếu self.data là None, đọc từ cleaned_data.csv
                if self.data is None and os.path.exists('data/cleaned_data.csv'):
                    self.data = pd.read_csv('data/cleaned_data.csv')
                
                # Kiểm tra nếu self.data vẫn None sau khi kiểm tra
                if self.data is not None:
                    # Sử dụng cleaned_data.csv làm input_file để chuẩn hóa
                    normalized_file = normalize_text('data/cleaned_data.csv')
                    
                    # Đọc file normalized_data.csv để hiển thị
                    normalized_data = pd.read_csv(normalized_file)
                    self.show_data_in_table(normalized_data, "Step 3: Normalize Text")
                else:
                    print("Data not available. Please run 'Read Data' and 'Clean Data' steps first.")
    def step_tokenize_text(self):
        # Kiểm tra nếu file tokenized_data.csv đã tồn tại
        if os.path.exists('data/tokenized_data.csv'):
            self.data = pd.read_csv('data/tokenized_data.csv')
        else:
            # Đọc dữ liệu từ bước 3 - normalized_data.csv
            self.data = pd.read_csv('data/normalized_data.csv')
            
            # Gọi hàm tokenize_text để xử lý tokenization
            tokenized_file = tokenize_text('data/normalized_data.csv')
            
            # Đọc lại dữ liệu tokenized
            self.data = pd.read_csv(tokenized_file)
        
        # Hiển thị dữ liệu trong bảng
        self.show_data_in_table(self.data, "Step 4: Tokenize Text")

    def step_label_data(self):
        # Kiểm tra xem tệp đã tồn tại chưa
        if os.path.exists('data/labeled_data.csv'):
            self.data = pd.read_csv('data/labeled_data.csv')  # Đọc dữ liệu từ tệp đã có
        else:
            # Gọi hàm label_data với tệp đầu vào đúng
            self.data = label_data('data/tokenized_data.csv')  # Sử dụng tệp CSV chứa dữ liệu đã được token hóa
            self.data.to_csv('data/labeled_data.csv', index=False)
        
        self.show_data_in_table(self.data, "Step 5: Label Data")

    def step_vectorize_text(self):
    # Kiểm tra xem tệp đã tồn tại chưa
        if os.path.exists('data/vectorized_data.csv'):
            self.data = pd.read_csv('data/vectorized_data.csv')  # Đọc dữ liệu từ tệp đã có
        else:
            # Gọi hàm vectorize_text với tệp đầu vào đúng
            self.data = vectorize_text('data/labeled_data.csv')  # Sử dụng tệp CSV chứa dữ liệu đã được gán nhãn
            self.data.to_csv('data/vectorized_data.csv', index=False)

        self.show_data_in_table(self.data, "Step 6: Vectorize Text")
    def step_handle_missing_noise(self):
        # Kiểm tra nếu self.data là None, đọc từ tệp vectorized_data.csv
        if self.data is None and os.path.exists('data/vectorized_data.csv'):
            self.data = pd.read_csv('data/vectorized_data.csv')

        if self.data is not None:
            # Lọc dữ liệu
            filtered_data, noise_count, missing_count = handle_missing_noise(self.data)

            # Lưu dữ liệu đã lọc vào tệp
            filtered_data.to_csv('data/filtered_data.csv', index=False)

            # Tạo một DataFrame cho thông tin số lượng đã loại bỏ
            summary_data = pd.DataFrame({
                'Dữ liệu đã loại bỏ': ['Nhiễu', 'Mất mát'],
                'Số lượng': [noise_count, missing_count]
            })

            # Lưu tệp thông tin số lượng
            summary_data.to_csv('data/data_summary.csv', index=False)

            # Cập nhật self.data để hiển thị dữ liệu đã lọc
            self.data = filtered_data

            self.show_data_in_table(self.data, "Step 7: Filtered Data")
        else:
            print("Data not available. Please run previous steps first.")

    def step_split_data(self):
        # Kiểm tra xem file đã tồn tại chưa
        if os.path.exists('data/train_data.csv') and os.path.exists('data/test_data.csv'):
            # Đọc dữ liệu từ các file train và test
            train_data = pd.read_csv('data/train_data.csv')
            test_data = pd.read_csv('data/test_data.csv')
        else:
            # Nếu chưa tồn tại, gọi hàm split_data để chia dữ liệu
            train_file, test_file = split_data("data/filtered_data.csv")
            train_data = pd.read_csv(train_file)
            test_data = pd.read_csv(test_file)

            # Lưu các dữ liệu train và test vào file
            train_data.to_csv('data/train_data.csv', index=False)
            test_data.to_csv('data/test_data.csv', index=False)

        # Hiển thị dữ liệu trong bảng
        self.show_data_in_table(train_data, "Step 8: Train Data")
        self.show_data_in_table(test_data, "Step 8: Test Data")
      

    def step_augment_data(self):
        # Kiểm tra xem file augmented_data.csv đã tồn tại chưa
        if os.path.exists('data/augmented_data.csv'):
            self.data = pd.read_csv('data/augmented_data.csv')  # Đọc dữ liệu từ file đã có
        else:
            if self.data is None:
                # Nếu self.data chưa được khởi tạo, đọc dữ liệu từ labeled_data.csv
                if os.path.exists('data/labeled_data.csv'):
                    self.data = pd.read_csv('data/labeled_data.csv')
                else:
                    print("Labeled data not found. Please run 'Label Data' step first.")
                    return
            
            # Gọi hàm augment_data để mở rộng dữ liệu
            augmented_data = augment_data(self.data)  
            augmented_data.to_csv('data/augmented_data.csv', index=False)  # Lưu dữ liệu đã mở rộng vào file

            # Cập nhật self.data để hiển thị dữ liệu đã mở rộng
            self.data = augmented_data  

        # Hiển thị dữ liệu đã mở rộng
        self.show_data_in_table(self.data, "Step 9: Data Augmentation")


if __name__ == "__main__":
    root = Tk()
    app = DataPipelineApp(root)
    root.mainloop()
