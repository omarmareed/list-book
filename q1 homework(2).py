from dbm import error


def inventory_update(catalog, action, book_details):
    required_fields = {'name', 'author', 'quantity', 'type', 'location'}

    if not all(field in book_details for field in required_fields):
        missing_fields = required_fields - book_details.keys()
        raise ValueError(f"Missing details: {', '.join(missing_fields)}")

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
    elif action == "update":
        for book in catalog:
            if book['name'] == book_name:
                book.update(book_details)
                return
        print(f"Book '{book_name}' not found for update.")

    else: raise ValueError("Invalid action. Choose 'add', 'remove', or 'update'.")



library_catalog = [  {'name': 'Lost', 'author': 'max smith', 'quantity': 4, 'type': 'Survival', 'location': 'World digital library'},
    {'name': 'Fury', 'author': 'patrick queens', 'quantity': 2, 'type': 'War/Action', 'location': 'Internet archive'},
]

try:
    inventory_update(library_catalog, 'add',
                     {'name': 'Rise of kingdoms', 'author': 'Ned stark', 'quantity': 3, 'type': 'Historical', 'location': 'Bartleby'})
    inventory_update(library_catalog, 'remove', {'name': 'Lost','author': ' max smith' , 'quantity': 2, 'type': ' survival' , 'location': 'World digital library'})
    inventory_update(library_catalog, 'update', {'name': 'Fury', 'author': 'Maurice Leblanc', 'quantity': 2, 'type': 'Fiction','location': 'French national library'})

except ValueError as i:
    print(i)

print(library_catalog)