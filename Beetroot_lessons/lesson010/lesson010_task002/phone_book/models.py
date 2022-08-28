import uuid


class Contact:
    def __init__(self, name, phone, email, address=None, notes=None, _id=None):
        self.id = str(uuid.uuid4()) if _id is None else _id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address if address is not None else "-"
        self.notes = notes if notes is not None else "-"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_short_name(self):
        initial = self.name.split()
        short_name = initial[0]
        if len(initial) > 1:
            short_name = f'{short_name} {initial[1][0]}'
        return short_name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_notes(self):
        return self.notes
