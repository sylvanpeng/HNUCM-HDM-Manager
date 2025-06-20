from db_utils import load_data, save_data
import pandas as pd

def add_data(input_path):
    df = load_data()
    new_data = pd.read_csv(input_path, encoding='utf-8-sig')
    # 自动生成IDs
    start_id = df['IDs'].max() + 1 if not df.empty else 1
    new_data['IDs'] = range(start_id, start_id + len(new_data))
    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df)
    print(f'已添加{len(new_data)}条数据') 