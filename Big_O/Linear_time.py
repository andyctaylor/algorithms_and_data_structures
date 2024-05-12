# All of our list variables.
fish = ["dory", "bruce", "marlin", "nemo"]
nemo = ["nemo"]
everyone = [
    "dory",
    "bruce",
    "marlin",
    "nemo",
    "gill",
    "bloat",
    "nigel",
    "squirt",
    "darla",
    "hank",
]
# This generates a sequence of numbers from 0 up to (but not including) 100
large = ["nemo" for i in range(10000)]


# Define a function called 'find_nemo' that takes a list (called 'array') as input
def find_nemo(array):

    # Iterate through each index ('i') in the list, from 0 up to the length of the list (not including the last item)
    for i in range(0, len(array)):
        # Check if the item at the current index 'i' is equal to the string "nemo"
        if array[i] == "nemo":
            # If "nemo" is found, print this message and exit the function
            print("Found Nemo!!")
            print(large)
            return  # Early exit since we've found Nemo
    # If the loop finishes without finding "nemo", print this message (this is outside the loop)
    print("Nemo not found")


# Calling the find_nemo function with the nemo list as an argument.
find_nemo(large)
