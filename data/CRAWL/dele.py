import pandas as pd

df = pd.read_excel('Bản sao merged_data.xlsx', sheet_name='Sheet1')
df = df.query('(index < 27) or ((index >= 27) and ((index - 24) % 24 == 1)) or (index > 110331)')

# Ghi DataFrame vào file Excel mới
df.to_excel('1file_moi.xlsx', index=False)
