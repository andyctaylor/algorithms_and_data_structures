# Algorithm to log all pairs of an array

# This means log the following:
# 1.2, 1.3, 1.4, 1.5 then 2.1, 2.2, 2.3, 2.4, 2.5  etc

# Psudocode
"""
FUNCTION log_all_pairs(array):
    FOR EACH element1 AT index i IN array:
        FOR EACH element2 AT index j IN array, STARTING FROM i + 1:
            LOG (element1, element2) 

Prints all unique pairs of elements from a given array.

    This function iterates through the array, pairing each element with all subsequent
    elements to its right. It avoids duplicate pairs and pairs of the same element.

    Args:
        array: The input list or array of elements.

    Time Complexity: O(n^2) due to nested loops.
    Space Complexity: O(1) as it only uses constant extra space for the loop variables.
"""

# Our Array
letters = ["a", "b", "c", "d", "e"]


# Here is function
def log_all_pairs(array):

    # Outer loop: Iterates over each element (item) in the array and also
    # keeps track of the index (i) using 'enumerate'.
    for i in range(len(array)):

        # Inner loop: Starts from the element immediately after the current 'item'
        for j in range(len(array)):
            print(array[i], array[j])


log_all_pairs(letters)
# Big O Notation is O(n*2)
