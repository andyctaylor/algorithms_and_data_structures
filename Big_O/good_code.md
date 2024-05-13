# What is good code?

The definition of good code lies in the below.

- Readable
- Scalable

# The 3 pillars of code

1.  Readable & Clean Code
2.  Speed & Time Complexity
3.  Memory & Space Complexity

# Scalable

As an engineer there are 2 things you need to consider for scalability.
Speed is usually dictated by the CPU power and RAM of the computer.

## Speed:

One of the valuable resources we consider when coding is time and speed.

- How fast is our runtime on the code?
- How many operations does it cost?
- How long does it take our function to run?

## Memory

Another one of the valuable resources is memory usage and expenditure.

# Space Complexity

Space complexity measures how much memory an algorithm uses relative to its input size. It focuses on the additional memory used during execution, not the memory occupied by the input itself. Here's a breakdown of the key points.

## Memory Areas: Algorithms primarily use two memory areas:

- Stack: Stores function calls, local variables, and return addresses. It has limited size.
- Heap: Stores dynamically allocated data (objects, arrays, etc.). It's larger and flexible.

## What It Measures:

1.  Auxiliary Space: The extra space an algorithm uses beyond the input. This includes temporary variables, recursive function calls, and data structures created during execution.
2.  Input Space: The memory used to store the input data itself. This is typically not considered when analyzing space complexity.

## Why It Matters: Understanding space complexity helps:

1.  Predict Memory Usage: Know if your algorithm will run out of memory with large inputs
2.  Optimize Algorithms: Choose algorithms with lower space complexity if memory is a constraint.
3.  Compare Algorithms: Evaluate the trade-offs between time and space complexity of different solutions.

## What causes space complexity

- Adding Variables
- Adding Data Structures
- Function Calls
- Allocations

# Examples:

Imagine your box compression function creates a new array to store the compressed data. The size of this array depends on the number of boxes being compressed (the input size).

- Scenario 1: Small Input: If you only have a few boxes, the new array will be small, and your function will use minimal memory.
- Scenario 2: Large Input: If you have thousands of boxes, the new array will be huge. This could cause your function to exceed the available memory and crash.

# Big O notation usage

The relationship between the input size and the size of the new array is what we analyze in space complexity. We typically use Big O notation to express this relationship, such as:

- O(1): Constant space. The algorithm uses a fixed amount of memory, regardless of input size.
- O(n): Linear space. The memory usage grows proportionally to the input size.
- O(n^2): Quadratic space. The memory usage grows with the square of the input size.

# Code Examples

See the Space_complexity_examples.py

## Example 1:

The hi_array list is the main contributor to space complexity.
Each time the loop runs, a new "hi" string is added to the list, making the list grow in proportion to the input m.

### Key Point:

1.  The loop variable i and the loop itself do use a small amount of memory, but their space usage is constant and doesn't change with the input size.
2.  The O(n) space complexity comes from the growing size of the hi_array list.

## Example 2:

The hi_array list is the main contributor to space complexity. Each time the loop runs, a new "hi" string is added to the list, making the list grow in proportion to the input m.

### Key Point:

1.  The loop variable i and the loop itself do use a small amount of memory, but their space usage is constant and doesn't change with the input size.
2.  The O(n) space complexity comes from the growing size of the hi_array list.
3.  The space complexity of array_of_hi(m) is O(n) because the function creates a list hi_array whose size directly depends on the input m.
4.  As the input increases, the list grows linearly, using more memory. 