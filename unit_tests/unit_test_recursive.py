import unittest
import sys
from recursive_floyd import floyd_recursive


NO_PATH = sys.maxsize


class TestFloydImperative(unittest.TestCase):
    def test_empty_test_graph(self):
        """
        Test that Floyd's algorithm works correctly on an empty test_graph.

        """
        test_graph = []
        shortest_path = floyd_recursive(test_graph)
        self.assertEqual(shortest_path, None)

    def test_single_node_test_graph(self):
        """
        Test that Floyd's algorithm works correctly on a test_graph with a single node.

        """
        test_graph = [[0]]
        shortest_path = floyd_recursive(test_graph)
        self.assertEqual(shortest_path, [[0]])

    def test_disconnected_test_graph(self):
        """
        Test that Floyd's algorithm works correctly on a disconnected test_graph.

        """
        test_graph = [
            [0, NO_PATH, NO_PATH],
            [NO_PATH, 0, NO_PATH],
            [NO_PATH, NO_PATH, 0],
        ]
        shortest_path = floyd_recursive(test_graph)
        self.assertEqual(
            shortest_path,
            [[0, NO_PATH, NO_PATH], [NO_PATH, 0, NO_PATH], [NO_PATH, NO_PATH, 0]],
        )

    def test_shortest_paths_on_simple_test_graph(self):
        """
        Test that Floyd's algorithm correctly computes the shortest paths on a simple test_graph.

        The expected behavior is that the output contains the correct shortest path distances
        """
        test_graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0],
        ]
        shortest_path = floyd_recursive(test_graph)
        self.assertEqual(
            shortest_path,
            [
                [0, 7, 12, 8],
                [NO_PATH, 0, 5, 7],
                [NO_PATH, NO_PATH, 0, 2],
                [NO_PATH, NO_PATH, NO_PATH, 0],
            ],
        )

    def test_negative_weight_cycle(self):
        """
        Test that Floyd's algorithm correctly handles a test_graph with a negative weight cycle.

        The expected behavior is that the output contains the correct shortest path distances,
        even with a negative weight cycle.
        """
        test_graph = [[0, 1, NO_PATH], [NO_PATH, 0, -1], [1, NO_PATH, 0]]
        shortest_path = floyd_recursive(test_graph)
        self.assertEqual(shortest_path, [[0, 1, 0], [0, 0, -1], [1, 2, 0]])


if __name__ == "__main__":
    unittest.main()
