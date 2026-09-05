"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        #My code
        #Node has data and could have two possible child nodes
        #New nodes start without children.
        self.value = value
        self.left = Empty
        self.right = Empty
        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        #My Code
        # The root is first node in the tree.
        self.root = Empty
        pass

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        #My code
        # Recursive method allows new value to move in and return tree format
        self.root = self._insert_recursive(self.root, value)
        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #My Code
        # If there's no node, a new value would be placed here.
        if node is Empty:
            return Node(value)
        
        #Smaller values belong on the left side.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        
        #Larger values go on right side.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
            return Node
        pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #My Code
        #Starts search at root node.
        return self._search_recursive(self.root, value)
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        #My code
        #If empty position, value does not exist.
        if node is Empty:
            return False

        #Value matches current node, so it was found.
        if value == node.value:
            return True

        # If target node is smaller, only left side needs to be checked
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Else the target must be larger, therefore check right.
        return self._search_recursive(node.right, value)
        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        #My Code
        result = []
        #Helper fills list in the correct traversal order.
        self._inorder_recursive(self.root, result)
        return result
        pass

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        #My Code
        #Nothing to visit when the node is empty.
        if node is Empty:
            return

        #Checking left side first.
        self._inorder_recursive(node.left, result)

        #Keep track of current node's value.
        result.append(node.value)

        #Visit the right side lastly.
        self._inorder_recursive(node.right, result)
        pass


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    #My Code
    #Start with an empty binary search tree.
    #The first value becomes the root.
    #Smaller numbers are placed on the left, while larger numbers are placed on the right.
    tree = BST()
    #The number listed make nodes on both sides of the root.
    numbers = [45, 25, 65, 15, 35, 55, 75]
    for number in numbers:
        tree.insert(number)
    print("Values inserted are:", numbers)


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.
    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    
    #My Code
    # Retrieving values from the BST using in-order traversal.
    # In-order traversal visits the left side first, then current node, and finally the right side.
    ordered_values = tree.inorder()
    print("Values from smallest to largest:", ordered_values)


    
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.
    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    #My Code
    #The first two searches return True because those values are in the tree.
    #The last two return False because those values do not exist.
    
    #Checks for values that are already stored in the tree.
    print("Looking for 35:", tree.search(35))
    print("Looking for 75:", tree.search(75))
    
    #Checks for values that were never inserted in tests.
    print("Looking for 20:", tree.search(20))
    print("Looking for 90:", tree.search(90))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    #My Code
    #Makes a separate BST that has only one value.
    single_tree = BST()
    single_tree.insert(100)

    #Shows the contents of the tree.
    print("One-node tree:", single_tree.inorder())

    #Searches for the value that was inserted.
    print("Searching for 100:", single_tree.search(100))

    #Searches for a value that is not in the tree.
    print("Searching for 50:", single_tree.search(50))
if __name__ == "__main__":
    main()
