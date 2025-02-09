import json
import os

DATA_FILE = "fragrance_data.json"


# Load existing data or create a new structure
def load_data():
    return (
        json.load(open(DATA_FILE))
        if os.path.exists(DATA_FILE)
        else {"fragrances": {}, "shopping_lists": {}}
    )


# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Add a fragrance
def add_fragrance(name, year, season, status):
    data = load_data()
    data["fragrances"].setdefault(year, {}).setdefault(season, {})[name] = status
    save_data(data)
    print(f"Added: {name} ({status}) to {year} - {season}")


# Create shopping list
def create_shopping_list(name):
    data = load_data()
    data["shopping_lists"][name] = []
    save_data(data)
    print(f"Shopping list '{name}' created.")


# Add to shopping list
def add_to_shopping_list(list_name, fragrance):
    data = load_data()
    if list_name not in data["shopping_lists"]:
        print("List not found! Create it first.")
        return
    data["shopping_lists"][list_name].append(fragrance)
    save_data(data)
    print(f"Added '{fragrance}' to '{list_name}'.")


# View stored data
def display_data():
    data = load_data()
    print(json.dumps(data, indent=4))
