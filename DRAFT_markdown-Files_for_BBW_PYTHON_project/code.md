
A Python program for storing information about Bath & Body Works fragrances and collections.

### **Overview**
A Python application for organizing Bath & Body Works fragrances. Users must be able to create shopping lists linked to birthdays, holidays, and special occasions, organizing saved fragrances by week, day, and year.

### **Key Features**

- **Fragrance Collection Management:** Allows users to add fragrances to their personal inventory.

- **Seasonal Organization:** Categorizes fragrances by year and season.

- **Shopping List Integration:** Users can create lists for birthdays, holidays, and special events.

- **Status Labels:** Assign labels such as “SHOPPING LIST,” “I Have Not Smelled,” “I Like This One,” etc.

- **Data Storage & Retrieval:** Saves and accesses lists using JSON files.

- **Data Organization:** Structured based on Year and Month.

- **Calendar Function:** For tracking events and birthdays.

- **Reminder System:** Sends push notifications, emails, or texts.

- **Gift List Organizer:** Sorts gifts by year, scent, collection, season, and event.


## How to Run

### Prerequisites

- Before starting, ensure you have the following installed:

- Python (version 3.6 or higher)

- A code editor (such as Visual Studio Code, PyCharm, or any text editor of your choice)

- Required Python libraries:

- `.json` for data storage

- `datetime` for handling dates

- `tkinter` for creating a graphical user interface (GUI) (optional)

- `schedule` for reminders (optional)

You can install additional libraries using pip, for example:

```bash
pip install schedule
```

---

### Step 1: Project Structure

Create a project directory with the following structure:
```md
fragrance_app/
│
├── main.py # Main application script
├── fragrance.py # Module for handling fragrance data
├── reminder.py # Module for reminders
├── data/ # Directory for storing JSON files
│ ├── fragrances.json
│ └── shopping_lists.json
└── README.md # Readme file for documentation
```

### Step 2: Setting Up the JSON Data Storage

1. Create `fragrances.json` and `shopping_lists.json` in the `data/` directory.

2. Initialize these files with empty JSON objects `{}` for easier handling later.

### Step 3: Implementing the Fragrance Management

In `fragrance.py`, implement functions to:

- **Add Fragrances**: Functions to add fragrances to the personal inventory, including properties like name, scent, collection, and season.

- **Load and Save**: Functions that load and save fragrance data using JSON.

```python
import json
import os

DATA_FILE = 'data/fragrances.json'
def load_fragrances():
if os.path.exists(DATA_FILE):
with open(DATA_FILE, 'r') as file:
return json.load(file)
return {}
def save_fragrance(fragrance_data):
with open(DATA_FILE, 'w') as file:
json.dump(fragrance_data, file)
def add_fragrance(name, scent, collection, season):
fragrances = load_fragrances()
fragrances[name] = {'scent': scent, 'collection': collection, 'season': season}
save_fragrance(fragrances)
```

### Step 4: Shopping List Management

Extend `fragrance.py` to handle shopping lists:

- Create functions to add shopping lists linked to specific events (birthdays, holidays).

- Implement functions for status labels.

### Step 5: Implementing the Reminder System

In `reminder.py`, implement a simple reminder system using `schedule`:

- Function to send reminders for upcoming events.

- Integration with an email client or SMS API if needed.

```python
import schedule
import time
def remind_for_event(event):
print(f"Reminder: Don't forget the {event}!")
def schedule_reminder(event, time):
schedule.every().day.at(time).do(remind_for_event, event)

# Keep scheduler running
while True:
schedule.run_pending()
time.sleep(1)
```

### Step 6: Creating the User Interface

In `main.py`, create a basic user interface using `tkinter` (optional):

- Create forms for adding fragrances and shopping lists.

- Display a calendar for tracking events.

```python

import tkinter as tk
from fragrance import add_fragrance
def add_fragrance_gui():
# Implementation of GUI for adding a fragrance
pass # Create your form here
if __name__ == "__main__":
root = tk.Tk()
root.title("Fragrance Organizer")
# Add your GUI components here
root.mainloop()
```

### Step 7: Implementing the Calendar Functionality

Use a library like `tkcalendar` or create a simple view with `tkinter` for displaying and interacting with dates.

### Step 8: Testing the Application

- Test each feature thoroughly to ensure everything works as planned.

- Handle exceptions and validate user inputs.

### Step 9: Documentation

- Create a `README.md` file to document how to run the application and its features.

### Running the Application

To run the application, execute the `main.py` script:

```bash
python main.py
```

### Conclusion

😊 Happy coding!
