Khristin Schenk
Feb 09th, 2025
SDEV-220: Module 3 Final Project Launch

# Module 3 Final Project Launch: *Python Program for Bath & Body Works*

### Introduction

This Python code is designed to manage information about fragrances and collections from Bath & Body Works. It offers a basic framework for organizing fragrance data, creating lists, and setting reminders. I plan to expand the program based on user feedback, new ideas, and any additional requirements that may come up.

---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Module 3 Final Project Launch: *Python Program for Bath & Body Works*](#module-3-final-project-launch-python-program-for-bath--body-works)
    - [Introduction](#introduction)
  - [**1. Setup the Project Structure**](#1-setup-the-project-structure)
  - [**2. Install Required Libraries**](#2-install-required-libraries)
  - [**3. Implement Core Features**](#3-implement-core-features)
      - [**3.2 Seasonal Organization**](#32-seasonal-organization)
      - [**3.3 Shopping List Integration**](#33-shopping-list-integration)
      - [**3.4 Reminder System**](#34-reminder-system)
      - [**3.5 Gift List Organizer**](#35-gift-list-organizer)
    - [**4. Main Application Loop**](#4-main-application-loop)
    - [**5. Enhancements**](#5-enhancements)
    - [**6. Running the Application**](#6-running-the-application)

<!-- /code_chunk_output -->

---

## **1. Setup the Project Structure**

Create a project folder with the following structure:

```plaintext
bath_body_works_app/
│
├── data/                  # Folder to store JSON files
│   ├── fragrances.json    # Stores user's fragrance inventory
│   ├── shopping_lists.json # Stores shopping lists
│   └── events.json        # Stores events and reminders
│
├── main.py                # Main application script
└── utils.py               # Utility functions (e.g., file handling)
```

---

## **2. Install Required Libraries**

Ensure you have Python installed, and install the following libraries if needed:

```bash
pip install json datetime
```

---

## **3. Implement Core Features**

    - > TEXT HERE TEXT HERE TEXT HERE
    - > TEXT HERE TEXT HERE TEXT HERE

**3.1 Fragrance Collection Management**

Allow users to add fragrances to their inventory and categorize them by year and season.

```python
import json
from datetime import datetime

# File paths
FRAGRANCES_FILE = "data/fragrances.json"
SHOPPING_LISTS_FILE = "data/shopping_lists.json"
EVENTS_FILE = "data/events.json"

# Load data from JSON files
def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save data to JSON files
def save_data(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Add a fragrance to the inventory
def add_fragrance():
    name = input("Enter fragrance name: ")
    year = input("Enter year (e.g., 2023): ")
    season = input("Enter season (e.g., Winter, Spring, Summer, Fall): ")
    status = input("Enter status (e.g., SHOPPING LIST, I Have Not Smelled, I Like This One): ")

    fragrance = {
        "name": name,
        "year": year,
        "season": season,
        "status": status
    }

    fragrances = load_data(FRAGRANCES_FILE)
    fragrances[name] = fragrance
    save_data(fragrances, FRAGRANCES_FILE)
    print(f"Added '{name}' to your fragrance inventory!")
```

---

#### **3.2 Seasonal Organization**

Allow users to view fragrances by year and season.

```python
def view_fragrances_by_season(year, season):
    fragrances = load_data(FRAGRANCES_FILE)
    filtered_fragrances = [f for f in fragrances.values() if f["year"] == year and f["season"] == season]

    if filtered_fragrances:
        print(f"Fragrances for {season} {year}:")
        for fragrance in filtered_fragrances:
            print(f"- {fragrance['name']} ({fragrance['status']})")
    else:
        print(f"No fragrances found for {season} {year}.")
```

---

#### **3.3 Shopping List Integration**

Allow users to create shopping lists for events like birthdays and holidays.

```python
def create_shopping_list():
    event_name = input("Enter event name (e.g., Birthday, Christmas): ")
    date = input("Enter date (YYYY-MM-DD): ")
    fragrances = input("Enter fragrance names (comma-separated): ").split(",")

    shopping_list = {
        "event_name": event_name,
        "date": date,
        "fragrances": [f.strip() for f in fragrances]
    }

    shopping_lists = load_data(SHOPPING_LISTS_FILE)
    shopping_lists[event_name] = shopping_list
    save_data(shopping_lists, SHOPPING_LISTS_FILE)
    print(f"Created shopping list for '{event_name}'!")
```

---

#### **3.4 Reminder System**

Implement a simple reminder system using Python's `datetime` module.

```python
def check_reminders():
    today = datetime.today().strftime("%Y-%m-%d")
    shopping_lists = load_data(SHOPPING_LISTS_FILE)

    print("Today's reminders:")
    for event_name, event_details in shopping_lists.items():
        if event_details["date"] == today:
            print(f"- {event_name}: {', '.join(event_details['fragrances'])}")
```

---

#### **3.5 Gift List Organizer**

Organize gifts by year, scent, collection, season, and event.

```python
def view_gift_lists():
    fragrances = load_data(FRAGRANCES_FILE)
    shopping_lists = load_data(SHOPPING_LISTS_FILE)

    print("Gift Lists:")
    for event_name, event_details in shopping_lists.items():
        print(f"\nEvent: {event_name} (Date: {event_details['date']})")
        for fragrance_name in event_details["fragrances"]:
            fragrance = fragrances.get(fragrance_name, {})
            print(f"- {fragrance_name} ({fragrance.get('season', 'N/A')} {fragrance.get('year', 'N/A')})")
```

---

### **4. Main Application Loop**

Combine all features into a menu-driven application.

```python
def main():
    while True:
        print("\nBath & Body Works Fragrance Tracker")
        print("1. Add Fragrance")
        print("2. View Fragrances by Season")
        print("3. Create Shopping List")
        print("4. Check Reminders")
        print("5. View Gift Lists")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_fragrance()
        elif choice == "2":
            year = input("Enter year: ")
            season = input("Enter season: ")
            view_fragrances_by_season(year, season)
        elif choice == "3":
            create_shopping_list()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            view_gift_lists()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

---

### **5. Enhancements**

- **Push Notifications**: Use third-party APIs like Twilio for SMS or email reminders.
- **GUI**: Use `tkinter` or `PyQt` for a graphical user interface.
- **Data Analysis**: Add features to analyze spending or fragrance preferences over time.

---

### **6. Running the Application**

Run the `main.py` script to start the application:

```bash
python main.py
```
