import unittest
import push_swap_operations


class TestPushSwapOperations(unittest.TestCase):
    def test_swap_a(self):
        empty_list = []
        one_element_list = [1]
        valid_list = [2, 1, 3, 4]

        result = push_swap_operations.swap_a(empty_list)
        self.assertEqual([], result, "swap_a - should do nothing if the list has no elements")

        result = push_swap_operations.swap_a(one_element_list)
        self.assertEqual([1], result, "swap_a - should do nothing if the list only has one elements")

        result = push_swap_operations.swap_a(valid_list)
        self.assertTrue((1 == result[0]) and (2 == result[1]), "swap_a - should swap the first 2 elements at the top of the list")
        self.assertEqual([3, 4], result[2:], "swap_a - should do nothing to the rest of the elements in the list")

        

if __name__ == "__main__":
    unittest.main()
