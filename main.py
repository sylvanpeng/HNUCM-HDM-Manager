import argparse
from add import add_data
from update import update_data
from export import export_data, export_by_years, export_single_field, export_multi_field

def main():
    parser = argparse.ArgumentParser(description='CSV数据集管理工具')
    subparsers = parser.add_subparsers(dest='command')

    # 添加
    parser_add = subparsers.add_parser('add', help='添加新数据')
    parser_add.add_argument('--input', required=True, help='输入csv文件路径')

    # 更新
    parser_update = subparsers.add_parser('update', help='更新数据字段')
    parser_update.add_argument('--field', required=True, help='要更新的字段')
    parser_update.add_argument('--value', required=True, help='新值')
    parser_update.add_argument('--filter', help='筛选条件（如 gt=="HE195"）')

    # 导出
    parser_export = subparsers.add_parser('export', help='导出数据')
    parser_export.add_argument('--filter', help='筛选条件（如 gt=="HE195"）')
    parser_export.add_argument('--output', required=True, help='导出文件路径')

    # 按年份导出图片
    parser_export_years = subparsers.add_parser('export_years', help='按年份导出图片')
    parser_export_years.add_argument('--img_dir', required=True, help='图片存放目录')
    parser_export_years.add_argument('--years', required=True, nargs='+', help='年份列表，如 2022 2023 2024')
    parser_export_years.add_argument('--output_dir', required=True, help='导出目标文件夹')
    parser_export_years.add_argument('--split', action='store_true', help='是否按年份分装')

    # 单字段导出
    parser_export_single = subparsers.add_parser('export_single', help='按单字段导出图片')
    parser_export_single.add_argument('--img_dir', required=True, help='图片存放目录')
    parser_export_single.add_argument('--field', required=True, help='字段名')
    parser_export_single.add_argument('--values', required=True, nargs='+', help='取值列表')
    parser_export_single.add_argument('--output_dir', required=True, help='导出目标文件夹')
    parser_export_single.add_argument('--split', action='store_true', help='是否拆分存储')

    # 多字段导出
    parser_export_multi = subparsers.add_parser('export_multi', help='按多字段导出图片')
    parser_export_multi.add_argument('--img_dir', required=True, help='图片存放目录')
    parser_export_multi.add_argument('--fields', required=True, nargs='+', help='字段名列表')
    parser_export_multi.add_argument('--values_list', required=True, nargs='+', help='每个字段的取值列表（逗号分隔）')
    parser_export_multi.add_argument('--output_dir', required=True, help='导出目标文件夹')

    args = parser.parse_args()

    if args.command == 'add':
        add_data(args.input)
    elif args.command == 'update':
        update_data(args.field, args.value, args.filter)
    elif args.command == 'export':
        export_data(args.filter, args.output)
    elif args.command == 'export_years':
        export_by_years(args.img_dir, args.years, args.output_dir, args.split)
    elif args.command == 'export_single':
        export_single_field(args.img_dir, args.field, args.values, args.output_dir, args.split)
    elif args.command == 'export_multi':
        values_list = [v.split(',') for v in args.values_list]
        export_multi_field(args.img_dir, args.fields, values_list, args.output_dir)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 