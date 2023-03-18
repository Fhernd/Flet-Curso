import matplotlib
import matplotlib.pyplot as plt

import flet as flt
from flet import *
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use('svg')


def main(page: Page):
    page.title = "Matplotlib Chart"

    fig, ax = plt.subplots()

    fruits = ['Apples', 'Bananas', 'Oranges', 'Pears']
    counts = [20, 4, 23, 17]

    bar_labels = ["red", "blue", "_red", "orange"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title="Fruit color")

    chart = MatplotlibChart(fig, expand=True)

    page.add(chart)


if __name__ == '__main__':
    flt.app(target=main)
