"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #My code
    #Making copy for original list
    arr = lst.copy()
    #Goes through list
    for i in range(len(arr) - 1):
        #Any swaps occur?
        swapped = False

        #Compare neighbor elements.
        #The largest unsorted value moves toward the end after each pass.
        for j in range(len(arr) - 1 - i):
            # Switch values if they are out of order.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        #If no swaps happens, list is sorted
        if not swapped:
            break
        # Return the sorted copy of the list
        return arr
    pass


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #My Code
    #List with zero or one element already in order
    if len(lst) <= 1:
        return lst.copy()

    #Locate middle position of list
    middle = len(lst) // 2

    #Divide list forming two smaller halves
    left = lst[:middle]
    right = lst[middle:]

    # Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    #Merge two sorted halves together
    return merge(left_sorted, right_sorted)
    pass


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    #My Code
    #Empty list for the sorted result
    result = []

    #Indexes for left and right lists.
    left_index = 0
    right_index = 0

    #Compare values while both lists still contain values.
    while left_index < len(left) and right_index < len(right):

        #Add smaller value to the result
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    #Include remaining values from the left list, if any
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    #Include remaining values from the right list, if any.
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    #Return combined sorted list.
    return result
    pass


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.
    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    
    #My code
    #Unsorted list with 8 values.
    dataset1 = [60, 29, 28, 22, 11, 96, 41, 38]

    #Original list shown
    print("Original list:", dataset1)

    #Sort list w/ Bubble Sort
    bubble_result1 = bubble_sort(dataset1)

    #Sort list w/ Merge Sort
    merge_result1 = merge_sort(dataset1)

    #Show both results
    print("Bubble Sort result:", bubble_result1)
    print("Merge Sort result:", merge_result1)

    #Compare results of both algorithms.
    print("Both Results Compared:", bubble_result1 == merge_result1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.
    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    #My Code
    #2nd dataset with different values
    dataset2 = [32, 12, 40, 9, 77, 21, 63, 12, 49]

    #Show original list
    print("Original list:", dataset2)

    #Sorting second dataset w/ Bubble Sort.
    bubble_result2 = bubble_sort(dataset2)

    # Sorting second dataset w/ Merge Sort.
    merge_result2 = merge_sort(dataset2)

    #Show both results.
    print("Bubble Sort result:", bubble_result2)
    print("Merge Sort result:", merge_result2)

    #Compare results from both algorithms.
    print("Both Results Compared:", bubble_result2 == merge_result2)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.
    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #My Code
    #Edge Case 1--Empty list.
    #Both algorithms return an empty list without errors
    empty_list = []
    print("\n1. Empty list:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))

    # Edge Case 2--Already sorted list.
    #Bubble Sort can stop early if no swaps are needed
    already_sorted = [10, 22, 34, 40, 54]
    print("\n2. Already sorted list:")
    print("Original:", already_sorted)
    print("Bubble Sort:", bubble_sort(already_sorted))
    print("Merge Sort:", merge_sort(already_sorted))
if __name__ == "__main__":
    main()
