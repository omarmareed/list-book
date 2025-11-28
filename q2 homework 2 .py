def library_query(catalog, criteria, sort_by=None):

    # Filter books based on criteria
    filtered_books = catalog

    for key, value in criteria.items():
        if key in ['title', 'author']:  # Partial match for 'title' and 'author'
            filtered_books = [book for book in filtered_books if value.lower() in book.get(key, '').lower()]
        elif key in ['year', 'genre']:  # Exact match for 'year' and 'genre'
            filtered_books = [book for book in filtered_books if book.get(key) == value]

    # Filter by availability
    if 'available' in criteria and criteria['available']:
        filtered_books = [book for book in filtered_books if book.get('copies', 0) > 0]

    # Sort results if sort_by is provided
    if sort_by:
        filtered_books = sorted(filtered_books, key=lambda book: book.get(sort_by))

    # Check if any books match the criteria
    if not filtered_books:
        return "No matching books found."

    return filtered_books



library_catalog = [
    {'title': 'The Great warrior', 'author': ' Scott bush', 'year': 1968, 'genre': 'War/Historical', 'copies': 3},
    {'title': 'Love thunder', 'author': 'Oliver queen', 'year': 1991, 'genre': 'Romance', 'copies': 0},
    {'title': 'The gentle thief', 'author': 'George obama', 'year': 1897, 'genre': 'suicide', 'copies': 5},
    {'title': 'Mystery island', 'author': 'Dyane johnson', 'year': 2004, 'genre': 'Adventure', 'copies': 2},
]


search_criteria = {'author': 'George', 'available': True}
results = library_query(library_catalog, search_criteria, sort_by='title')
print(results)
