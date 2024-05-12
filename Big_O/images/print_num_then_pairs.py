# Print numbers and then print pairs.

# The Array
new_array = [1, 2, 3, 4, 5]


def print_numbers_then_pairs(array):

    # There are a total of three loops here but only one variable. So we need only variable for our Big-O notation

    print("The numbers are : ")  # O(1)
    for i in range(len(array)):  # O(n)
        print(array[i])  # n*O(1)

    print("The pairs are :")  # O(1)
    for i in range(len(array)):  # n*O(n)
        for j in range(len(array)):  # n*O(n)
            print(array[i], array[j])  # n*n*O(1)


print_numbers_then_pairs(new_array)
