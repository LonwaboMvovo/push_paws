from typing import List, Tuple, Union
import operations as ops


def get_user_ints () -> Union[List[int], str]:
    user_input = input("List of ints: ")

    try:
        response = [int(num) for num in user_input.strip().split()]

        if len(response) != len(set(response)):
            return "duplicate input: " + user_input

        return response
    except ValueError as e:
        return "invalid input: " + user_input


def get_user_instructions() -> List[str]:
    return input("Instructions: ").lower().split()


def execute_instructions(lst_a: List[int], lst_b: List[int], instructions: List[str]) -> Tuple[List[int], List[int]]:
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
    return input_list == sorted(input_list)


def survey_says(lst_a, lst_b):
    response = "OK"

    if not list_sorted(lst_a) or lst_b:
        response = "KO"

    return response


def main():
    print("\nChecker Program\n")

    lst_a = get_user_ints()
    lst_b = []

    instructions = get_user_instructions()

    lst_a, lst_b = execute_instructions(lst_a, lst_b, instructions)

    print(survey_says(lst_a, lst_b))
    

if __name__ == "__main__":
    main()

# TODO - error handling for 'get_user_ints' & 'get_user_instructions'
# TODO - docstrings