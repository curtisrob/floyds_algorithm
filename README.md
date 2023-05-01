# Recursive Floyd's Algorithm

The aim of this project is to rewrite floyd's algortihm to use recursion as opposed to the imperative solution that uses iterative loops.

Both solutions can be found in the parent directory <br>

Imperative Version: imperative_floyd.py <br>
Recursive Version: recursive_floyd.py <br>

## Requirements

There are two requirements to run the programme, which can be found in the requirements.txt file. <br>
Run the following command in your terminal to install all the necessary packages: pip install -r requirements.txt <br>

## Unit Tests

To ensure that the functions operate as expected, unit tests can be found in the /unit_tests folder <br>

## Performance Test

To measure the performance of the two solutions, a module to comapre the imperative approach vs the recursive approach can be found in the performance_testing/ folder

## Solution

Running recursive_floyd.py should produce the following output: <br>

[[0, 7, 9223372036854775807, 8], [9223372036854775807, 0, 5, 9223372036854775807], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]] <br>

[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]] <br>

These two matrices represent the input graph followed by a matrix containing the shortest path between each node. <br>
The input graph can be changed in the code file.


