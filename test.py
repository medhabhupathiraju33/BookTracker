# temporary lists to verify main menu logic is working properly before using JSON file
book_lists = {
'to_be_read': ['book 3', 'book 4'],
'currently_reading': ['book 2'],
'finished': ['book 1'],
}


def display_books(book_data):
    print('\n ----- BOOK TRACKER -----')
    print(f"To Be Read: {book_data['to_be_read']}")
    print(f"Currently Reading: {book_data['currently_reading']}")
    print(f"Finished: {book_data['finished']}")
    print('-------------------------\n')


cont = True
while cont:
    user_input = input('\nMain Menu:\n1. Add book to a list\n2. View book lists\n3. Exit\nEnter the number that corresponds to the option you want to choose: ')
    # compares user input to string to aviod ValueError if string is entered 
    if user_input == '1':
        # inner while loop is to help with input validation when user is asked which list they want to append a book to
        while True:
            which_list = input('\n1. To Be Read\n2. Currently Reading\n3. Finished\nWhich list do you want to add a book to? Enter the number that corresponds to the option you want to choose: ')
            if which_list in ['1','2','3']:
                break
            print('Please pick a number that corresponds to one of the given options: ')
        book_name = input('Enter the name of the book you want to add: ')
        if which_list == '1':
            book_lists['to_be_read'].append(book_name)
        elif which_list == '2':
            book_lists['currently_reading'].append(book_name)
        elif which_list == '3':
            book_lists['finished'].append(book_name)
    elif user_input == '2':
        display_books(book_lists)
    elif user_input == '3':
        cont = False
    else: 
        print('Please pick a number that corresponds to one of the given options:')