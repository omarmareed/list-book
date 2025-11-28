def inventory_update(catalog, action, book_details):
    required_subjects = {'name', 'author', 'quantity', 'type', 'location'}

    if not all(subject in book_details for subject in required_subjects):
        missing_details = required_subjects - book_details.keys()
        raise ValueError(f"Missing details: {', '.join(missing_details)}")

    book_name = book_details["name"]
    book_quantity = book_details["quantity"]

    # adding a book to the catalog
    if action == "add":
        for book in catalog:
            if book["name"] == book_name:
                book["quantity"] += book_quantity
                return

        catalog.append(book_details.copy())

    # removing a book from the catalog
    elif action == "remove":
        for book in catalog:
            if book["name"] == book_name:
                if book["quantity"] > book_quantity:
                    book["quantity"] -= book_quantity
                else:
                    catalog.remove(book)
                return
        print(f"Book '{book_name}' not found for removal.")

    # updating a book in the catalog " the author and the type and location "
    elif action =="update":
        for book in catalog:
            if book['name'] == book_name:
                book.update(book_details)
                return
        print(f"Book '{book_name}' there is no update.")

    else: raise ValueError("Invalid action. Choose 'add', 'remove', 'update'.")

# examples of books
library_catalog = [  {'name': 'Lost', 'author': 'max smith', 'quantity': 4, 'type': 'Survival', 'location': 'World digital library'},
    {'name': 'Fury', 'author': 'patrick queens', 'quantity': 2, 'type': 'War/Action', 'location': 'Internet archive'},
]

try:
    inventory_update(library_catalog, 'add', {'name': 'Rise of kingdoms', 'author': 'Ned stark', 'quantity': 3, 'type': 'Historical', 'location': 'Bartleby'})
    inventory_update(library_catalog, 'remove', {'name': 'Lost','author': ' max smith' , 'quantity': 2, 'type': ' survival' , 'location': 'World digital library'})
    inventory_update(library_catalog, 'update', {'name': 'Fury', 'author': 'Maurice Leblanc', 'quantity': 2, 'type': 'Fiction','location': 'French national library'})

except ValueError as i:
    print(i)

print(library_catalog)

#########################################################################################################################################################################################################
#########################################################################################################################################################################################################

def library_query(catalog, criteria, sort_by=None):

    # Filter books based on criteria
    filtered_books = catalog

    for key, value in criteria.items():
        if key in ['title', 'author']:  # Partial match for 'title' and 'author'
            filtered_books = [book for book in filtered_books if value.lower() in book.get(key, '').lower()]
        elif key in ['year', 'genre']:  # Exact match for 'year' and 'genre'
            filtered_books = [book for book in filtered_books if book.get(key) == value]


    if 'available' in criteria and criteria['available']:
        filtered_books = [book for book in filtered_books if book.get('copies', 0) > 0]

    if sort_by:
        filtered_books = sorted(filtered_books, key=lambda book: book.get(sort_by))

    # Check if any books match the criteria
    if not filtered_books:
        return "No matching books found."

    return filtered_books


library_catalog = [
    {'title': 'The Great warrior', 'author': ' Scott bush', 'year': 1968, 'genre': 'War/Historical', 'copies': 3},
    {'title': 'Love thunder', 'author': 'Oliver queen', 'year': 1991, 'genre': 'Romance', 'copies': 0},
    {'title': 'The gentle thief', 'author': 'Aresen lupin ', 'year': 1897, 'genre': 'suicide', 'copies': 5},
    {'title': 'Mystery island', 'author': 'Dyane johnson', 'year': 2004, 'genre': 'Adventure', 'copies': 2},
]


search_criteria = {'author': 'Aresen', 'available': True}
results = library_query(library_catalog, search_criteria, sort_by='title')
print(results)

#########################################################################################################################################################################################################
#########################################################################################################################################################################################################


def loan_management(catalog, user_account, book_name, action):

    book = next((b for b in catalog if b['title'].lower() == book_name.lower()), None)

    if not book:
        return "Error: The book is not in the catalog."

    if action == 'borrow':
        if book['copies'] > 0:
            book['copies'] -= 1
            user_account['borrowed_books'].append(book_name)
            return f"You have borrowed '{book_name}'."
        else:
            return f"Sorry, '{book_name}' is not available."

    elif action == 'return':
        if book_name in user_account['borrowed_books']:
            late_fee = 0
            if user_account.get('borrowed_dates', {}).get(book_name, None):

                if user_account['borrowed_dates'][book_name] > 7:  # 7 is an example
                    late_fee =  4 # 4 is an example

            book['copies'] += 1
            user_account['borrowed_books'].remove(book_name)
            user_account['debts'] += late_fee

            if late_fee > 0:
                 return (f"You returned '{book_name}'. "
                        f"You got late fee of ${late_fee}.")
            else:
                 return f"You returned '{book_name}'."

        else:
             return f"Error: You borrowed'{book_name}'."

    else:
         return "Error: Invalid action. Please use 'borrow' , 'return'."


library_catalog = [{'title': 'The industrial revolution', 'author': 'Thomas shelby', 'year': 1802, 'genre': 'Historical', 'copies': 3},
    {'title': 'The last dance', 'author': 'paolo maldini', 'year': 2008, 'genre': 'sport', 'copies': 5},]

user_account = { 'name': 'Leonardo','borrowed_books': [5],'debts': 2,'borrowed_dates': {}}


print(loan_management(library_catalog, user_account, 'The last dance', 'borrow'))

user_account['borrowed_dates']['The last dance'] = 9  # 9 is example

print(loan_management(library_catalog, user_account, 'The last dance', 'return'))


print(f"Borrowed Books: {user_account['borrowed_books']}")
print(f"Debts: ${user_account['debts']}")


