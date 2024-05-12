# What is the Big O of the below function? (Hint, you may want to go line by line)
def anotherFunction():
    pass


def funChallenge(input):
    a = 10  # assignment = 0(1)
    a = 50 + 3  # re-assignment = 0(1)

    for item in len(input):  # loop = 0(n)

        anotherFunction()  # function = 0(n)
        stranger = True  # function = 0(n)
        a += 1  # increment = 0(n)
    return a  # return = 0(1)


funChallenge(input)  # function = 0(1)

# Big O Notation: 4 steps + 4n = O(n)
