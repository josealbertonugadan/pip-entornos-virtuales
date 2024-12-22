import matplotlib.pyplot as plt


def generate_pie_chart():
    """
    Generates a pie chart with predefined labels and values, and saves it as a PNG file.

    This function creates a pie chart using the labels ["A", "B", "C"] and the corresponding
    values [200, 34, 120].
    The generated pie chart is saved as "pie.png" in the current directory.

    Args:
        None

    Returns:
        None
    """
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
