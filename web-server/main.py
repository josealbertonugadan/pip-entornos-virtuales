import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def get_numbers():
    """
    Returns a list of numbers.

    Returns:
        list: A list containing the numbers 1, 2, and 3.
    """
    return [1, 2, 3]


@app.get("/contact")
def get_contact():
    """
    Returns contact information in JSON format.

    Returns:
        dict: A dictionary containing the contact name.
    """
    return {"name": "Platzi"}


@app.get("/about", response_class=HTMLResponse)
def get_about():
    """
    Returns an HTML response with information about the page.

    Returns:
        str: An HTML string containing a heading and a paragraph.
    """
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """


def run():
    """
    Runs the application by fetching categories from the store.

    Returns:
        None
    """
    store.get_categories()


if __name__ == "__main__":
    run()
