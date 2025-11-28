def library_query(catalog, criteria, sort_by=None, available=False):

    results = []

    for book in catalog:
        match = True

        for key, value in criteria.items():
            if key in book:
                if key in ['year', 'genre']:
                    if book[key] != value:
                        match = False
                        break
                elif key in ['title', 'author']:
                    if value.lower() not in book[key].lower():
                        match = False
                        break
            else:
                match = False
                break


        if available and book.get('copies', 0) <= 0:
            match = False

        if match:
            results.append(book)

    #
    if sort_by:
        results = sorted(results, key=lambda x: x.get(sort_by, ''))

    #
    if not results:
        return

    return results



catalog = [
    {'title': 'lost', 'author': 'pablo smith', 'year': 2016, 'genre': 'survival', 'copies': 5},
    {'title': 'fury', 'author': 'patrick queens', 'year': 2019, 'genre': 'war/action', 'copies': 0},
    {'title': 'rise of the kingdoms', 'author': 'ned stark', 'year': 2021, 'genre': 'historical', 'copies': 3},
]

#
criteria = {'author': 'pablo smith', 'year': 2016},


result = library_query(catalog,criteria, sort_by='title', available=True)
print(result)


