"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #My Code
    #O(n) because in the worst, might have to go by every item in the list.
     for i in range(len(lst)):
        if lst[i] == target:
            return i
    pass


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
#My code
#Starting and ending positions for search area.
       left = 0
       right = len(lst) - 1

    while left <= right:
        #Middle position of the current search area.
        middle = (left + right) // 2

        #See whether middle value is target.
        if lst[middle] == target:
            return middle

        #If target is larger than the middle value, remove left half of search space.
        elif lst[middle] < target:
            left = middle + 1

        #If the target is smaller than the middle value, remove right half of search space.
        else:
            right = middle - 1
        #Every iteration gets rid of half of the remaining values, pertaining to binary search with O(log n) time.
        return -1
    pass


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

#Dataset of student grades
    small_data = [65, 70, 75, 80, 85, 90, 95]

    print("Student grades:", small_data)

    # Test a grade that exists in the list.
    target = 85

    linear_result = linear_search(small_data, target)
    binary_result = binary_search(small_data, target)

    print("\nSearching for target grade:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms find 85 at index 4.
    # Linear search looks for each grade from start.
    # Binary search looks for middle and removes half of remaining search area each time.

    # Test a grade that does not exist.
    target = 97

    linear_result = linear_search(small_data, target)
    binary_result = binary_search(small_data, target)

    print("\nSearching for grade:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    #Both searches return -1 because 88 is not in the list.
    #Linear search looks at all grades prior to deciding whether grade is not present.
    # Binary search removes half of the list during each step.
    #End of small dataset code


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

#Large sorted dataset of employee IDs.
    large_data = list(range(1000, 11000))

    print("Employee ID dataset holds", len(large_data), "values.")

    #Search for an employee ID near end of the list.
    #Linear search will have to check multiple values before finding particular ID.
    target = 10950

    linear_result = linear_search(large_data, target)
    binary_result = binary_search(large_data, target)

    print("\nSearching for employee ID:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms find the employee ID.
    # Linear search has O(n) time complexity because it potentially needs to go through every item in the list
    # Binary search has O(log n) time complexity because each iteration removes half of the remaining values

    
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

# EDGE CASE 1: Empty list
    empty_list = []

    print("\n1. Empty list:", empty_list)
    print("Linear search for 100:", linear_search(empty_list, 100))
    print("Binary search for 100:", binary_search(empty_list, 100))
    # Both algorithms return -1 because there are no values in the list to search.


    # EDGE CASE 2: Single-element list
    single_list = [42]

    print("\n2. Single-element list:", single_list)
    print("Searching for 42:")
    print("Linear search:", linear_search(single_list, 42))
    print("Binary search:", binary_search(single_list, 42))
    # Both algorithms return index 0 because 42 is the only
    # item in the list.


    # EDGE CASE 3: Target is not present
    edge_list = [15, 25, 35, 45, 55]

    print("\n3. Target not present:", edge_list)
    print("Searching for 40:")
    print("Linear search:", linear_search(edge_list, 40))
    print("Binary search:", binary_search(edge_list, 40))
    # Both algorithms return -1 because 40 is not in the list.


    # EDGE CASE 4: Target is the last value
    print("\n4. Target at the last position:", edge_list)
    print("Searching for 55:")
    print("Linear search:", linear_search(edge_list, 55))
    print("Binary search:", binary_search(edge_list, 55))
    #Linear search must check each item from the beginning before finding 55 at the last position.
    #Binary search can reach the target much faster because it removes half of the search area each time.
   
    print("\n=== Last COMPARISON ===")
    print("Linear Search: O(n)")
    print("Binary Search: O(log n)")
    print("Linear search works on sorted or unsorted lists, but it")
    print("Might check every element.")
    print("Binary search is faster for large datasets, but the")
    print("list must already be sorted.")
    print("As the dataset grows, binary search becomes more")
    print("efficient because each search reduces the search")
    print("space by about half.")

if __name__ == "__main__":
    main()
