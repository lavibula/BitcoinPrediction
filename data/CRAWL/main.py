import pandas as pd

# Khởi tạo dataframe trống
merged_df = pd.DataFrame()

# Đọc và merge các file Excel
for i in range(1, 19):
    filename = f"CRAWL/data/data{i}.xlsx"  # tên file Excel
    df = pd.read_excel(filename)
    df = df.rename(columns={"time": "time{i}"})
    df = df.drop(columns=['t'])
    
    if merged_df.empty:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df, on='time{i}', how='outer')

# Loại bỏ các cột trùng lặp (nếu có)

# Lưu kết quả vào file Excel
merged_df.to_excel("merged_data.xlsx", index=False)
print(merged_df.head())