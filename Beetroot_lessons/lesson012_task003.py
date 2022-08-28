"""Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and
print the reason it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'"""


def arg_rules(type_: type, max_length: int, contains: list):
    def validation(func):
        def verification(*args):
            for i in range(len(args)):
                if type(args[i]) != type_:
                    print(f"Error in {args[i]}, argument should be a {type_} type.")
                    return False
                elif len(args[i]) > max_length:
                    print(f"Error in {args[i]}, argument should be a {max_length} "
                          f"symbols long.")
                    return False
                elif False in [contain not in args for contain in contains]:
                    print(f"Error in {args[i]}, argument should contain a {contains} "
                          f"symbols")
                    return False
            return func(*args)
        return verification
    return validation


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'