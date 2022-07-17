from api.vfd_api import series_power_list
from utils.myexcel.myxls import Xlsx


class ComparisonZone:
    def __init__(self):
        self.suppliers = None


class Block:
    def __init__(self):
        self.suppliers = None


def create_compare_price():
    comparison_zone = ComparisonZone()
    comparison_zone.suppliers = [3, 4, 5]

    block1 = Block()
    block1.series = (9, 11, 13)

    block2 = Block()
    block2.series = (9, None, 14)

    comparison_zone.blocks = [block1, block2]

    xlsx = Xlsx('upload/compare.xlsx', overwrite=True)
    row = 1

    for i, block in enumerate(comparison_zone.blocks[:1]):
        power_list = []
        for series_id in block1.series:
            power_list += series_power_list(series_id)
        power_list = set(power_list)
        power_list = sorted(power_list, key=lambda x: (x[1], x[0]))

        print(f'block{i + 1} power_list:')
        for x in power_list:
            print(x)
        print()

        for power in power_list:
            xlsx.ws.cell(row=row, column=1).value = power[0]
            xlsx.ws.cell(row=row, column=2).value = power[1]
            row += 1

    xlsx.save_and_open()
