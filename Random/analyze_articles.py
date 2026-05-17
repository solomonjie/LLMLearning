import pandas as pd
import os

# 读取Excel文件
file_path = os.path.join(os.path.dirname(__file__), 'data', '文章整理.xlsx')

print("正在读取Excel文件...")
try:
    # 读取所有工作表
    excel_file = pd.ExcelFile(file_path)
    print(f"\n文件中的工作表: {excel_file.sheet_names}")
    
    # 读取第一个工作表
    df = pd.read_excel(file_path, sheet_name=0)
    
    print(f"\n数据形状: {df.shape}")
    print(f"\n列名: {list(df.columns)}")
    print(f"\n前5行数据:")
    print(df.head())
    
    print(f"\n数据类型:")
    print(df.dtypes)
    
    print(f"\n基本统计信息:")
    print(df.describe(include='all'))
    
    # 保存一些基本信息
    df.info()
    
except Exception as e:
    print(f"读取文件时出错: {e}")