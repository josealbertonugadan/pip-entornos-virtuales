import requests


def get_categories():
    """
    Fetches categories from the API and prints the response details.

    It prints the HTTP status code, the response text, and the type of the response text.
    Finally, it parses the JSON response and prints the name of each category.

    Args:
        None

    Returns:
        None
    """
    response = requests.get("https://api.escuelajs.co/api/v1/categories", timeout=100)
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    categories = response.json()
    for category in categories:
        print(category["name"])
