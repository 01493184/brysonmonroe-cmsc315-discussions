# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment helped learn how a Binary Search Tree stores and manages info. One of the main topics I learned is that values smaller than the current node are placed on the left, while the larger values are placed on the right. I also gained practice with recursive methods for inserting and finding values. In addition, I learned how an in-order traversal works. By visiting the left subtree, the current node, and then the right subtree, the values are shown in numerical order.

2. What challenges did you encounter, and how did you overcome them?
At first, recursion was one of the more challenging parts of the assignment because I had to understand how the program moves from one node to another. I worked through this by looking at the tree one step at a time and testing different values to see where they were placed. Doing the search method for both existing and missing values also helped me understand how the BST makes decisions.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
A BST can improve efficiency because its ordering allows the program to remove parts of the tree during a search. A balanced BST can search in about O(log n) time, compared with O(n) for a basic linear search. However, an unbalanced BST can be less efficient when it comes to results.
