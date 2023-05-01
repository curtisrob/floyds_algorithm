import sys

NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]


def floyd_recursive(input_graph):
    """
    Floyd's algorithm for finding the shortest path between all pairs of nodes in a graph.
    Coded recursively.
    """
    distance = [row[:] for row in input_graph]

    n = len(distance)

    # If there are no nodes in the graph, return from the function
    if n == 0:
        return

    # Iterate through all pairs of nodes and calculate the shortest distance between them
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # If there is no path between nodes i and k or nodes k and j, continue
                if distance[i][k] == NO_PATH or distance[k][j] == NO_PATH:
                    continue

                # Calculate the distance between nodes i and j via node k
                new_dist = distance[i][k] + distance[k][j]

                # If the new distance is shorter than the current distance, update the distance matrix
                if new_dist < distance[i][j]:
                    distance[i][j] = new_dist

    # Recursively call the function on the subgraph with one fewer node
    floyd_recursive(distance[:-1][:-1])

    # Return the distance matrix
    return distance


shortest_path = floyd_recursive(graph)
