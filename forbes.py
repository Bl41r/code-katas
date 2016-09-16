import json


def oldrich_and_youngest(filename):
    """Return info for oldest under 80 and youngest billionaires."""
    with open(filename) as json_data:
        data = json.load(json_data)

    init_dict1 = {'net_worth (USD)': 0, 'age': 0}
    init_dict2 = {'net_worth (USD)': 0, 'age': 80}
    return_dict = {'oldest': init_dict1, 'youngest': init_dict2}
    for entry in data:
        if entry['age'] < 1 or entry['age'] > 79:
            continue
        if entry['age'] > return_dict['oldest']['age'] and entry['net_worth (USD)'] > return_dict['oldest']['net_worth (USD)']:
            return_dict['oldest'] = entry
        if entry['age'] < return_dict['youngest']['age']:
            return_dict['youngest'] = entry
    print(((return_dict['oldest']['name'], return_dict['oldest']['net_worth (USD)'], return_dict['oldest']['source']),
            (return_dict['youngest']['name'], return_dict['youngest']['net_worth (USD)'], return_dict['youngest']['source'])))
    return ((return_dict['oldest']['name'], return_dict['oldest']['net_worth (USD)'], return_dict['oldest']['source']),
            (return_dict['youngest']['name'], return_dict['youngest']['net_worth (USD)'], return_dict['youngest']['source']))


if __name__ == '__main__':  # pragma: no cover
    oldrich_and_youngest('forbes_billionaires_2016.json')
