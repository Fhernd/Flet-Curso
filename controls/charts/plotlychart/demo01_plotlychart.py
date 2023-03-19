import plotly.express as px

import flet as flt
from flet import *

from flet.plotly_chart import PlotlyChart


def main(page: Page):
    page.title = "Plotly Chart Demo"

    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')

    page.add(PlotlyChart(fig, expand=True))


if __name__ == "__main__":
    flt.app(target=main)
