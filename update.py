from db_utils import load_data, save_data

def update_data(field, value, filter_expr):
    df = load_data()
    if filter_expr:
        df.loc[df.eval(filter_expr), field] = value
    else:
        df[field] = value
    save_data(df)
    print(f'已更新字段 {field}') 