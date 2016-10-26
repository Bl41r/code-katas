"""Forbes top 40.

This savory chunk of code takes a provided json file, namely
forbes_billionaires.json, and returns the oldest dude on the list under
the age of 80, and the youngest member of the list.  There are a few
'errors' in the json file, so only valid ages are considered.
"""

import json


def oldrich_and_youngest(filename):
    """Return info for oldest under 80 and youngest billionaires."""
    with open(filename) as json_data:
        data = json.load(json_data)

    init_dict_o = {'name': 'init', 'net_worth (USD)': 0, 'age': 0}
    init_dict_y = {'name': 'init', 'net_worth (USD)': 0, 'age': 80}
    return_dict = {'oldest': init_dict_o, 'youngest': init_dict_y}

    for entry in data:
        try:
            if entry['age'] < 1 or entry['age'] > 79:
                continue
            if entry['age'] > return_dict['oldest']['age']:
                return_dict['oldest'] = entry
            if entry['age'] < return_dict['youngest']['age']:
                return_dict['youngest'] = entry
        except KeyError:
            raise KeyError('There was a problem the data.')
    print(return_dict)

    return ((return_dict['oldest']['name'],
            return_dict['oldest']['net_worth (USD)'],
            return_dict['oldest']['source']),

            (return_dict['youngest']['name'],
                return_dict['youngest']['net_worth (USD)'],
                return_dict['youngest']['source']))


if __name__ == '__main__':  # pragma: no cover
    print(oldrich_and_youngest('forbes_billionaires_2016.json'))
