import unittest
import push_swap_operations


class TestPushSwapOperations(unittest.TestCase):
    def test_swap_first_two_elements_empty_list(self):
        empty_list = []
        result = push_swap_operations.swap_first_two_elements(empty_list)
        self.assertEqual([], result, "swap_first_two_elements - should do nothing if the list has no elements")


    def test_swap_first_two_elements_one_element_list(self):
        one_element_list = [1]
        result = push_swap_operations.swap_first_two_elements(one_element_list)
        self.assertEqual([1], result, "swap_first_two_elements - should do nothing if the list only has one elements")


    def test_swap_first_two_elements_valid_list_list(self):
        valid_list = [2, 1, 3, 4, 5]
        result = push_swap_operations.swap_first_two_elements(valid_list)
        self.assertTrue((1 == result[0]) and (2 == result[1]), "swap_first_two_elements - should swap the first 2 elements at the top of the list")
        self.assertEqual([3, 4, 5], result[2:], "swap_first_two_elements - should do nothing to the rest of the elements in the list")


    def test_swap_both_first_two_elements_empty_list(self):
        empty_list_a = []
        empty_list_b = []
        result_a, result_b = push_swap_operations.swap_both_first_two_elements(empty_list_a, empty_list_b)
        self.assertEqual([], result_a, "swap_both_first_two_elements - should do nothing if list_a has no elements")
        self.assertEqual([], result_b, "swap_both_first_two_elements - should do nothing if list_b has no elements")


    def test_swap_both_first_two_elements_one_element_list(self):
        one_element_list_a = [1]
        one_element_list_b = [2]
        result_a, result_b = push_swap_operations.swap_both_first_two_elements(one_element_list_a, one_element_list_b)
        self.assertEqual([1], result_a, "swap_both_first_two_elements - should do nothing if list_a only has one elements")
        self.assertEqual([2], result_b, "swap_both_first_two_elements - should do nothing if list_b only has one elements")


    def test_swap_both_first_two_elements_valid_list(self):
        list_a = [2, 1, 3, 4, 5]
        list_b = [7, 6, 8, 9, 10]
        result_a, result_b = push_swap_operations.swap_both_first_two_elements(list_a, list_b)
        self.assertTrue((1 == result_a[0]) and (2 == result_a[1]), "swap_both_first_two_elements - should swap the first 2 elements at the top of list_a")
        self.assertEqual([3, 4, 5], result_a[2:], "swap_both_first_two_elements - should do nothing to the rest of the elements in list_a")
        self.assertTrue((6 == result_b[0]) and (7 == result_b[1]), "swap_both_first_two_elements - should swap the first 2 elements at the top of list_b")
        self.assertEqual([8, 9, 10], result_b[2:], "swap_both_first_two_elements - should do nothing to the rest of the elements in list_b")


if __name__ == "__main__":
    unittest.main()
