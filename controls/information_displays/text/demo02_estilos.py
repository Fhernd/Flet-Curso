import flet as flt
from flet import *


def main(page: Page):
    page.title = 'Temas de Estilos de Texto - Ejemplo'
    page.scroll = 'adaptive'

    page.add(
        Text("Display Large", style=TextThemeStyle.DISPLAY_LARGE),
        Text("Display Medium", style=TextThemeStyle.DISPLAY_MEDIUM),
        Text("Display Small", style=TextThemeStyle.DISPLAY_SMALL),
        Text("Headline Large", style=TextThemeStyle.HEADLINE_LARGE),
        Text("Headline Medium", style=TextThemeStyle.HEADLINE_MEDIUM),
        Text("Headline Small", style=TextThemeStyle.HEADLINE_MEDIUM),
        Text("Title Large", style=TextThemeStyle.TITLE_LARGE),
        Text("Title Medium", style=TextThemeStyle.TITLE_MEDIUM),
        Text("Title Small", style=TextThemeStyle.TITLE_SMALL),
        Text("Label Large", style=TextThemeStyle.LABEL_LARGE),
        Text("Label Medium", style=TextThemeStyle.LABEL_MEDIUM),
        Text("Label Small", style=TextThemeStyle.LABEL_SMALL),
        Text("Body Large", style=TextThemeStyle.BODY_LARGE),
        Text("Body Medium", style=TextThemeStyle.BODY_MEDIUM),
        Text("Body Small", style=TextThemeStyle.BODY_SMALL),
    )


if __name__ == '__main__':
    flt.app(target=main)
