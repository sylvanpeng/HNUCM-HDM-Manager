import pandas as pd
from config import CSV_PATH, DEFAULT_FIELDS

def load_data():
    try:
        df = pd.read_csv(CSV_PATH, encoding='utf-8-sig')
    except FileNotFoundError:
        df = pd.DataFrame(columns=DEFAULT_FIELDS)
    return df

def save_data(df):
    df.to_csv(CSV_PATH, index=False, encoding='utf-8-sig') 