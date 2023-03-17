import flet as flt
from flet import *


def main(page: Page):
    page.title = "Bottom Sheet"

    def bottom_sheet_closed(event):
        print('bottom_sheet_closed')
    
    def show_bs(event):
        bst_principal.open = True
        page.update()
    
    def close_bs(event):
        bst_principal.open = False
        page.update()
    

    bst_principal = BottomSheet(
        Container(
            Column([
                Text("This is sheet's content"),
                ElevatedButton("Close bottom sheet", on_click=close_bs)
            ],
            tight=True,),
        padding=10
        ),
        open=True,
        on_dismiss=bottom_sheet_closed
    )

    page.overlay.append(bst_principal)

    page.add(ElevatedButton("Display bottom sheet", on_click=show_bs))


if __name__ == "__main__":
    flt.app(target=main)
