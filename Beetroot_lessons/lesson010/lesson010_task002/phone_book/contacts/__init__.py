from rich.console import Console
from rich.table import Table
from rich import box
from rich import prompt
import uuid


def add_contact(some_list):
    """
    This function add the new contact to the list by asking user a data needed.
    :param some_list: Original list
    :return: modified list
    """
    uid = str(uuid.uuid4())
    name = input('Enter a name: ')
    email = input('Enter an e-mail: ')
    phone = input('Enter a phone number: ')
    address = input('Enter an address (optional): ')
    notes = input('Enter the notes (optional): ')
    address = address if len(address) > 0 else '-'
    notes = notes if len(notes) > 0 else '-'

    cell = {'id': uid,
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'notes': notes}

    some_list.append(cell)
    print("Contact created successfully!")
    return some_list


def clear_all(some_list):
    """
    This function clear all values in given list after user confirmation.
    :param some_list: Original list
    :return: Depends on user selection returns clear or an original list
    """
    print('This operation will remove all Your contacts.')
    choice = input('Will You continue (y/n)?: ')
    if choice == 'y':
        some_list = []
        return some_list
    else:
        return some_list


def del_single_contact(some_list):
    """
    This function delete only one selected contact from the list by prompting user
    to select an email of contact to be deleted.
    :param some_list: Original list
    :return: Modified list
    """
    del_mail = input('Enter an e-mail of Your contact, You want to delete: ')
    for cell in some_list:
        if cell['email'].lower().find(del_mail.lower()) != -1:
            some_list.remove(cell)
            print(f'Contact with email {del_mail} has been removed.')
            return some_list
    print(f'Contact with email {del_mail} not exist in the list.')


def editor(some_list, menu_string):
    """
    This function editing the contact by selected email, if it in the list.
    :param some_list: original list.
    :param menu_string: Menu template.
    :return: Edited list, or original list, depends on user's actions
    """
    param = prompt.Prompt.ask('Enter the "search by" parameter ('
                              'i.e.: name, email, phone or address)')
    edit_cont = prompt.Prompt.ask('Enter the value of given parameter for searching')

    try:
        for cell in some_list:
            if (param.lower() in cell.keys()) and \
                    (cell[param.lower()].find(edit_cont.lower()) != -1):
                while True:
                    print(menu_string)
                    item = prompt.Prompt.ask('Select item, you want to edit')
                    if item == 'r':
                        return some_list
                    elif item == 'n':
                        user_name = prompt.Prompt.ask('Enter the final name You want '
                                                      'to change')
                        cell['name'] = user_name
                    elif item == 'e':
                        user_email = prompt.Prompt.ask('Enter the final E-mail You '
                                                       'want to change')
                        cell['email'] = user_email
                    elif item == 'p':
                        user_phone = prompt.Prompt.ask('Enter the final phone You want '
                                                       'to change')
                        cell['phone'] = user_phone
                    elif item == 'a':
                        user_address = prompt.Prompt.ask('Enter the final address You '
                                                         'want to change')
                        cell['address'] = user_address
                    elif item == 'c':
                        user_notes = prompt.Prompt.ask('Enter the final notes You want '
                                                       'to change')
                        cell['notes'] = user_notes
                    else:
                        print('Unknown command.')
        else:
            print(f'Contact with parameter "{param}" or value "{edit_cont}" does'
                  f' not exist.')
    except TypeError:
        print('Your contact book have wrong data.')


def print_list(some_list):
    """
    This function prints all contains of the given parameter in the table mode.
    :param some_list: Original list
    :return: Nothing
    """
    table = table_creation()

    for cell in some_list:
        table.add_row(
            cell['name'],
            cell['email'],
            cell['phone'],
            cell.get('address', '-') or '-',
            cell.get('notes', '-') or '-'
        )
    console = Console()
    console.print(table)


def search_contact(some_list, menu_string):
    """
    This function will arrange searching in the list of contacts by various topics
    :param some_list: Original list, or empty list if original was cleared before
    :param menu_string: Sub menu template.
    :return: Table view with searched contact(s)
    """

    def search_engine(cont_list, s_key, s_value):
        search_list = []
        for contact in cont_list:
            if contact[s_key].lower().find(s_value.lower()) != -1:
                search_list.append(contact)
        table = table_creation(title='Search results')
        for cell in search_list:
            table.add_row(
                cell['name'],
                cell['email'],
                cell['phone'],
                cell.get('address', '-') or '-',
                cell.get('notes', '-') or '-'
            )
        console = Console()
        console.print(table)

    while True:
        print(menu_string)
        item = input('Item: ')
        if item == 'r':
            return
        elif item == 'fn' or item == 'ln' or item == 'n':
            key = 'name'
            value = input('Enter first, last or full name of contact: ')
            search_engine(some_list, key, value)
        elif item == 'e':
            key = 'email'
            value = input('Enter E-mail of contact: ')
            search_engine(some_list, key, value)
        elif item == 'p':
            key = 'phone'
            value = input('Enter phone number of contact: ')
            search_engine(some_list, key, value)
        elif item == 'a':
            key = 'address'
            value = input('Enter the City or State of contact: ')
            search_engine(some_list, key, value)
        else:
            print('Unknown command')


def table_creation(title='List of contacts'):
    table = Table(title=title, show_lines=True, box=box.DOUBLE_EDGE,
                  style='blue', row_styles=['dim', ''], title_style='dark_magenta',
                  header_style='dark_red')
    table.add_column("Name", style="green", justify='center')
    table.add_column("E-mail", style="blue", justify='center')
    table.add_column("Phone", style="green", justify='center')
    table.add_column("Address", justify='center')
    table.add_column("Notes", justify='center')
    return table


def menus(value):
    if value == 'main':
        main_menu = """
Main menu. Choose an option from below:
a - to add the contact
c - to clear contact list
d - to delete contact by e-mail
e - to edit contact
f - to find a contact
p - to print list of contacts
s - to save the changes
q - to exit (Anyhow, all changes to be saved to a file while exiting)
            """
        return main_menu
    elif value == 'edit':
        edit_menu = """
    Edit submenu. Select an item, You want to edit as follows:
    n - edit name
    e - edit E-mail
    p - edit phone
    a - edit address
    c - edit notes
    r - to return to the previous menu
            """
        return edit_menu
    elif value == 'search':
        search_menu = """
    Search submenu. Select an item, You want to search by:
    fn - search by first name
    ln - search by last name
    n - search by full name
    e - search by E-mail
    p - search by full phone number
    a - search by City or State
    r - to return to the previous menu
        """
        return search_menu
