import flet as flt
from flet import *


def main(page: Page):
    dbl_demo = DataTable(
        columns=[
            DataColumn(Text('First name')),
            DataColumn(Text('Last name')),
            DataColumn(Text('Age'), numeric=True)
        ],
        rows= [
            DataRow(cells=[
                DataCell(Text('John')),
                DataCell(Text('Smith')),
                DataCell(Text('43'))
            ]),
            DataRow(cells=[
                DataCell(Text('Jack')),
                DataCell(Text('Brown')),
                DataCell(Text('19'))
            ]),
            DataRow(cells=[
                DataCell(Text('Alice')),
                DataCell(Text('Wong')),
                DataCell(Text('25'))
            ]),
    ])

    page.add(dbl_demo)


if __name__ == '__main__':
    flt.app(target=main)
