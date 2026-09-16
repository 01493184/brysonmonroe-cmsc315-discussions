"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    
    #My code
    #Dictionary stores data as key-value pairs.
    #Key identifies item and the value stores its data.
    products = {}
    #5 products with prices.
    products["Laptop"] = 850
    products["Keyboard"] = 45
    products["Mouse"] = 25
    products["Monitor"] = 220
    products["Headphones"] = 60
    # Display dictionary after adding the products.
    print("Product dictionary:", products)


    
    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.
    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    #My code
    #Using product name as key to find price.
    #Dictionary quickly finds value connected to requested key.
    laptop_price = products["Laptop"]
    monitor_price = products["Monitor"]

    
    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.
    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    #My code 
    print("Before update:", products)
    #Changing price of existing product.
    #Giving existing key a new value that will swap the old value.
    products["Keyboard"] = 50
    print("After updating Keyboard:", products)


    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:", products)

    # Change the price of an existing product.
    # Giving an existing key a new value replaces the old value.
    products["Keyboard"] = 50
    print("After updating Keyboard:", products)



    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    
    #My code
    #Remove headphones from the dictionary.
    #Both the key and its value are removed.
    del products["Headphones"]
    print("After deleting Headphones:", products)

    
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    # Explain what happens in each case.
    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")
    
    #My Code
    #Edge Case 1: Looks up key not in the dictionary.
    #get() returns None when key cannot be found.
    missing_product = products.get("Tablet")
    print("Looking up Tablet:", missing_product)
    print("Tablet not found in the dictionary, so the result is None.")

    #Edge Case 2: Add new key that was not already present.
    #Assigning a value to a new key adds it to the dictionary.
    products["Tablet"] = 300
    print(When Tablet was added:", products)

    #Edge Case 3: Delete item that doesn't exist.
    if "Printer" in products:
        del products["Printer"]
        print("Printer was removed.")
    else:
        print("Printer not found, nothing deleted.")


if __name__ == "__main__":
    main()
