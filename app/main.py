import utils
import read_csv
import charts


def run():
    """
    Main function to run the population data analysis and visualization.

    This function reads population data from a CSV file, filters it for South American countries,
    generates a pie chart of the world population percentage for these countries, and then
    prompts the user to input a specific country to generate a bar chart of its population over
    the years.

    Steps:
        1. Reads data from 'data.csv'.
        2. Filters the data for countries in South America.
        3. Generates a pie chart of the world population percentage for South American countries.
        4. Prompts the user to input a country name.
        5. Filters the data for the specified country.
        6. If the country is found, generates a bar chart of its population over the years.

    Returns:
        None
    """
    data = read_csv.read_csv("data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))

    countries = list(map(lambda x: x["Country"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    charts.generate_pie_chart(countries, percentages)

    country = input("Type Country => ")
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country["Country"], labels, values)


if __name__ == "__main__":
    run()
