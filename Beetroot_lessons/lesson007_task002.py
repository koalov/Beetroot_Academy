"""Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as
parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’
as a parameter. Make the function print out the values of the dictionary to make sure
that it works as intended."""


def make_country(country_name, capital):
    country = dict()
    country[country_name] = capital
    return country


print(make_country('Ukraine', 'Kyiv'))
print(make_country('Israel', 'Haifa'))
print(make_country('USA', 'Washington'))
print(make_country('Italy', 'Rome'))
print(make_country('Philippines', 'Manila'))
print(make_country('Singapore', 'Singapore'))
