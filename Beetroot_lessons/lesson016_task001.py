"""Task 1

Create a class method named `validate`, which should be called from the `__init__`
method to validate parameter email, passed to the constructor. The logic inside the
`validate` method could be to check if the passed email parameter is a valid email
string.

Email validations:

Valid email address format

Email address """


class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        is_valid = False
        if type(self.email) == str and len(self.email) > 3 and '@' in self.email:
            is_valid = True
        return print(f'Email address: {self.email} is '
                     f'{"valid" if is_valid == True else "invalid"} format.')

    def __str__(self):
        return self.validate()


mail = EmailValidator('user@example.com')
