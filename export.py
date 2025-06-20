import os
import shutil
import pandas as pd
import config
from db_utils import load_data

def export_single_field(field, values, output_dir, split):
    """
    """
    df = load_data()
    img_dir = config.IMG_DIR
    if 'ALL' not in values:
        values = [str(v) for v in values]
        df = df[df[field].astype(str).isin(values)]
    if split and 'ALL' not in values:
        for v in values:
            v_dir = os.path.join(output_dir, str(v))
            os.makedirs(v_dir, exist_ok=True)
            for _, row in df[df[field].astype(str) == str(v)].iterrows():
                src = os.path.join(img_dir, row['NAME'])
                dst = os.path.join(v_dir, row['NAME'])
                if os.path.exists(src):
                    shutil.copy2(src, dst)
        print(f'已按{field}分装导出到 {output_dir}')
    else:
        os.makedirs(output_dir, exist_ok=True)
        for _, row in df.iterrows():
            src = os.path.join(img_dir, row['NAME'])
            dst = os.path.join(output_dir, row['NAME'])
            if os.path.exists(src):
                shutil.copy2(src, dst)
        print(f'已全部导出到 {output_dir}')


def export_multi_field(fields, values_list, output_dir):
    """
    """
    df = load_data()
    img_dir = config.IMG_DIR
    for field, values in zip(fields, values_list):
        if 'ALL' not in values:
            values = [str(v) for v in values]
            df = df[df[field].astype(str).isin(values)]
    os.makedirs(output_dir, exist_ok=True)
    for _, row in df.iterrows():
        src = os.path.join(img_dir, row['NAME'])
        dst = os.path.join(output_dir, row['NAME'])
        if os.path.exists(src):
            shutil.copy2(src, dst)
    print(f'多字段筛选已导出到 {output_dir}')