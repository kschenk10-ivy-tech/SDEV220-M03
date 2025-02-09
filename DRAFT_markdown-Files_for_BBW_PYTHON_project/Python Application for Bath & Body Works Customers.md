> Khristin Schenk
> February 9th, 2025
> Module 3 Final Project Launch
> SDEV220, Fall 2025

# Python Application for Bath & Body Works Customers

*This Python application is designed specifically for Bath & Body Works customers, enabling users to log and track their favorite candles by year and season. Customers can create a shopping list linked to their birthdays, holidays, and special occasions, all organized by week, day, and year. The details included are name (last, first), month, day, and year.*

---
### Core Functionalities of the Command-Line Program:
1. Add candles to a personal collection.
2. Organize candle inventories by year and season.
3. Designate statuses such as “SHOPPING LIST,” “I Have Not Smelled,” “I Like This One,” and more.
4. Save and retrieve data using a file format like JSON.

## Year and Month Organization:
- **2025:** JANUARY, FEBRUARY, MARCH, APRIL, ...and so on.

- **2024:** JANUARY, FEBRUARY, MARCH, APRIL, ...and so on.

- **2023:** JANUARY, FEBRUARY, MARCH, APRIL, ...and so on.

## Data Management:
Saved information may include:
- Shopping list options (Drafts, Final, Last Year, This Year, All Time)

- Status options (CREATE SHOPPING LIST, IMPORT SHOPPING LIST, SAVE/EDIT, UPDATE, BIRTHDAY HISTORY BY YEAR)


## User Prompts:
- Create a shopping list.

- Open my list(s) (dropdown for available years).

### Updating Information:
- Confirm updates before exiting.

- Prompt users to save changes.

### Birthday Computation:
To calculate age within the program, use the following formulas:

- Years: `=DATEDIF(A1, TODAY(), “Y”)`

- Months since last birthday: `=DATEDIF(A1, TODAY(), “YM”)`

- Days until next birthday: `=DATEDIF(A1, TODAY(), “MD”)`

- Combine results: `=CONCAT(A2, " years, ", A3, " months, ", A4, " days ")`

> **NOTE:** TO-DO!
> *Make an excel file that includes a column with formulas for the  Birthday Computation feature*
>
### Monthly Breakdown:
- 2025 | JANUARY (YEAR | MONTH)
- DAY (01-31)
- NAME (Last, First) / (First, Last)
- AGE THIS YEAR

### User Prompts for Editing:
- Create a shopping list.
- Edit shopping list.
- Export or share shopping list.
- Send notifications to phone or email.

### Inspiration for the Project:
The concept is inspired by a 3-inch binder used to store greeting cards, postcards, photographs, notes, artwork, and other personal items. These items are organized into sections based on the month they need to be sent or given. The binder includes tabbed dividers for each month of the year and has an introductory page for each section indicating the month and year. A basic table lists names and corresponding birthdays for each individual, arranged in alphabetical order and then sorted by the days of the month. Following pages for each month contain clear vellum envelopes to keep cards intended for specific individuals throughout the year, ensuring that cards are prepared in advance. This system combines elements of a calendar, reminder service (with push notifications, emails, texts, etc.), and a gift list organizer, organized by year, scent, collection, season, person, month, day, event, and more. 

---

### Binder Title:
Year

### Binder Dividers:
Month

### Table Columns:
- List of Days (01, 02, 03, …, 28, …, 31, etc.)
- Status (No Information Saved, View/Edit Notes, Plans, etc.)
- View/Edit Shopping/Wish Lists
- View/Edit Contacts
- List of Names (First, Last) or (Last, First)
- Names and Ages for the Current Year.

### Functions:
- Create, edit, or view:
  - Gift List
  - Shopping List (This Year, Last Year, All, etc.)
  - Set reminders (Yes/No)

