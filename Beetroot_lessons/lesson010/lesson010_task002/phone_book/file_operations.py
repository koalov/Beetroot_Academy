import json
from models import Contact


def get_contacts(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            contacts = [Contact(c["name"], c["email"], c["phone"], c['address'],
                                c['notes'], c['id']) for c in json.load(file)]
            return json.load(file)
    except json.JSONDecodeError:
        contacts = []
        return contacts


def save_contacts(filename, contacts):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=2, ensure_ascii=False)





