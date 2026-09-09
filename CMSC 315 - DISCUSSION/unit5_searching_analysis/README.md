# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
After I finished this assignment, I now understand how different search algorithms work and why they have their time complexities. I learned that linear search examines items one at a time, starting from the beginning of the list. Because every item potentially has to be checked, its time complexity is O(n). Binary search works in another way by checking the middle value and it eliminates half of the remaining search area during each step. This gives binary search an O(log n) time complexity. 

2. What challenges did you encounter, and how did you overcome them?
One challenge I experienced was getting managing binary search code. Basically, I had to make sure the left and right values were updated properly and that return -1 was placed outside the loop. I solved these problems by looking carefully at each step of the algorithm and testing the code with different types of values and edge cases.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
Linear search is useful when working with smaller or unsorted lists because it's not super hard and it does not require the data to be organized. Binary search is a better choice for larger sorted datasets because it can find info much more quickly. However, the data must be sorted first. Overall, this assignment taught me how algorithm choice can improve program performance and make searching large amounts of data more efficient.
   
