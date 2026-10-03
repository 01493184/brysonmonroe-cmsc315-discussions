# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment helped me understand how graphs can be represented and explored using BFS. I learned how an adjacency list can be used to show which nodes are connected to each other. I also learned how a queue controls the order of the search and why keeping track of visited nodes is important. One of the main things I understood from this assignment is that BFS explores the graph one level at a time rather than going as far as possible down one path.

2. What challenges did you encounter, and how did you overcome them?
The part I found most challenging was understanding the order in which BFS processes each node. I had to pay attention to how nodes were placed into the queue and then removed using popleft(). Testing the program with different starting points helped me understand the process better. I also used edge cases, such as starting with a node that had no connections, to make sure my function behaved correctly. Working through these examples helped me identify and fix problems in my code.

3. Compare BFS and DFS conceptually and describe real-world applications and use cases.
   Both methods have practical uses. BFS could be useful in a social network for finding connections between people or in a map application for finding a path with the fewest stops. DFS could be useful for searching through folders and subfolders on a computer, exploring a maze, or examining connected parts of a system. The best method depends on what the program needs to accomplish and how the graph is structured.

