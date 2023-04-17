import pandas as pd

# Khởi tạo dataframe trống
merged_df = pd.DataFrame()

# Đọc và merge các file Excel
data_excel = pd.read_excel("working/Data_working.xlsx")

# Chuyển đổi sang định dạng CSV và lưu vào tệp mới
data_excel.to_csv("working/Data_working.csv", index=False)