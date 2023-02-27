import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Data table styles'

    dbl_demo = DataTable(
        width=700,
        bgcolor='yellow',
        border=border.all(2, 'red'),
        border_radius=10,
        vertical_lines=border.BorderSide(3, 'blue'),
        horizontal_lines=border.BorderSide(1, 'blue'),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=colors.BLACK12,
        heading_row_height=100,
        data_row_color={'hovered': '0x30FF0000'},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            DataColumn(Text('Column 1'),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
            DataColumn(
                Text('Column 2'),
                tooltip='This is a second column',
                numeric=True,
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ],
        rows= [
            DataRow([
                DataCell(Text('A')), DataCell(Text('1'))],
                selected=True,
                on_select_changed=lambda e: print(f"row select changed: {e.data}")
            ),
            DataRow([
                DataCell(Text('B')), DataCell(Text('2'))
            ]),
        ]
    )

    page.add(dbl_demo)


if __name__ == '__main__':
    flt.app(target=main)
