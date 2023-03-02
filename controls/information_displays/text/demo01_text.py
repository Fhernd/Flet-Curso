import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Text Custom Styles'
    page.scroll = 'adaptive'

    textos = []

    lbl_texto = Text('Size 10', size=10)
    textos.append(lbl_texto)

    lbl_texto = Text('Size 20, italic', size=20, color='pink600', italic=True)
    textos.append(lbl_texto)

    lbl_texto = Text('Size 40, w100', size=40, color=colors.WHITE, weight=FontWeight.W_100, bgcolor=colors.BLUE_600)
    textos.append(lbl_texto)

    lbl_texto = Text('Size 50, Normal', size=50, color=colors.WHITE, weight=FontWeight.NORMAL, bgcolor=colors.ORANGE_800)
    textos.append(lbl_texto)

    lbl_texto = Text('Size 60, w900', size=60, color=colors.WHITE, weight=FontWeight.BOLD, bgcolor=colors.PURPLE_900)
    textos.append(lbl_texto)

    lbl_texto = Text('Size 70, w900, selectable', size=70, color=colors.WHITE, weight=FontWeight.W_900, selectable=True)
    textos.append(lbl_texto)

    lbl_texto = Text('Limit long text to 1 line with ellipsis', style=TextThemeStyle.HEADLINE_SMALL)
    textos.append(lbl_texto)

    lbl_texto = Text(
            "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
            max_lines=1,
            overflow="ellipsis",
        )
    textos.append(lbl_texto)

    lbl_texto = Text("Limit long text to 2 lines and fading", style=TextThemeStyle.HEADLINE_SMALL)
    textos.append(lbl_texto)

    lbl_texto = Text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.",
            max_lines=2,
    )
    textos.append(lbl_texto)

    lbl_texto = Text("Limit the width and height of long text", style=TextThemeStyle.HEADLINE_SMALL)
    textos.append(lbl_texto)

    lbl_texto = Text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.",
            width=700,
            height=100,
    )
    textos.append(lbl_texto)

    page.add(*textos)


if __name__ == '__main__':
    flt.app(target=main)
