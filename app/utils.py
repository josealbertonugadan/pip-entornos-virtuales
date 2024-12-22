def get_population(country_dict):
    """
    Extracts population data from a dictionary for specific years and returns the labels and values.

    Args:
        country_dict (dict): A dictionary containing population data for a country.
        The keys should be strings representing years (e.g., "2022 Population").

    Returns:
        tuple: A tuple containing two elements:
            - labels (dict_keys): The years for which population data is available.
            - values (dict_values): The population values corresponding to the years.
    """
    population_dict = {
        "2022": int(country_dict["2022 Population"]),
        "2020": int(country_dict["2020 Population"]),
        "2015": int(country_dict["2015 Population"]),
        "2010": int(country_dict["2010 Population"]),
        "2000": int(country_dict["2000 Population"]),
        "1990": int(country_dict["1990 Population"]),
        "1980": int(country_dict["1980 Population"]),
        "1970": int(country_dict["1970 Population"]),
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(data, country):
    """
    Filters the population data for a specific country.

    Args:
        data (list): A list of dictionaries containing population data for multiple countries.
        country (str): The name of the country to filter the data for.

    Returns:
        list: A list of dictionaries containing population data for the specified country.
    """
    result = list(filter(lambda item: item["Country"] == country, data))
    return result
