# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment helped me understand how dictionaries work as hash tables. I practiced creating a dictionary and adding different key-value pairs to it. I also learned how to find a value by using its key, change an existing value, and remove information from the dictionary. These operations helped me better understand how data can be suitable to manage.

2. What challenges did you encounter, and how did you overcome them?
   One difficulty I had was working with keys that were not in the dictionary. I learned that using get() is a safe way to search for a missing key because it returns None instead of causing an error. I also had to learn how to safely remove a key that does not exist by checking for it first. With resolving these issues, testing each part of the code helped me find and fix these issues.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
Hash tables organize data by using keys to find the values. A collision happens when two keys are designated to go to the same location. Hash tables handle these collisions so the information can still be accessed. Because of this process, hash tables can find data much faster than checking every item individually. This makes them useful when a program needs to work with a lot of information.
