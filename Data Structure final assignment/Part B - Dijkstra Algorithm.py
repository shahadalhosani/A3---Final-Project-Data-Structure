from Graphs import * # used in pycharm when we want to connect a file that we are working with to a seperate file to avoid any errors, in this case it is the Graph file

import heapq  # Importing heapq for implementing heaps
def dijkstra(graph, start, end):  # define a function to find the shortest path using Dijkstra's algorithm
    distances = {vertex: float('infinity') for vertex in graph.vertices}  # initialize distances dictionary with all vertices set to infinity
    distances[start] = 0  # set the distance of the starting vertex to 0
    previous = {}  # To store the previous vertex for each vertex
    queue = [(0, start)]  # initialize a priority queue with (distance, vertex) tuples

    while queue:  # a while loop to execute Dijkstra's algorithm until the priority queue is empty
        current_distance, current_vertex = heapq.heappop(queue)  # pop the vertex with the smallest distance from the priority queue using the .pop() function

        if current_vertex == end: # checks if the current vertex is the end vertex
            break  # if it is, exit the loop

        for neighbor, edge in graph.vertices[current_vertex].adjacent.items(): # a for loop to iterate through the neighbors of the current vertex
            weight = edge.length  # get the weight of the edge, which is also the length between the intersections(nodes)
            distance = current_distance + weight  # calculate the total distance to the neighbor by adding the current distance with the weight(length of the edge)

            if distance < distances[neighbor]:  # check if the new distance is smaller than the current distance to the neigbhbot
                distances[neighbor] = distance  # if it is, update the distance to the neighbor
                previous[neighbor] = current_vertex  # Update previous vertex
                heapq.heappush(queue, (distance, neighbor))  # then push the neighbor to the priority queue with its updated distance

    # now that we found the shortest distance we can know the shortest path (from which node letter to which)
    shortest_path = []  # initialize an empty list to store the vertices of the shortest path
    current_vertex = end  # start from the end vertex
    while current_vertex != start:  # continue until reaching the start vertex
        shortest_path.append(current_vertex)  # append the current vertex to the shortest path
        current_vertex = previous[current_vertex]  # move to the previous vertex using the 'previous' dictionary
    shortest_path.append(start)  # append the start vertex to the shortest path (to complete the path)
    shortest_path.reverse()  # reverse the path to get it in the correct order

    return distances[end], shortest_path  # return the shortest distance and path between two intersections


# Test case 1 - Find Shortest distance and path
start_vertex = 'C'  # define the starting vertex
end_vertex = 'T'  # define the end vertex
shortest_distance, shortest_path = dijkstra(graph, start_vertex, end_vertex)  # find the shortest distance using Dijkstra's algorithm
print("\nShortest distance from", start_vertex, "to", end_vertex, ":", shortest_distance)  # print the shortest distance
print("Shortest path:", shortest_path)  # print the shortest path

# Test case 2 - Find Shortest distance and path
start_vertex = 'A'  # define the starting vertex
end_vertex = 'D'  # define the end vertex
shortest_distance, shortest_path = dijkstra(graph, start_vertex, end_vertex)  # find the shortest distance using Dijkstra's algorithm
print("\nShortest distance from", start_vertex, "to", end_vertex, ":", shortest_distance)  # print the shortest distance
print("Shortest path:", shortest_path)  # print the shortest path

# Test case 3 - Find Shortest distance and path
start_vertex = 'B'  # define the starting vertex
end_vertex = 'F'  # define the end vertex
shortest_distance, shortest_path = dijkstra(graph, start_vertex, end_vertex)  # find the shortest distance using Dijkstra's algorithm
print("\nShortest distance from", start_vertex, "to", end_vertex, ":", shortest_distance)  # print the shortest distance
print("Shortest path:", shortest_path)  # print the shortest path
