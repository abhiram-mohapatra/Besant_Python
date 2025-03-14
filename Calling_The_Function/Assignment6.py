#Conditional statement using calling the function(For book store and stationary store) 

# Function to handle bookstore tasks
def bookstore():
    print("\n Welcome, we have the following categories of books available:")
    print("1. Fiction")
    print("2. Non-fiction")
    print("3. Science")
    print("4. Fantasy")
    print("5. Mystery")
    
    category_choice = input("\nPlease choose a category: ")
    
    if category_choice == '1':
        display_books('Fiction')
    elif category_choice == '2':
        display_books('Non-fiction')
    elif category_choice == '3':
        display_books('Science')
    elif category_choice == '4':
        display_books('Fantasy')
    elif category_choice == '5':
        display_books('Mystery')
    else:
        print("\nInvalid choice! Returning to the main menu.")
    
    continue_shopping = input("\nWould you like to continue shopping? (yes/no): ").lower()
    if continue_shopping == 'yes':
        bookstore()
    else:
        print("\nThank you for visiting the store!")

# Function to display books based on category
def display_books(category):
    books = {
        'Fiction': ['The Great Gatsby -  by F. Scott Fitzgerald', 'To Kill a Mockingbird - by Harper Lee', '1984 - by George Orwell'],
        'Non-fiction': ["Sapiens: A Brief History of Humankind - by Yuval Noah Harari", 'Educated - by Tara Westover', 'Becoming - by Michelle Obama'],
        'Science': ['A Brief History of Time -  by Stephen Hawking', 'The Selfish Gene - by Richard Dawkins', 'The Gene: An Intimate History - by Siddhartha Mukherjee'],
        'Fantasy': ["Harry Potter and the Sorcerer's Stone - by J.K. Rowling", 'The Hobbit -  by J.R.R. Tolkien', 'A Game of Thrones - by George R.R. Martin'],
        'Mystery': ['The Girl with the Dragon Tattoo - by Stieg Larsson', 'Gone Girl - by Gillian Flynn', 'The Hound of the Baskervilles - by Arthur Conan Doyle']
    }
    
    print(f"\nHere are some {category} books available for you:")
    for index, value in enumerate(books[category], start=1):
        print(f"{index}. {value}")
    
    book_choice = int(input("\nEnter your choice: "))
    if book_choice <= len(books[category]):
        print(f"\nYou have selected: {books[category][book_choice - 1]}")
        purchase_confirmation = input("Would you like to purchase this book? (yes/no): ").lower()
        if purchase_confirmation == 'yes':
            print(f"\nThank you for purchasing {books[category][book_choice - 1]}!")
        else:
            print("\nYou chose not to purchase this book. Returning to category menu.")
    else:
        print("\nInvalid book selection. Returning to category menu.")

# Function to handle stationery store tasks
def stationery_store():
    print("\nWelcome, we have the following categories of items available:")
    print("1. Writing Instruments")
    print("2. Notebooks & Paper")
    print("3. Office Supplies")
    print("4. Art Supplies")
    print("5. Accessories")
    
    category_choice = input("\nPlease choose a category (Enter the number): ")
    
    if category_choice == '1':
        display_stationery('Writing Instruments')
    elif category_choice == '2':
        display_stationery('Notebooks & Paper')
    elif category_choice == '3':
        display_stationery('Office Supplies')
    elif category_choice == '4':
        display_stationery('Art Supplies')
    elif category_choice == '5':
        display_stationery('Accessories')
    else:
        print("\nInvalid choice! Returning to the main menu.")
    
    continue_shopping = input("\nWould you like to continue shopping? (yes/no): ").lower()
    if continue_shopping == 'yes':
        stationery_store()
    else:
        print("\nThank you for visiting the store!")

# Function to display stationery items based on category
def display_stationery(category):
    items = {
        'Writing Instruments': ['Pens', 'Pencils', 'Markers'],
        'Notebooks & Paper': ['Notebooks', 'Loose Leaf Paper', 'Sticky Notes'],
        'Office Supplies': ['Staplers', 'Paper Clips', 'Binders'],
        'Art Supplies': ['Paint', 'Brushes', 'Canvas'],
        'Accessories': ['Organizers', 'Desk Lamps', 'Calendars']
    }
    
    print(f"\nHere are some {category} items available for you:")
    for index, value in enumerate(items[category], start=1):
        print(f"{index}. {value}")
    
    item_choice = int(input("\nEnter your choice: "))
    if item_choice <= len(items[category]):
        print(f"\nYou have selected: {items[category][item_choice - 1]}")
        purchase_confirmation = input("Would you like to purchase this item? (yes/no): ").lower()
        if purchase_confirmation == 'yes':
            print(f"\nThank you for purchasing {items[category][item_choice - 1]}!")
        else:
            print("\nYou chose not to purchase this item. Returning to category menu.")
    else:
        print("\nInvalid item selection. Returning to category menu.")

# Main function to ask user for store type
def store_choice():
    print("\nWelcome to our Store! We have two section")
    print("1. Bookstore")
    print("2. Stationery Store")
    
    choice = input("\nPlease choose the which section you want to visit (Enter 1 for Bookstore or 2 for Stationery Store): ")
    
    if choice == '1':
        bookstore()
    elif choice == '2':
        stationery_store()
    else:
        print("\nInvalid choice!")
        store_choice()

# Start the program
store_choice()
