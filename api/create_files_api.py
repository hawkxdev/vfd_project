import numpy as np
from xlsxwriter.utility import xl_col_to_name
from api.vfd_api import series_power_list, get_supplier, get_series, get_vfd_by_params, get_price_vfd
from utils.different import img_resize
from utils.files import file_name_with_ext
from utils.myexcel.myxls import Xlsx
from vfd.models import Series


class ComparisonZone:
    def __init__(self):
        self.suppliers = None


class Block:
    def __init__(self, series):
        self.series = series
        self.price_col = []


def column_by_n(n):
    return 6 * (n + 1)


def create_compare_price():
    comparison_zone = ComparisonZone()

    # comparison_zone.suppliers = [3, 4, 5]
    # comparison_zone.blocks = [
    #     Block((9, 11, 13)),
    #     Block((9, None, 14)),
    #     Block((7, 11, 13)),
    #     Block((7, None, 14)),
    #     Block((7, 12, 15)),
    #     Block((6, 12, 15)),
    #     Block((8, 12, 15)),
    # ]

    comparison_zone.suppliers = [9, 6, 8]
    comparison_zone.blocks = [
        Block((29, 19, 24)),
    ]

    eur_rub = 59.81
    eur_usd = 1.00
    usd_rub = 59.84

    xlsx = Xlsx('upload/compare.xlsx', overwrite=True)
    row = 1

    for i, supplier_id in enumerate(comparison_zone.suppliers):
        supplier = get_supplier(supplier_id)
        xlsx.ws.cell(row=row, column=column_by_n(i)).value = supplier.name

    row += 1

    for i, block in enumerate(comparison_zone.blocks):
        power_list = []
        for series_id in block.series:
            if series_id:
                power_list += series_power_list(series_id)
        power_list = set(power_list)
        power_list = sorted(power_list, key=lambda x: (x[1], x[0]))

        print(f'block{i + 1} power_list:')
        for x in power_list:
            print(x)
        print()

        row_p = row + 1
        for power in power_list:
            xlsx.ws.cell(row=row_p, column=1).value = power[0]
            xlsx.ws.cell(row=row_p, column=2).value = power[1]
            row_p += 1

        for j, series_id in enumerate(block.series):
            if series_id:
                series = get_series(series_id)
                xlsx.ws.cell(row=row, column=column_by_n(j)).value = f'{series.brand} {series.name}'

                supplier = get_supplier(comparison_zone.suppliers[j])
                currency = supplier.currency
                xlsx.ws.cell(row=row, column=column_by_n(j) + 2).value = currency

                # if currency != 'EUR':
                #     block.price_col.append(column_by_n(j) + 3)
                # else:
                #     block.price_col.append(column_by_n(j) + 2)

                if currency != 'USD':
                    block.price_col.append(column_by_n(j) + 3)
                else:
                    block.price_col.append(column_by_n(j) + 2)

                row_s = row + 1
                for power in power_list:
                    power, voltage = power[0], power[1]
                    vfd = get_vfd_by_params(series, power, voltage)
                    if vfd:
                        xlsx.ws.cell(row=row_s, column=column_by_n(j)).value = vfd.article
                        xlsx.ws.cell(row=row_s, column=column_by_n(j) + 1).value = vfd.name

                        price = get_price_vfd(supplier, vfd)
                        col_r = None
                        if price:
                            price = price.price
                            price_val = price

                            # if currency == 'RUB':
                            #     price_val = round(price_val / eur_rub, 2)
                            # elif currency == 'USD':
                            #     price_val = round(price_val / eur_usd, 2)

                            if currency == 'RUB':
                                price_val = round(price_val / usd_rub, 2)
                            elif currency == 'EUR':
                                price_val = round(price_val * eur_usd, 2)

                            xlsx.ws.cell(row=row_s, column=column_by_n(j) + 2).value = price
                            col = xl_col_to_name(column_by_n(j) + 1)
                            xlsx.ws[f'{col}{row_s}'].number_format = '0.00'

                            col_r = column_by_n(j) + 2
                            if price != price_val:
                                col1 = xl_col_to_name(column_by_n(j) + 1)
                                col2 = xl_col_to_name(column_by_n(j) + 2)

                                # if currency == 'RUB':
                                #     xlsx.ws.cell(row=row_s, column=column_by_n(j) + 3) \
                                #         .value = f'={col1}{row_s}/{eur_rub}'
                                # elif currency == 'USD':
                                #     xlsx.ws.cell(row=row_s, column=column_by_n(j) + 3) \
                                #         .value = f'={col1}{row_s}/{eur_usd}'

                                if currency == 'RUB':
                                    xlsx.ws.cell(row=row_s, column=column_by_n(j) + 3) \
                                        .value = f'={col1}{row_s}/{usd_rub}'
                                elif currency == 'EUR':
                                    xlsx.ws.cell(row=row_s, column=column_by_n(j) + 3) \
                                        .value = f'={col1}{row_s}*{eur_usd}'

                                xlsx.ws[f'{col2}{row_s}'].number_format = '0.00'
                                col_r = column_by_n(j) + 3

                        if j != 0 and col_r:
                            col1 = xl_col_to_name(col_r - 1)
                            col2 = xl_col_to_name(block.price_col[0] - 1)
                            col = xl_col_to_name(col_r)
                            val_col2 = xlsx.ws[f'{col2}{row_s}'].value
                            if val_col2:
                                xlsx.ws.cell(row=row_s, column=col_r + 1).value = f'={col1}{row_s}/{col2}{row_s} - 1'
                                xlsx.ws[f'{col}{row_s}'].number_format = '0%'

                    row_s += 1

        row = row + len(power_list) + 2

    xlsx.width_auto() \
        .save_and_open()


def create_compare_series(series):
    print(f'{series = }')
    # series = ['15', '14']

    filename = 'upload/compare_series.xlsx'
    xlsx = Xlsx(filename, overwrite=True)

    xlsx.column_width(1, 42)
    xlsx.row_height(1, 70)

    arr = []

    for j, series_id in enumerate(series):
        col = j + 2
        ser = Series.objects.get(id=series_id)

        arr.append([])

        xlsx.column_width(col, 40)

        xlsx.ws.cell(row=1, column=col).value = f'{ser.brand.name} {ser.name}'
        xlsx.header_row_font(1)

        img_path = ser.image.path
        new_img_path = f'upload/temp/{file_name_with_ext(img_path)}'
        if img_resize(img_path=img_path, new_img_path=new_img_path, height=90):
            xlsx.img_to_cell(1, col, new_img_path, 3.8, 0.1)

        row = 2
        for field in Series._meta.get_fields():
            cell = xlsx.ws.cell(row=row, column=col)

            if field.name not in ['id', 'name', 'brand', 'frequencydrive', 'accessory', 'image', 'applications',
                                  'description']:
                xlsx.cell_alignment(row, col, horizontal='left', vertical='top', wrap_text=True)
                xlsx.cell_alignment(row, 1, horizontal='left', vertical='top', wrap_text=True)

                xlsx.ws.cell(row=row, column=1).value = field.verbose_name
                xlsx.cell_bold(row, 1)
                # xlsx.ws.cell(row=row, column=4).value = field.name

                value = getattr(ser, field.name, None)

                if value is None:
                    cell.value = 'Нет информации'
                    arr[j].append(0)
                else:
                    if field.name == 'category':
                        cell.value = ser.category.name
                    else:
                        if field.choices:
                            filtered = list(filter(lambda x: x[0] == value, field.choices))
                            label = filtered[0][1]
                            cell.value = label
                            if value < 10:
                                arr[j].append(int(value))
                            else:
                                arr[j].append(int(value / 10))
                        else:
                            if value in [True, False]:
                                cell.value = 'Да' if value else 'Нет'
                                arr[j].append(1 if value else 0)
                            else:
                                cell.value = value
                                arr[j].append(0)
                    # elif field.name == 'applications':
                    #     s = ', '.join(list(ser.applications.values_list('name', flat=True)))
                    #     cell.value = s
                row += 1

    print(arr)
    arr = np.array(arr)
    print(arr)
    arr = np.swapaxes(arr, 0, 1)
    # print(arr, np.size(arr, 0))

    cols_rating = []

    for row, x in enumerate(arr):
        average = sum(x) / len(x)
        for col, y in enumerate(x):
            if y > average:
                xlsx.cell_background(row + 3, col + 2, 'LightGreen')
                cols_rating.append(col + 2)

    unique_cols = list(set(cols_rating))
    col_counts_in_rating = []

    for col in unique_cols:
        count = len(list(filter(lambda k: k == col, cols_rating)))
        col_counts_in_rating.append(count)

    max_count = max(col_counts_in_rating)
    for i, col in enumerate(unique_cols):
        if col_counts_in_rating[i] == max_count:
            xlsx.cell_background(1, col, 'LightGreen')

    xlsx.save()
    return filename
