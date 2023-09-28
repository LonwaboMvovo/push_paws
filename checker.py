from typing import List, Tuple, Union
import operations as ops


def get_user_ints () -> Union[List[int], str]:
    """
    Prompts the user to input a list of integers, validates the input,
    and returns a list of integers if the input is valid and contains no duplicates.

    Returns:
        List[int] | str: A list of integers if input is valid, or an error message."
    """
    try:
        response = [int(num) for num in input("List of ints: ").strip().split()]

        if len(response) != len(set(response)):
            return "ERROR: duplicate input"

        return response
    except ValueError as e:
        return "ERROR: invalid input"


def get_user_instructions() -> Union[List[str], str]:
    """
    Prompts the user to input a sequence of instructions.
    Validates the input by checking if each instruction is one of the valid instructions.
    
    Returns:
        List[str] | str: A list of user instructions if all are valid, or an error message if any input instruction is invalid.
    """
    valid_instructions = {"sa", "sb", "ss", "pa", "pb", "ra", "rb", "rr", "rra", "rrb", "rrr"}

    user_instructions = input("Instructions: ").strip().lower().split()
    for user_inst in user_instructions:
        if user_inst not in valid_instructions:
            return "ERROR: invalid instructions"

    return user_instructions


def execute_instructions(lst_a: List[int], lst_b: List[int], instructions: List[str]) -> Tuple[List[int], List[int]]:
    """
    Execute a sequence of instructions on two lists, lst_a and lst_b, and return the updated lists.

    Args:
        lst_a (List[int]): The first list to operate on.
        lst_b (List[int]): The second list to operate on.
        instructions (List[str]): A list of instructions specifying the operations to be performed.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists, representing the updated lst_a and lst_b.
    """
    for instruction in instructions:
        if instruction == "sa":
            lst_a = ops.swap_first_two_elements(lst_a)
        elif instruction == "sb":
            lst_b = ops.swap_first_two_elements(lst_b)
        elif instruction == "ss":
            lst_a, lst_b = ops.swap_both_first_two_elements(lst_a, lst_b)
        elif instruction == "pa":
            lst_a, lst_b = ops.push_to_another_list(lst_a, lst_b)
        elif instruction == "pb":
            lst_b, lst_a = ops.push_to_another_list(lst_b, lst_a)
        elif instruction == "ra":
            lst_a = ops.rotate_list(lst_a)
        elif instruction == "rb":
            lst_b = ops.rotate_list(lst_b)
        elif instruction == "rr":
            lst_a, lst_b = ops.rotate_both_lists(lst_a, lst_b)
        elif instruction == "rra":
            lst_a = ops.reverse_rotate_list(lst_a)
        elif instruction == "rrb":
            lst_b = ops.reverse_rotate_list(lst_b)
        else:
            lst_a, lst_b = ops.reverse_rotate_both_lists(lst_a, lst_b)

    return lst_a, lst_b


def list_sorted(input_list: List[int]) -> bool:
    """
    Check if a given list of integers is sorted in non-decreasing order.

    Args:
        input_list (List[int]): The list of integers to check.

    Returns:
        bool: True if the input list is sorted in increasing order, False otherwise.
    """
    return input_list == sorted(input_list)


def survey_says(lst_a, lst_b):
    """
    Checks values of two lists and considers what the response should be based on checker program specifications.

    Args:
        lst_a: The first list to consider.
        lst_b: The second list to consider.

    Returns:
        str: The response, which can be one of the following:
            - "OK" if lst_a is sorted in increasing order and lst_b is empty.
            - "KO" if lst_a is not sorted in non-decreasing order or lst_b is not empty.
    """
    response = "OK"

    if not list_sorted(lst_a) or lst_b:
        response = "KO"

    return response


def main():
    print("\nChecker Program\n")

    lst_a = get_user_ints()
    if isinstance(lst_a, str):
        print(lst_a)
        return

    lst_b = []

    instructions = get_user_instructions()
    if isinstance(instructions, str):
        print(instructions)
        return

    lst_a, lst_b = execute_instructions(lst_a, lst_b, instructions)

    print(survey_says(lst_a, lst_b))
    

if __name__ == "__main__":
    main()
