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
            return f"Sorry, '{book_name}' is  not available."

    elif action == 'return':
        if book_name in user_account['borrowed_books']:
            late_fee = 0
            if user_account.get('borrowed_dates', {}).get(book_name, None):

                if user_account['borrowed_dates'][book_name] > 7:  # 7 is an example
                    late_fee = 5  # 5 is an example

            book['copies'] += 1
            user_account['borrowed_books'].remove(book_name)
            user_account['debts'] += late_fee

            if late_fee > 0:
                 return (f"You have returned '{book_name}'. "
                        f"You got a late fee of ${late_fee}.")
            else:
                 return f"You have returned '{book_name}'."

        else:
             return f"Error: You did borrow '{book_name}'."

    else:
         return "Error: Invalid action. Please use 'borrow' or 'return'."


library_catalog = [{'title': 'The Great Britain', 'author': 'Lionel messi', 'year': 1925, 'genre': 'Historical', 'copies': 3},
    {'title': 'The last dance', 'author': 'Paolo maldini', 'year': 2008, 'genre': 'sport', 'copies': 5},]

user_account = { 'name': 'Leonardo','borrowed_books': [],'debts': 0,'borrowed_dates': {}}


print(loan_management(library_catalog, user_account, 'The last dance', 'borrow'))

user_account['borrowed_dates']['The last dance'] = 8  # 8 is an example

print(loan_management(library_catalog, user_account, 'The last dance', 'return'))


print(f"Borrowed Books: {user_account['borrowed_books']}")
print(f"Debts: ${user_account['debts']}")
