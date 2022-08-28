import contacts
import os.path
from file_operations import get_contacts, save_contacts

print('Welcome to the Contacts v1.0!')

# Contact list shall contain following data:
# name, e-mail, phone, address (optional), notes (optional)

filename = os.path.join(os.path.dirname(__file__), 'contacts_book.json')
contacts_list = get_contacts(filename)
if type(contacts_list) != list:
    contacts_list = []

contacts.print_list(contacts_list)

while True:
    print(contacts.menus('main'))

    action = input('Choice Your action: ')

    if action == 'q':
        prompt = input('Want You to save changes (y/n): ')
        if prompt == 'y':
            save_contacts(filename, contacts_list)
        print('Thank you! See You next time!')
        break

    elif action == 'a':
        contacts_list = contacts.add_contact(contacts_list)

    elif action == 'c':
        contacts_list = contacts.clear_all(contacts_list)

    elif action == 'd':
        contacts_list = contacts.del_single_contact(contacts_list)

    elif action == 'e':
        contacts_list = contacts.editor(contacts_list, contacts.menus('edit'))

    elif action == 'p':
        contacts.print_list(contacts_list)

    elif action == 'f':
        contacts.search_contact(contacts_list, contacts.menus('search'))

    elif action == 's':
        save_contacts(filename, contacts_list)

    else:
        print('Unknown choice!')
