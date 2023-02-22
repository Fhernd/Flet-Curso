import flet as flt
from flet import alignment, colors, CircleAvatar, Container, Page, Stack

def main(page: Page):
    stack = Stack(
        [
            CircleAvatar(
                foreground_image_url="https://avatars.githubusercontent.com/u/1562371?v=4"
            ),
            Container(
                content=CircleAvatar(bgcolor=colors.GREEN, radius=5),
                alignment=alignment.bottom_left
            ),
        ],
        width=40,
        height=40,
    )

    page.add(stack)


if __name__ == '__main__':
    flt.app(target=main)
