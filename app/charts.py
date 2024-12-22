import matplotlib.pyplot as plt


def generate_bar_chart(chart_name, bar_labels, bar_values):
    """
    Generates a bar chart and saves it as a PNG file.

    Args:
        chart_name (str): The name of the chart file to be saved.
        bar_labels (list): A list of labels for the bars.
        bar_values (list): A list of values for the bars.
    """
    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(bar_labels, bar_values)
    plt.savefig(f"./imgs/{chart_name}.png")
    plt.close()


def generate_pie_chart(pie_labels, pie_values):
    """
    Generates a pie chart and saves it as a PNG file.

    Args:
        pie_labels (list): A list of labels for the pie slices.
        pie_values (list): A list of values for the pie slices.
    """
    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.pie(pie_values, labels=pie_labels)
    ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [10, 40, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
