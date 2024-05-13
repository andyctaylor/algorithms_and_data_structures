# Space complexity O(1)
def boooo(n):
    for iten in range(0, len(n)):  # Corrected the variable name (item)
        print("booooo")


boooo([1, 2, 3, 4, 5])
# The space complexity of this Big O Notation is: O(1)
"""
Key Point: Even though the function iterates over the input list, 
the space complexity is O(1) because we're not creating any new data 
structures that scale with the input size.
"""


# Space complexity O(n)
def array_of_hi(m):
    hi_array = []  # Data structure = 1

    for i in range(m):  # Variable (i) = 1  &  Data structure (Loops) = 1
        # Data structure (Each item is an additional memory space) = n
        hi_array.append("hi")
    return hi_array


results = array_of_hi(6)
print(results)
# The space complexity of this Big O Notation is: O(n)
