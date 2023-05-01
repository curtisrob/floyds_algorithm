import timeit
import sys
from recursive_floyd import floyd_recursive
from imperative_floyd import floyd

NO_PATH = sys.maxsize

graph_one = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]

graph_two = [
    [0, 5, NO_PATH, NO_PATH, 2, NO_PATH, NO_PATH, NO_PATH],
    [5, 0, 8, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 8, 0, 6, NO_PATH, 1, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 6, 0, 3, NO_PATH, 2, NO_PATH],
    [2, NO_PATH, NO_PATH, 3, 0, NO_PATH, NO_PATH, 4],
    [NO_PATH, NO_PATH, 1, NO_PATH, NO_PATH, 0, 7, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 2, NO_PATH, 7, 0, 9],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 4, NO_PATH, 9, 0],
]


def test_floyd_recursive_one():
    """
    Test the recursive Floyd's algorithm on graph_one
    """
    floyd_recursive(graph_one)


def test_floyd_recursive_two():
    """
    Test the recursive Floyd's algorithm on graph_two
    """
    floyd_recursive(graph_two)


def test_floyd_imperative_one():
    """
    Test the imperative Floyd's algorithm on graph_one
    """
    floyd(graph_one)


def test_floyd_imperative_two():
    """
    Test the imperative Floyd's algorithm on graph_two
    """
    floyd(graph_two)


if __name__ == "__main__":
    num_runs = 10000
    print(f"Running performance tests {num_runs} times...")

    time_imperative = timeit.timeit(test_floyd_recursive_one, number=num_runs)
    print(
        f"Recursive version took {time_imperative:.6f} seconds to run {num_runs} times on graph 1"
    )

    time_imperative = timeit.timeit(test_floyd_recursive_two, number=num_runs)
    print(
        f"Recursive version took {time_imperative:.6f} seconds to run {num_runs} times on graph 2"
    )

    time_imperative = timeit.timeit(test_floyd_imperative_one, number=num_runs)
    print(
        f"Imperative version took {time_imperative:.6f} seconds to run {num_runs} times on graph 1"
    )

    time_imperative = timeit.timeit(test_floyd_imperative_two, number=num_runs)
    print(
        f"Imperative version took {time_imperative:.6f} seconds to run {num_runs} times on graph 2"
    )
