# code-katas
- This repo holds solutions for the Code Wars katas and other katas
which I have worked on.


This one features a node search for airplane travel.

https://codefellows.github.io/sea-python-401d4/assignments/kata_flight_paths.html

### usage  in iPython3:
- run flight_paths.py
- data = extract_nodes_from_json('cities_with_airports.json')
- gr = build_graph(data)
- depth_first_search(gr, gr.node_dict['Denver'], gr.node_dict['Honolulu'])
- spt_Dijkstra(gr, 'Denver', 'Honolulu') OR spt_AStar(gr, 'Denver', 'Honolulu')
