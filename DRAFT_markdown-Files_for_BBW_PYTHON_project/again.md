# **Python Application Proposal: Bath & Body Works Candle Tracker**

### **Application Overview**
This Python application is designed for Bath & Body Works customers to log, track, and organize their favorite fragrances by year, season, and special occasions. Users can create personalized shopping lists linked to birthdays, holidays, and events. The application will feature a  **command-line interface (CLI)**  with a focus on simplicity and functionality. It will allow users to manage their candle collections, set reminders, and organize data efficiently.

----------

### **Core Functionalities**

1.  **Candle Collection Management**:
    
    -   Add, update, or remove candles from a personal collection.
        
    -   Organize candles by year, season, and scent.
        
    -   Assign statuses to candles (e.g., “SHOPPING LIST,” “I Have Not Smelled,” “I Like This One”).
        
2.  **Shopping List Creation**:
    
    -   Create and manage shopping lists for birthdays, holidays, and special occasions.
        
    -   Organize shopping lists by week, day, and year.
        
    -   Save and retrieve shopping lists using JSON files.
        
3.  **Data Organization**:
    
    -   Organize data by year and month (e.g., 2025 → JANUARY → Day 01).
        
    -   Include user details such as name (last, first), month, day, and year.
        
4.  **Birthday Computation**:
    
    -   Calculate age and days until the next birthday using formulas.
        
    -   Display age and birthday reminders for each user.
        
5.  **User Prompts**:
    
    -   Create, edit, or view shopping lists.
        
    -   Open saved lists by year (dropdown-style selection).
        
    -   Confirm updates and prompt users to save changes before exiting.
        
6.  **Notifications**:
    
    -   Send reminders via email or phone for upcoming birthdays or events.
        

----------

### **System Architecture**

The application will be built using  **object-oriented programming (OOP)**  principles and will include the following components:

#### **Classes**

1.  **`Candle`**:
    
    -   Attributes:  `name`,  `scent`,  `season`,  `year`,  `status`  (e.g., “SHOPPING LIST,” “I Like This One”).
        
    -   Methods:  `update_status()`,  `display_details()`.
        
2.  **`User`**:
    
    -   Attributes:  `first_name`,  `last_name`,  `birthday`  (month, day, year).
        
    -   Methods:  `calculate_age()`,  `days_until_birthday()`.
        
3.  **`ShoppingList`**:
    
    -   Attributes:  `year`,  `month`,  `day`,  `candles`  (list of  `Candle`  objects).
        
    -   Methods:  `add_candle()`,  `remove_candle()`,  `save_to_file()`,  `load_from_file()`.
        

#### **Data Management**

-   Data will be stored in  **JSON files**  for persistence.
    
-   Example JSON structure:
    
    json
    
    Copy
    
    {
      "2025": {
        "JANUARY": {
          "01": {
            "name": "Doe, John",
            "age": 30,
            "candles": [
              {"name": "Vanilla Bean", "scent": "Vanilla", "status": "SHOPPING LIST"},
              {"name": "Fresh Linen", "scent": "Clean", "status": "I Like This One"}
            ]
          }
        }
      }
    }
    

----------

### **User Interaction Flow**

1.  **Main Menu**:
    
    -   Options: Create Shopping List, Open Shopping List, Edit Shopping List, Exit.
        
    -   Example:
        
        Copy
        
        Welcome to Bath & Body Works Candle Tracker!
        1. Create Shopping List
        2. Open Shopping List
        3. Edit Shopping List
        4. Exit
        
2.  **Create Shopping List**:
    
    -   Prompt user for year, month, day, and candle details.
        
    -   Save the list to a JSON file.
        
3.  **Open Shopping List**:
    
    -   Display available years and months.
        
    -   Allow users to select a list to view or edit.
        
4.  **Edit Shopping List**:
    
    -   Add, remove, or update candles.
        
    -   Assign statuses to candles.
        
5.  **Exit**:
    
    -   Prompt users to save changes before exiting.
        

----------

### **Technical Requirements**

1.  **Programming Language**: Python 3.x.
    
2.  **Libraries**:
    
    -   `json`  for data storage and retrieval.
        
    -   `datetime`  for birthday computations.
        
    -   `smtplib`  for email notifications (optional).
        
3.  **Data Structures**:
    
    -   Lists, dictionaries, and tuples for organizing data.
        
4.  **Error Handling**:
    
    -   Ensure the program runs without syntax or runtime errors.
        
    -   Validate user inputs (e.g., dates, names).
        

----------

### **Sample Output**

#### **Main Menu**

Copy

Welcome to Bath & Body Works Candle Tracker!
1. Create Shopping List
2. Open Shopping List
3. Edit Shopping List
4. Exit
Enter your choice: 1

#### **Create Shopping List**

Copy

Enter year: 2025
Enter month: JANUARY
Enter day: 01
Enter name (Last, First): Doe, John
Enter candle name: Vanilla Bean
Enter scent: Vanilla
Assign status (SHOPPING LIST, I Like This One, etc.): SHOPPING LIST
Candle added successfully!

#### **Open Shopping List**

Copy

Available years: 2025
Enter year: 2025
Available months: JANUARY
Enter month: JANUARY
Day 01:
- Name: Doe, John
- Age: 30
- Candles:
  1. Vanilla Bean (Vanilla) - SHOPPING LIST
  2. Fresh Linen (Clean) - I Like This One

----------

### **Documentation**

1.  **Proposal**: Detailed description of the application and its functionalities.
    
2.  **Class Diagram**: Visual representation of classes and their relationships.
    
3.  **Report**: Sample outputs and test cases demonstrating the application’s functionality.
    

----------

### **Inspiration**

The application is inspired by a 3-inch binder system used to organize greeting cards, photos, and personal items by month and year. It combines elements of a calendar, reminder service, and gift list organizer, tailored for Bath & Body Works customers.

> Written with [StackEdit](https://stackedit.io/).
