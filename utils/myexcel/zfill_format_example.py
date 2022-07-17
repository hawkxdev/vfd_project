# https://groups.google.com/g/python-excel/c/GMZMQu1NZt8

import xlrd


def zfill_format(fname):
    book = xlrd.open_workbook(fname, formatting_info=True)
    sheet = book.sheet_by_index(0)
    for rowx in range(sheet.nrows):
        for colx in range(sheet.ncols):
            cell = sheet.cell(rowx, colx)
            xf = book.xf_list[cell.xf_index]
            format = book.format_map[xf.format_key]
            format_str = format.format_str
            print('rowx=%d colx=%d ctype=%d xfx=%d s_value=%s fmt=%s'
                  % (rowx, colx, cell.ctype, cell.xf_index, str(cell.value), format_str))
            if cell.ctype == xlrd.XL_CELL_NUMBER and all(x == '0' for x in format_str):
                print(' looks like %0*d' % (len(format_str), int(cell.value)))


fileName = '!Номенклатура.xls'
filepath = f'D:\\Share\\{fileName}'

if __name__ == '__main__':
    zfill_format(filepath)
