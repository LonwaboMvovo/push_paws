import unittest
from unittest.mock import patch
import operations
import checker


class TestOperations(unittest.TestCase):
    def test_swap_first_two_elements_empty_list(self):
        empty_list = []
        result = operations.swap_first_two_elements(empty_list.copy())
        self.assertEqual(empty_list, result, "swap_first_two_elements - should do nothing if the list has no elements")


    def test_swap_first_two_elements_one_element_list(self):
        one_element_list = [1]
        result = operations.swap_first_two_elements(one_element_list.copy())
        self.assertEqual(one_element_list, result, "swap_first_two_elements - should do nothing if the list only has one elements")


    def test_swap_first_two_elements_valid_list_list(self):
        valid_list = [2, 1, 3, 4, 5]
        result = operations.swap_first_two_elements(valid_list.copy())
        self.assertTrue((valid_list[1] == result[0]) and (valid_list[0] == result[1]), "swap_first_two_elements - should swap the first 2 elements at the top of the list")
        self.assertEqual(valid_list[2:], result[2:], "swap_first_two_elements - should do nothing to the rest of the elements in the list")


    def test_swap_both_first_two_elements_empty_list(self):
        empty_list_a = []
        empty_list_b = []
        result_a, result_b = operations.swap_both_first_two_elements(empty_list_a.copy(), empty_list_b.copy())
        self.assertEqual(empty_list_a, result_a, "swap_both_first_two_elements - should do nothing if list_a has no elements")
        self.assertEqual(empty_list_b, result_b, "swap_both_first_two_elements - should do nothing if list_b has no elements")


    def test_swap_both_first_two_elements_one_element_list(self):
        one_element_list_a = [1]
        one_element_list_b = [2]
        result_a, result_b = operations.swap_both_first_two_elements(one_element_list_a.copy(), one_element_list_b.copy())
        self.assertEqual(one_element_list_a, result_a, "swap_both_first_two_elements - should do nothing if list_a only has one elements")
        self.assertEqual(one_element_list_b, result_b, "swap_both_first_two_elements - should do nothing if list_b only has one elements")


    def test_swap_both_first_two_elements_valid_list(self):
        list_a = [2, 1, 3, 4, 5]
        list_b = [7, 6, 8, 9, 10]
        result_a, result_b = operations.swap_both_first_two_elements(list_a.copy(), list_b.copy())
        self.assertTrue((list_a[1] == result_a[0]) and (list_a[0] == result_a[1]), "swap_both_first_two_elements - should swap the first 2 elements at the top of list_a")
        self.assertEqual(list_a[2:], result_a[2:], "swap_both_first_two_elements - should do nothing to the rest of the elements in list_a")
        self.assertTrue((list_b[1] == result_b[0]) and (list_b[0] == result_b[1]), "swap_both_first_two_elements - should swap the first 2 elements at the top of list_b")
        self.assertEqual(list_b[2:], result_b[2:], "swap_both_first_two_elements - should do nothing to the rest of the elements in list_b")


    def test_push_to_a_empty_b(self):
        list_a = [1, 2, 3, 4, 5]
        list_b = []
        result_a, result_b = operations.push_to_another_list(list_a.copy(), list_b.copy())
        self.assertEqual(list_a, result_a, "push_to_another_list - should do nothing if list_b has no elements")
        self.assertEqual(list_b, result_b, "push_to_another_list - should do nothing if list_b has no elements")


    def test_push_to_a_valid_b(self):
        list_a = [3, 4, 5]
        list_b = [2, 1]
        result_a, result_b = operations.push_to_another_list(list_a.copy(), list_b.copy())
        self.assertEqual([2, 3, 4, 5], result_a, "push_to_another_list - the first element of list_a should now be the former first element of list_b")
        self.assertEqual([1], result_b, "push_to_another_list - the first element of list_b should now be the former second element of list_b")


    def test_rotate_list(self):
        list_a = [1, 2, 3, 4, 5]
        result = operations.rotate_list(list_a)
        self.assertEqual([2, 3, 4, 5, 1], result, "rotate_list - elements not shifted correctly. The first should become the last")


    def test_rotate_both_lists(self):
        list_a = [1, 2, 3, 4, 5]
        list_b = [6, 7, 8, 9, 10]
        result_a, result_b = operations.rotate_both_lists(list_a, list_b)
        self.assertEqual([2, 3, 4, 5, 1], result_a, "rotate_both_lists - elements not shifted correctly in list_a. The first should become the last")
        self.assertEqual([7, 8, 9, 10, 6], result_b, "rotate_both_lists - elements not shifted correctly in list_b. The first should become the last")


    def test_reverse_rotate_list(self):
        list_a = [2, 3, 4, 5, 1]
        result = operations.reverse_rotate_list(list_a)
        self.assertEqual([1, 2, 3, 4, 5], result, "reverse_rotate_list - elements not shifted correctly. The last should become the first")


    def test_reverse_rotate_both_lists(self):
        list_a = [2, 3, 4, 5, 1]
        list_b = [7, 8, 9, 10, 6]
        result_a, result_b = operations.reverse_rotate_both_lists(list_a, list_b)
        self.assertEqual([1, 2, 3, 4, 5], result_a, "reverse_rotate_both_lists - elements not shifted correctly in list_a. The last should become the first")
        self.assertEqual([6, 7, 8, 9, 10], result_b, "reverse_rotate_both_lists - elements not shifted correctly in list_b. The last should become the first")


class TestChecker(unittest.TestCase):
    @patch("builtins.input", side_effect=["3 2 1 0"])
    def test_get_user_ints_valid_input(self, mock_input):
        result = checker.get_user_ints()
        self.assertEqual([3, 2, 1, 0], result, "get_user_ints - should return an integer list of the user arguments")


    @patch("builtins.input", side_effect=["3 two 1 LMAO"])
    def test_get_user_ints_invalid_input(self, mock_input):
        result = checker.get_user_ints()
        self.assertEqual("ERROR: invalid input", result, "get_user_ints - should return an error message for invalid user input")


    @patch("builtins.input", side_effect=["9 0 2 1 0"])
    def test_get_user_ints_duplicate_input(self, mock_input):
        result = checker.get_user_ints()
        self.assertEqual("ERROR: duplicate input", result, "get_user_ints - should return an error message for user input with duplicates")  


    @patch("builtins.input", side_effect=["sa sb ss pa pb ra rb rr rra rrb rrr"])
    def test_get_user_instructions_valid_input(self, mock_input):
        result = checker.get_user_instructions()
        self.assertEqual(["sa", "sb", "ss", "pa", "pb", "ra", "rb", "rr", "rra", "rrb", "rrr"], result, "get_user_instructions - should return a string list of the user instructions")


    @patch("builtins.input", side_effect=["swap_a sb ss PhantomAssassin ra rrr"])
    def test_get_user_instructions_invalid_input(self, mock_input):
        result = checker.get_user_instructions()
        self.assertEqual("ERROR: invalid instructions", result, "get_user_instructions - should return an error message for invalid user instructions")


    def test_execute_instructions_sa(self):
        lst_a = [1, 2, 3, 4, 5]
        lst_b = [6, 7, 8, 9, 10]
        instructions = ["rra", "pb", "ss", "ra", "sb", "sa", "rr", "rrb", "rrr", "pa", "rb"]

        result_a, result_b = checker.execute_instructions(lst_a, lst_b, instructions)
        self.assertEqual([10, 3, 1, 4, 2], result_a, "execute_instructions - instructions executed incorrectly on list_a")
        self.assertEqual([6, 7, 8, 9, 5], result_b, "execute_instructions - instructions executed incorrectly on list_b")


    def test_list_sorted(self):
        sorted_list = [-2, -1, 0, 1, 2]
        result = checker.list_sorted(sorted_list)
        self.assertTrue(result)


    def test_list_not_sorted(self):
        unsorted_list = [-1, 2, 1, -2, 0]
        result = checker.list_sorted(unsorted_list)
        self.assertFalse(result)


    def test_survey_says_ok(self):
        lst_a = [1, 2, 3, 4, 5]
        lst_b = []
        result = checker.survey_says(lst_a, lst_b)
        self.assertEqual("OK", result, "survery_says - should return 'OK' for sorted lst_a and empty lst_b")

    
    def test_survey_says_ko_unsorted_a(self):
        lst_a = [-1, 2, 1, -2, 0]
        lst_b = []
        result = checker.survey_says(lst_a, lst_b)
        self.assertEqual("KO", result, "survery_says - should return 'KO' for unsorted lst_a and empty lst_b")


    def test_survey_says_ko_not_empty_b(self):
        lst_a = [1, 2, 3, 4, 5]
        lst_b = [69, 420]
        result = checker.survey_says(lst_a, lst_b)
        self.assertEqual("KO", result, "survery_says - should return 'KO' for sorted lst_a and not empty lst_b")


if __name__ == "__main__":
    unittest.main()
