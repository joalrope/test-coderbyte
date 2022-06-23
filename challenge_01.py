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


def clean_json(json):
    return {k: v for k, v in json.items() if (
        v != 'N/A' and v != '-' and v != '')}


def clear_list(list):
    return [i for i in list if (
        i != 'N/A' and i != '-' and i != '')]


def clean_key(dic):
    for key, value in dic.items():
        if isinstance(value, dict):
            dic[key] = clean_json(value)
        elif isinstance(value, list):
            dic[key] = clear_list(value)


def clean_data():
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')

    dic = r.json()

    new_dic = clean_json(dic)

    clean_key(new_dic)

    return new_dic


print(clean_data())
