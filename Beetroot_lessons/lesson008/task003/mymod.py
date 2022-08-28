def count_lines(name):
    with open(name, 'r') as file:
        file.seek(0)
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as f:
        symbols = 0
        f.seek(0)
        for line in f.readlines():
            symbols += len(line)
    return symbols


def test(name):
    lines = count_lines(name)
    symbols = count_chars(name)
    print(f'Given file have a {lines} lines, and {symbols} symbols in it.')


test('Volcanoes.txt')
