import matplotlib.pyplot as plt


def generate_pie_chart():
    """Crea una gráfico de pastel"""
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
