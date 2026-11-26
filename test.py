book_lists = {
'to_be_read': ['book 3', 'book 4'],
'currently_reading': ['book 2'],
'finished': ['book 1'],
}


def display_books(book_data):
    # displays all of the book lists in the terminal
    print('\n ----- BOOK TRACKER -----')
    print(f"To Be Read: {book_data['to_be_read']}")
    print(f"Currently Reading: {book_data['currently_reading']}")
    print(f"Finished: {book_data['finished']}")
    print('-------------------------\n')

display_books(book_lists)