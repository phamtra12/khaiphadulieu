import pandas as pd
import tkinter as tk
from tkinter import messagebox
import nltk

def handle_missing_noise(data):
    # Kiểm tra dữ liệu mất mát
    missing_data = data.isnull().sum()

    # Tạo chuỗi thông báo cho dữ liệu mất mát
    missing_info = "Số lượng dữ liệu mất mát trong mỗi cột:\n" + str(missing_data)

    # Giả sử cột 'Nhãn' là cột cần kiểm tra để xác định nhiễu
    noise_condition = data['Nhãn'].isna()  # Điều kiện cho dữ liệu bị nhiễu
    missing_condition = data.isnull().any(axis=1)  # Điều kiện cho dữ liệu mất mát

    # Đếm số lượng dữ liệu nhiễu và mất mát
    noise_count = data[noise_condition].shape[0]
    missing_count = data[missing_condition].shape[0]

    # Lọc dữ liệu
    filtered_data = data[~(noise_condition | missing_condition)]

    # Kiểm tra dữ liệu bị nhiễu (các từ không cần thiết)
    stop_words = set(nltk.corpus.stopwords.words('english'))

    # Loại bỏ các từ không cần thiết trong cột 'tokens'
    if 'tokens' in data.columns:
        data['tokens'] = data['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

    # Tạo thông điệp để hiển thị
    message = f"{missing_info}\nSố lượng dữ liệu nhiễu: {noise_count}\nSố lượng dữ liệu mất mát: {missing_count}"

    # Hiển thị thông điệp trong một cửa sổ
    show_message_box(message)

    return filtered_data, noise_count, missing_count

def show_message_box(message):
    # Tạo cửa sổ Tkinter
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính
    messagebox.showinfo("Thông tin dữ liệu", message)  # Hiển thị thông điệp
    root.destroy()  # Đóng cửa sổ sau khi hiển thị

