
# Bath & Body Works Fragrance Organizer

<!--
![Project Inspiration](https://via.placeholder.com/800x200.png?text=Digital+Fragrance+Organizer)  _Replace with actual screenshot_
-->


## 🌟 Features

### **Core Capabilities**

-   **Fragrance Tracker**  
    Catalog scents by year/season with custom statuses:  
    `Favorite`,  `I Like This One`,  `Wishlist`,  `Not Smelled`
    
-   **Smart Shopping Lists**  
    Create lists for birthdays, holidays, or events with:
    
    -   Status tracking (`Draft`,  `Final`,  `Last Year`,  `This Year`)
        
    -   Auto-save/load via JSON
        
    -   Sharing/export options
        
-   **Birthday Integration**  
    _Coming Soon: Age calculations and gift reminders_
    

### **Data Management**

-   **Structured Storage**
    
    json
    
    Copy
    
    {
      "2025": {
        "Spring": {
          "Palo Santo & Sage": "Favorite",
          "Paris Café": "Wishlist"
        }
      },
      "shopping_lists": {
        "Birthday": ["Palo Santo & Sage", "White Tea & Sage"]
      }
    }
    
-   **Automatic Organization**  
    Data sorted by year → month → day for easy historical tracking.
    

----------

## 🚀 Getting Started

### Installation

1.  Clone repository:
    
    bash
    
    Copy
    
    git clone https://github.com/yourusername/fragrance-organizer.git
    
2.  Install requirements:
    
    bash
    
    Copy
    
    pip install json os
    

### Basic Usage

python

Copy

# Add a fragrance
add_fragrance("Winter Wonderland", "2025", "Winter", "I Like This One")

# Create shopping list
create_shopping_list("Holiday Gifts")

# Add item to list
add_to_shopping_list("Holiday Gifts", "Winter Wonderland")

----------

## 📂 Data Structure

JSON Field

Description

Example Values

`year`

Chronological tracking (2023-2025)

`2024`,  `2025`

`season`

Seasonal categorization

`Winter`,  `Spring`,  `Summer`,  `Fall`

`shopping_lists`

Custom lists with fragrance names

`Birthday`,  `Spring Favorites`

----------

## 🗂️ Binder System vs. Digital Organizer

Binder System

Digital Application

Physical monthly tabs

Auto-sorted calendar view

Handwritten notes

Searchable digital records

Manual age calculations

_Planned: Automated birthday reminders_

Paper shopping lists

Shareable lists with status tracking

----------

## 📜 Project Inspiration

Digitizes a physical organization system using:

-   **Monthly sections**  for tracking events
    
-   **Pocket dividers**  → Digital reminders/notes
    
-   **Alphabetical lists**  → Searchable contacts
    
-   **Gift planning**  → Smart shopping lists
    

----------

## 🛠️ Future Enhancements

1.  Birthday age calculator with Excel integration
    
2.  Email/SMS reminders for events
    
3.  Fragrance recommendation engine
    
4.  Multi-user collaboration
    

----------

_Created with ❤️ by [Your Name] –  [Contribute](https://github.com/yourusername/fragrance-organizer)_  
_License: MIT_
