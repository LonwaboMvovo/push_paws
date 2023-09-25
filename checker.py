from typing import List, Tuple
import operations as ops


def get_ints_from_user () -> List[int]:
    return input("List of ints: ").split()


def get_instructions_from_user() -> List[int]:
    return input("Instructions: ").lower().split()


def execute_instructions(lst_a: List[int], lst_b: List[int], instructions: List[int]) -> Tuple[List[int], List[int]]:
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


def main():
    print("\nChecker Program\n")

    lst_a = [int(num) for num in get_ints_from_user()]
    lst_b = []

    instructions = get_instructions_from_user()

    lst_a, lst_b = execute_instructions(lst_a, lst_b, instructions)

    if list_sorted(lst_a) and not lst_b:
        print("OK")
    else:
        print("KO")
    

if __name__ == "__main__":
    main()
