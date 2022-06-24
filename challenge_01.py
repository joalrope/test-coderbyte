# Back-end Challenge
# Imagine you are writing a function within a Django
# application to parse JSON data. In the Python file,
# write a program to perform a GET request on the
# route https://coderbyte.com/api/challenges/json/json-cleaning
# and then clean the object according to the following rules:
# Remove all keys that have values of N/A, -, or empty strings.
# If one of these values appear in an array,
# remove that single item from the array.
# Then print the modified object as a string.

# Example Input
# {"name":{"first":"Daniel","middle":"N/A","last":"Smith"},"age":45}

# Example Output
# {"name":{"first":"Daniel","last":"Smith"},"age":45}


import requests


def match(value):
    return (value != 'N/A' and value != '-' and value != '')


def clean_key(dic):

    new_dic = {k: v for k, v in dic.items() if match(v)}

    for key, value in new_dic.items():
        if isinstance(value, dict):
            new_dic[key] = {k: v for k, v in value.items() if match(v)}
        elif isinstance(value, list):
            new_dic[key] = [i for i in value if match(i)]

    return new_dic


def clean_data():
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')

    return clean_key(r.json())


print(clean_data())
