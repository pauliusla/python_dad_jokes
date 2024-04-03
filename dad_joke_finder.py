from requests import get
from random import choice
from pyfiglet import figlet_format
from termcolor import colored


def get_dad_jokes(term):
    url = "https://icanhazdadjoke.com/search"

    response = get(
        url, headers={"Accept": "application/json"}, params={"term": term})

    return response.json()


def get_joke_topic():
    searh_term = input("Enter dad joke topic: ")

    while not searh_term:
        searh_term = input("You have to provide a topic")

    return searh_term


def get_random_joke(jokes):
    if not jokes:
        return None

    return choice(jokes)


def display_joke(joke, num_jokes):
    if not len(jokes["results"]):
        print("No jokes were found")
    else:
        print(f"I found {num_jokes} jokes for You, this is the best one:")
        print(random_joke["joke"])


ascii_art = figlet_format("DAD JOKE 3000")
colored_ascii = colored(ascii_art, "blue")
print(colored_ascii)

search_term = get_joke_topic()
jokes = get_dad_jokes(search_term)
random_joke = get_random_joke(jokes["results"])
num_jokes = len(jokes["results"])

display_joke(random_joke, num_jokes)
