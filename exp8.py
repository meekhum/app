def main_menu():
    """
    Display the main menu and handle user interactions.
    """
    print("Welcome to the Library System")
    
    while True:
        print("\nMain Menu:")
        print("1. Add Book to Cart")
        print("2. Show Cart")
        print("3. Search Record")
        print("4. Update Catalogue")
        print("5. Exit")
        
        try:
            user_choice = int(input("Enter your choice (1-5): "))
            
            if user_choice == 1:
                add_book_to_cart()
            elif user_choice == 2:
                show_cart()
            elif user_choice == 3:
                search_record()
            elif user_choice == 4:
                Update_Catalogue()
            elif user_choice == 5:
                print("Thank you for using the Library System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Assuming these functions are defined elsewhere in the code
def add_book_to_cart():
    pass

def show_cart():
    pass

def search_record():
    pass

def Update_Catalogue():
    pass

# To run the system

main_menu()