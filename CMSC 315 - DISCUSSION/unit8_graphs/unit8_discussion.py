"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    
    #My code
    #If called starting point is not present in graph, nothing is left to discover.
    if start not in graph:
        return []
    #Keep track of nodes that have already been discovered.
    visited = set()
    #BFS relies on a queue so the earliest discovered node is handled first.
    queue = deque()
    #Begin the search with the selected starting node.
    visited.add(start)
    queue.append(start)
    #This list will contain the final order of the search.
    order = []

    while queue:
        #Take the oldest item from the queue.
        current_node = queue.popleft()

        # Save the node in the order it was processed.
        order.append(current_node)

        #View all nodes directly connected to current node.
        for neighbor in graph[current_node]:

            #Only add a neighbor if it wasn't found yet.
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
    pass


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.
    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    #My Code
    # The graph uses an adjacency list, where each computer
    # stores a list of computers it is connected to.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    
    
    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.
    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")
   
    #My Code
    starting_node = "A"
    #Run BFS beginning with node A.
    visited_order = bfs(graph, starting_node)
    
    #Starting point and the order the nodes were reached.
    print(f"Starting node: {starting_node}")
    print(f"Nodes visited: {visited_order}")
    
    #Another connection to the graph.
    #Update both nodes.
    graph["A"].append("F")
    graph["F"].append("A")
    
    print("\n=== BFS AFTER ADDING A NEW CONNECTION ===")
    updated_order = bfs(graph, starting_node)
    print(f"Starting node: {starting_node}")
    print(f"Updated visit order: {updated_order}")

    

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.
    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #Edge Case 1
    # Changing the starting location can change the order
    # in which the nodes are discovered.

    another_start = "D"
    result_one = bfs(graph, another_start)

    print("\n1. Starting from another computer:")
    print(f"Starting point: {another_start}")
    print(f"Visit order: {result_one}")

    #Edge Case 2
     small_graph = {
        "A": []
    }
    result_four = bfs(small_graph, "A")
    print("\n4. Graph containing one node:")
    print(f"Graph: {small_graph}")
    print(f"Visit order: {result_four}")

if __name__ == "__main__":
    main()
