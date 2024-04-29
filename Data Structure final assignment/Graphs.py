import networkx as nx  # Importing NetworkX library for graph creation and manipulation
import matplotlib.pyplot as plt  # Importing Matplotlib library for visualization

class Edge:  # define a class named Edge, which will be the roads
    def __init__(self, edge_id, name, length, houses=None):  # constructor method for initializing attributes for Edge
        self.id = edge_id  # add attribute of id
        self.name = name  # add attribute of name
        self.length = length  # add attribute of length
        self.houses = houses if houses else []  # add attribute of house if available, otherwise, it will be represented as an empty list


class Vertex:  # define a class named Vertex, which will be the intersections
    def __init__(self, vertex_id):  # constructor method for initializing attributes for Vertex
        self.id = vertex_id  # add attribute of id
        self.adjacent = {}  # initialize adjacent as dictionary

    def add_neighbor(self, neighbor, edge):  # define a function to add a neighbor for a vertex
        self.adjacent[neighbor] = edge  # adding neighbor and corresponding edge to the adjacency list of the vertex


class Graph:  # define a class named Graph
    def __init__(self):  # constructor method for the Graph class to initialize its attributes
        self.vertices = {}  # initialize vertices as dictionary
        self.edges = []  # initialize edges as list

    def add_edge(self, from_vertex, to_vertex, edge_id, edge_name, length, houses=None):  # define a function to add an edge to the graph
        if from_vertex not in self.vertices:  # Check if 'from_vertex' is not in the vertices dictionary
            self.vertices[from_vertex] = Vertex(from_vertex)  # If not, create a new vertex object and add it to the vertices dictionary
        if to_vertex not in self.vertices:  # Check if 'to_vertex' is not in the vertices dictionary
            self.vertices[to_vertex] = Vertex(to_vertex)  # If not, create a new vertex object and add it to the vertices dictionary
        edge = Edge(edge_id, edge_name, length, houses)  # create a new edge object
        self.vertices[from_vertex].add_neighbor(to_vertex, edge)  # Add the edge to the 'from_vertex' neighbor list
        self.vertices[to_vertex].add_neighbor(from_vertex, edge)  # Add the edge to the 'to_vertex' neighbor list
        self.edges.append(edge)  # Append the edge to the list of edges in the graph

    def add_intersections(self, intersections):  # define a function to add intersections to the graph
        for intersection_id, intersection_data in intersections:  # iterate over each intersection and its data
            self.vertices[intersection_id] = Vertex(intersection_data['id'])  # create a new vertex object for each intersection and add it to the vertices dictionary


# Define your graph
graph = Graph()

# Add intersections (vertices) with IDs
intersections = [
    ('A', {'id': 'A'}),
    ('B', {'id': 'B'}),
    ('C', {'id': 'C'}),
    ('D', {'id': 'D'}),
    ('E', {'id': 'E'}),
    ('F', {'id': 'F'}),
    ('G', {'id': 'G'}),
    ('H', {'id': 'H'}),
    ('I', {'id': 'I'}),
    ('J', {'id': 'J'}),
    ('K', {'id': 'K'}),
    ('L', {'id': 'L'}),
    ('M', {'id': 'M'}),
    ('N', {'id': 'N'}),
    ('O', {'id': 'O'}),
    ('P', {'id': 'P'}),
    ('Q', {'id': 'Q'}),
    ('R', {'id': 'R'}),
    ('S', {'id': 'S'}),
    ('T', {'id': 'T'})
]

# Add intersections to the graph
graph.add_intersections(intersections)

# Add roads (edges)
# Defining roads along with their attributes
roads = [
    ('A', 'B', 'AB', 'Al Asayil St', 5, [('H1', False), ('H2', False), ('H3', False)]),
    ('B', 'C', 'BC', 'Al Aswaq St', 7, [('H4', False), ('H5', False)]),
    ('C', 'D', 'CD', 'Al Basamat St', 4, []),
    ('D', 'E', 'DE', 'Al Fursan St', 6, [('H6', False)]),
    ('E', 'F', 'EF', 'Al Hamalan St', 8, []),
    ('F', 'G', 'FG', 'Al Khillan St', 3, [('H7', False)]),
    ('G', 'H', 'GH', 'Al Mawaqid St', 5, [('H8', False)]),
    ('H', 'I', 'HI', 'Al Muazaz St', 4, []),
    ('I', 'J', 'IJ', 'Al Mufrad St', 7, []),
    ('J', 'K', 'JK', 'Al Mustaqbal St', 10, [('H9', False)]),
    ('K', 'L', 'KL', 'Al Nakhlah St', 6, [('H10', False)]),
    ('L', 'M', 'LM', 'Al Sadih St', 8, []),
    ('M', 'N', 'MN', 'Al Sarhan St', 9, [('H11', False), ('H12', False), ('H13', False)]),
    ('N', 'O', 'NO', 'Al Shamikheen St', 5, []),
    ('O', 'P', 'OP', 'Al Shamsi St', 7, [('H14', False)]),
    ('P', 'Q', 'PQ', 'Al Waqf St', 6, []),
    ('Q', 'R', 'QR', 'Al Yahhal St', 8, []),
    ('R', 'S', 'RS', 'Al Zaffi St', 9, [('H15', False)]),
    ('S', 'T', 'ST', 'Al Sihayli St', 10, [('H16', False)]),
    ('T', 'A', 'TA', 'Mreefah St', 14, []),
    ('A', 'F', 'AF', 'Nakhi St', 10, []),
    ('B', 'H', 'BH', 'Al Shibaykah St', 9, []),
    ('C', 'J', 'CJ', 'st 10', 9, []),
    ('D', 'L', 'DL', 'Rayyana Avenue', 11, []),
    ('E', 'N', 'EN', 'Al Marmouq st', 4, []),
    ('F', 'P', 'FP', 'Al Yasir st', 7, []),
    ('G', 'R', 'GR', 'st 20', 10, []),
    ('H', 'T', 'HT', 'st 30', 12, [('H17', False), ('H18', False)])
]

for road in roads:
    graph.add_edge(*road)

# Create a NetworkX graph
G = nx.Graph()

# Add roads (edges) with house information to the graph
for edge in graph.edges:
    house_info = ', '.join([f'{house} (Delivered)' if is_delivered else f'{house}' for house, is_delivered in edge.houses])
    edge_label = f"{edge.name} ({edge.length})\nHouses: {house_info}"
    G.add_edge(edge.id[0], edge.id[1], id=edge.id, label=edge_label)

# Draw the graph
plt.figure(figsize=(14, 14))  # Larger figure size
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='pink', node_size=1000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the graph
plt.show()
