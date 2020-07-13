import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aopeng_sites.settings')

import django
if django.VERSION >= (1, 7):
    django.setup()

from op_xadmin.models import goods, orderInfo
import xlrd

def excel_table_by_name(file_excel='/home/zhumingzhu/django-test/aopeng_sites/07-02.xlsx',
                        col_name_index=0, by_name=u'07-02'):
    data = xlrd.open_workbook(file_excel)
    table = data.sheet_by_name(by_name)
    n_rows = table.nrows
    col_names = table.row_values(col_name_index)
    order_list = []
    for row_num in range(1, n_rows):
        row = table.row_values(row_num)
        new_order_unit = orderInfo(
            op_id = row[0],
            kayouli_id = row[1],
            factory_name = row[2],
            goods_name = row[3],
        )
        order_list.append(new_order_unit)
    goods.objects.bulk_create(order_list)

def main():
    excel_table_by_name()

if __name__ == "__main__":
    main()
    print('Done!')



