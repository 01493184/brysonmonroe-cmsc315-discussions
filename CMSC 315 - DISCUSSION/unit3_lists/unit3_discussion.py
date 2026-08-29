"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    #My Code
    #Insert() function puts new value at the specified index
    #Elelements already there are moved one spot to the right to create more space for next element
    lst.insert(index, value)
    pass
    


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.
    
    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    #My Code
    #Approves index before removing so program doesn't grow an IndexError when called position does not exist.
    if index < 0 or index >= len(lst):
        return None
    #when item goes away, elements shift to the left one-by-one to fill gaps
    return lst.pop(index)
    pass


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    #My Code
    #Using linear search to see rate of growth
    for index in range(len(lst)):
        #Compares current element with the value that is being founded
        if lst[index] == value:
            return index
        #Just in case loop exits without narrowing down a value
        return -1
    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.
   
    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    #Here's a list of different fruits for insertion method
    fruits = ["apple", "banana", "orange", "grape"]

    #Shows list before changes.
    print("Original list:", fruits)

    # Inserting new fruit at start of list.
    # Original fruits shift one position to the right.
    insert_at(fruits, 0, "pineapple")
    print("After inserting 'pineapple' at the beginning:", fruits)

    # Insert another fruit in the middle of the list.
    # Elements from that position onward move one position to the right.
    insert_at(fruits, 3, "pair")
    print("After inserting 'pair' in the middle:", fruits)

    # Insert a fruit at the end of the list.
    # Because there are no elements after the insertion point, very little
    # shifting is needed.
    insert_at(fruits, len(fruits), "plum")
    print("After inserting 'plum' at the end:", fruits)
 
    
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # List of animals for the deletion method.
    animals = ["dog", "cat", "rabbit", "horse", "turtle"]

    print("Original list:", animals)

    # Deleting first item on list.
    # The animals left shift one position to the left.
    removed = delete_at(animals, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", animals)

    # Deleting middle item on list.
    # Elements after the removed item shift one spot to the left to fill a position.
    removed = delete_at(2)
    print("Removed from middle:", removed)
    print("Updated list:", animals)

    # Deleting final item on list.
    # There are no more elements after it, no other elements need to shift.
    removed = delete_at(2)
    print("Removed from end:", removed)
    print("Updated list:", animals)
    print
    
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    #List of school subjects for the search method.
    subjects = ["math", "science", "history", "art", "music"]

    print("List being searched:", subjects)

    # Search the subject that exists in the list.
    # Searches elements from left to right until "art" is found.
    result = search_value(subjects, "art")
    print("Searching for 'art': index", result)

    # Search for a subject that is not in the list.
    # Every element is checked, so function returns -1.
    result = search_value(subjects, "anatomy")
    print("Searching for 'anatomy': index", result)


    
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.
    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    #EDGE CASE 1:
    #Deleting an item using an index that does not exist.
    #Checks the index first and returns None
    numbers = [10, 20, 30]
    print("Original numbers:", numbers)
    removed = delete_at(numbers, 10)
    print("Delete index 10:", removed)
    print("List after invalid deletion:", numbers)

    
    # EDGE CASE 2:
    # Insert into an empty list.
    # Index 0 is the beginning of the empty list, so the new value is the only element.
    empty_list = []
    print("Empty list before insertion:", empty_list)
    insert_at(empty_list, 0, "first item")
    print("Empty list after insertion:", empty_list)

    
    # EDGE CASE 3:
    # Search for a value in an empty list.
    # There are no elements to check, so function returns -1.
    another_empty_list = []
    result = search_value(another_empty_list, "missing")
    print("Searching an empty list for 'missing':", result)


if __name__ == "__main__":
    main()
