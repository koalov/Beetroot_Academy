"""Write a decorator that takes a list of stop words and replaces them with * inside the
decorated function

def stop_words(words: list):
    pass

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"""


def stop_words(words: list):
    def string_to_change(func):
        def inside_func(*args):
            new_string = func(*args)
            for word in words:
                if word in new_string:
                    new_string = new_string.replace(word, "*")
            return new_string
        return inside_func
    return string_to_change


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
