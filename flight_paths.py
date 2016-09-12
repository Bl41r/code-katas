import json
from simple_graph import Node, SimpleGraph
from simple_graph import spt_Dijkstra


def extract_data_from_json(file):
    with open(file) as json_data:
        data = json.load(json_data)
    new_data = []
    for d in data:
        entry = {}
        entry['city'] = d['city']
        entry['neighbors'] = d['destination_cities']
        entry['lat-lon'] = d['lat_lon']
        new_data.append(entry)
    return new_data


def build_graph(new_data):
    gr = SimpleGraph()

    for city in new_data:
        n = Node(city['city'], city['lat-lon'])
        try:
            gr.add_node(n)
        except KeyError:
            pass

    for city in new_data:
        if city['city'] not in gr.node_dict.keys():
            continue
        key = city['city']
        for neighbor in city['neighbors']:
            try:
                d = calculate_distance(gr.node_dict[key].data, gr.node_dict[neighbor].data)
            except KeyError:
                continue
            gr.node_dict[key].neighbors.append((neighbor, d))
    return gr


def depth_first_search(graph, start, end):
    """Perform a depth traversal.  'start' and 'end' are nodes."""
    curr = [start]
    ret = []
    path = []
    d = 0

    while len(curr):
        c = curr.pop()
        ret.append(c.name)
        path.append(c.name)
        if len(path) > 1:
            d += calculate_distance(graph.node_dict[path[-2]].data, graph.node_dict[path[-1]].data)
        if c.name == end.name:
            break
        if len(c.neighbors) == 0:
            path = [start.name]
            d = 0
        for n in c.neighbors:
            if graph.node_dict[n[0]].name not in ret:
                curr.append(graph.node_dict[n[0]])
    return path, d


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934   # convert km to miles
