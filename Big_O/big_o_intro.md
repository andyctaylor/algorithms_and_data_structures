# Big O asymptotic analysis

In the world of analyzing algorithms and their efficiency (how well they perform as the amount of data they handle grows), Big O notation is our tool. It helps us express how the runtime (how long an algorithm takes to finish) changes as the input size (the amount of data) increases.

1.  O(1): Super fast, like finding a book on your desk. The time stays the same no matter how many books you have.
2.  O(n): Takes longer with more data, like reading through each book on a shelf.
3.  O(n log n): A bit slower than O(n), like sorting your bookshelf.
4.  O(n^2): Even slower with more data, like comparing every book to every other book on your shelf.

- Helps us to figure out how long a code block or algorithm takes to run.
- it tells us how well a problem is solved, Basically helps
  us to distinguish good code from bad code.
- Big O Notation allows us to measure the scalability of our code.
  i.e: Giving our machines instructions through code to do something
  that would produce a desired result.

# Big O notation diagram

![This is a diagram Big O notation ](./images/Big_O.jpeg)

1.  This Diagram represents when we grow bigger with our input/elements i.e: 'nemo'
    how much does out function slow down. As our elements increases, how many more operations do we need to do.
2.  This is called algorithmic efficiency.

# Rules of Big O

This is how to calculate Big O in an interview. There are 4 rules.

## Rule 1: Worst Case:

- when calculating big o we always think about the worst case.
- When we talk about big old we're talking about worst case.
  i.e: If you have an array of names and your name is at the last part of the array that you want to select that is the worst case.

## Rule 2: Remove Constants:

That is a Constants:
Simple arithmetic calculations (like adding two numbers), assigning a value to a variable or accessing an element in an array (assuming you know its index)

Why Remove Constants:
Constants, by their very nature, don't scale. They remain the same no matter how big or small the input is. So, when we're looking at the overall growth of an algorithm, we can safely ignore them.

- Focus on Scalability: Big O notation helps you understand how an algorithm's performance changes as the input grows.
- Constants Don't Scale: Constant time operations are important, but they don't affect the overall scaling behavior.
- Simplify Your Analysis: Removing constants makes Big O expressions easier to work with and compare.

## Rule 3: Different terms for inputs:

Use different variables to represent the sizes of different inputs when expressing the complexity of an algorithm using Big O notation.

Why Rule #3 Matters:

- Accuracy: Using separate variables lets us accurately capture how each input influences the algorithm's behavior.
  It provides a clearer picture of what's happening.
- Comparison: If we have different algorithms that solve the same problem but take varying types of input,
  Rule #3 makes it easier to compare them fairly.
- O(n log n)

- Identify: When analyzing an algorithm, carefully identify all the different types of input it takes.
- Variables: Assign distinct variable names (e.g., m, n, p, q) to represent the sizes of each input type.
- Express: Include all these variables in your Big O notation to give a precise picture of the algorithm's runtime.

## Rule 3: Drop non dominants: Drop non-dominant terms.

- This means that if we get the following: O(n + n\*2), We will drop the first term. i.e: O(n\*2)
- Exercise print_num_then_pairs.py has a Big O notation of O(n\*2) or Quadratic time.

# Big O notation of O(n) or Linear time

1.  Exercise big_o_O(n) has a Big O notation of O(n) or Linear time.
2.  The amount of elements in your function usually are the amount of operations you run.
    i.e: If you are running a loop of 4 inputs and you would need to do for operations on that input. looping 4 time on 4 inputs. This is linear.
3.  Basically it takes linear time to find Nemo.
4.  This is the most common notation. = Fair
5.  Scalability means as things grow larger does its scale.

# Big O notation of O(1) or Constant time

1.  Exercise big_o_O1 has a Big O notation of O(1) or Constant time.
2.  If you have a function that only does one operation that is Constant time.
    selecting the first array of a array of names. No matter how many names are added to the array, you only run one operation to select the first name.

# Bing O Notation O(n\*2) or Quadratic time

Other Examples of Quadratic Time

Nested loops: Whenever you have one loop inside another, it's often a sign of quadratic time.
Certain types of sorting algorithms: Selection sort and insertion sort can also have quadratic time complexity.

1.  Every time the number of elements increase we increase the number of Operations quadratically.
    i.e: if we have 2 elements and
2.  Interview questions usually ask you to solve something that is O(n\*2) and seeing if you can get it to O(n) or O(1).

# Bing O Notation O(n!) or Factorial time - oh no!

It usually means that we are adding a nested loop For every input we have which is bad

1. If you see this fix it immediately.
