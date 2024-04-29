from Graphs import *

from collections import deque  # Importing deque from collections module for implementing queues
def bfs_package_distribution(graph, start):  # define a function to perform package distribution using breadth-first search (BFS)
    visited = set()  # initialize a set to keep track of visited road indices
    queue = deque([(start, 0)])  # Initialize a deque to store (current_road_index, level) tuples for BFS traversal
    paths = {}  # Initialize a dictionary to store package distribution paths

    while queue:  # execute BFS until the queue is empty
        current_road_index, level = queue.popleft()  # dequeue the next road index and its level

        if current_road_index in visited:
            continue  # skip if the current road index has been visited before

        visited.add(current_road_index)  # mark the current road index as visited
        road_data = graph.edges[current_road_index]  # get data of the current road
        for house, is_delivered in road_data.houses:
            if level not in paths:
                paths[level] = []  # initialize an empty list for houses at the current level
            if not is_delivered:
                paths[level].append(house)  # add undelivered houses to the current level

        for neighbor_index, edge in enumerate(
                graph.edges):  # iterate through edges to find neighbors of the current road
            if edge.id[0] == graph.edges[current_road_index].id[1]:  # check if the starting vertex of the edge matches the ending vertex of the current road
                queue.append((neighbor_index, level + 1))  # enqueue neighbor road with increased level

    return paths  # return the paths dictionary containing package distribution information


# Print package distribution using level-by-level BFS
print("Package distribution using level-by-level BFS:")
paths = bfs_package_distribution(graph, 0)  # Starting from road 'A' to 'B'
for level, houses in paths.items():  # iterate through the paths dictionary to print package distribution at each level
    print(f"Level {level}: {houses}")  # print the level and corresponding houses
