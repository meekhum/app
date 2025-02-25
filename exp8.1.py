def add_book_to_cart():
    """
    Function to add a book to the shopping cart.
    It validates the book ID, action (buy/rent), and quantity/renting period.
    """
    global Shopping_Cart, library_catalogue  # Assuming these are defined globally
    
    while True:
        book_id = input("Enter the Book ID (or type 'END' to return to the main menu): ")
        
        if book_id == "END":
            return  # Return to main menu
        
        if is_valid_book_id(book_id):
            action = input("Do you want to 'Buy' or 'Rent' the book? ").strip().lower()
            
            if action == "buy":
                quantity = int(input("Enter the quantity: "))
                if is_valid_quantity(book_id, quantity):
                    # Add book to shopping cart
                    book_details = library_catalogue[book_id]
                    Shopping_Cart[book_id] = {
                        'Title': book_details['Title'],
                        'Author': book_details['Author'],
                        'Quantity': quantity,
                        'Purchasing Price': book_details['Purchasing Price']
                    }
                    # Update the catalogue
                    library_catalogue[book_id]['Items Available'] -= quantity
                    print(f"{quantity} copies of '{book_details['Title']}' added to the cart.")
                else:
                    print("Invalid quantity. Please try again.")
                    
            elif action == "rent":
                renting_period = int(input("Enter the renting period in days (max 90 days): "))
                if renting_period > 0 and renting_period <= 90:
                    # Add book to shopping cart
                    book_details = library_catalogue[book_id]
                    Shopping_Cart[book_id] = {
                        'Title': book_details['Title'],
                        'Author': book_details['Author'],
                        'Renting Period': renting_period,
                        'Renting Price': book_details['Purchasing Price'] * 0.30 * (renting_period // 30 + 1)  # Calculate renting cost
                    }
                    # Update the catalogue
                    library_catalogue[book_id]['Renting Availability'] = False  # Set to not available for rent
                    print(f"'{book_details['Title']}' added to the cart for renting for {renting_period} days.")
                else:
                    print("Invalid renting period. Please try again.")
            else:
                print("Invalid action. Please enter 'Buy' or 'Rent'.")
        else:
            print("Invalid Book ID. Please try again.")

def is_valid_book_id(book_id):
    """
    Validate the book ID.
    Check if the book ID exists in the library catalogue and follows the format "BXXX".
    """
    if book_id in library_catalogue:
        return True
    else:
        return False

def is_valid_quantity(book_id, quantity):
    """
    Validate the quantity for purchasing.
    Check if the quantity is a valid integer and does not exceed available stock.
    """
    if quantity > 0 and quantity <= library_catalogue[book_id]['Items Available']:
        return True
    else:
        return False