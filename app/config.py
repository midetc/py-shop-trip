import json


def load_config(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)
