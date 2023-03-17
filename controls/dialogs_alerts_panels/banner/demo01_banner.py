import flet as flt
from flet import *


def main(page: Page):
    page.title = "Banner"

    def banner_closed(event):
        page.banner.open = False
        page.update()
    

    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
        content=Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
        ),
        actions=[
            TextButton("Retry", on_click=banner_closed),
            TextButton("Ignore", on_click=banner_closed),
            TextButton("Cancel", on_click=banner_closed),
        ]
    )

    def btn_show_banner_clicked(event):
        page.banner.open = True
        page.update()
    

    page.add(
        ElevatedButton(
            "Show Banner",
            on_click=btn_show_banner_clicked,
        )
    )


if __name__ == "__main__":
    flt.app(target=main)
