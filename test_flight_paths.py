import pytest

def test_extract_data_from_json():
    """Test extracted data."""
    from flight_paths import extract_data_from_json
    data = extract_data_from_json('cities_with_airports.json')
    assert len(data) > 0
    assert type(data) is list
    assert type(data[0]) is dict


def test_build_graph():
    """Assert graph is built properly."""
    from flight_paths import build_graph
    from flight_paths import extract_data_from_json
    data = extract_data_from_json('cities_with_airports.json')
    gr = build_graph(data)

    assert len(gr.edges()) > 0
    assert len(gr.node_dict) > 0
    assert len(gr.nodes()) > 0
    assert len(gr.neighbors(gr.node_dict['Charlotte'])) > 70


def test_depth_first_search():
    """Assert search was completed."""
    from flight_paths import build_graph
    from flight_paths import extract_data_from_json
    from flight_paths import depth_first_search
    data = extract_data_from_json('cities_with_airports.json')
    gr = build_graph(data)
    x = depth_first_search(gr, gr.node_dict['Charlotte'], gr.node_dict['Honolulu'])
    assert x[0][0] == 'Charlotte' and x[0][-1] == 'Honolulu'


def test_spt_Dijkstra():
    """Test distance found.  Denver to Honolulu is direct."""
    from flight_paths import build_graph
    from flight_paths import extract_data_from_json
    from simple_graph import spt_Dijkstra
    data = extract_data_from_json('cities_with_airports.json')
    gr = build_graph(data)
    dist = spt_Dijkstra(gr, 'Denver', 'Honolulu')
    assert dist < 3361 and dist > 3360


def test_spt_AStar():
    """Test distance found."""
    from flight_paths import build_graph
    from flight_paths import extract_data_from_json
    from simple_graph import spt_AStar
    data = extract_data_from_json('cities_with_airports.json')
    gr = build_graph(data)
    dist = spt_AStar(gr, 'Denver', 'Honolulu')
    assert dist < 3361 and dist > 3360
