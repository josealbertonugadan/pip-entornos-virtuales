"""Módulo que genera distintos gráficos"""

import matplotlib.pyplot as plt


def generate_pie_chart():
    """Crea una gráfico de pastel"""
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
