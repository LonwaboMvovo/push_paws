from typing import List, Tuple


def swap_first_two_elements(lst: List[int]) -> List[int]:
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]

    return lst


def swap_both_first_two_elements(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    return swap_first_two_elements(lst_a), swap_first_two_elements(lst_b)



def push_to_another_list(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    if lst_b:
        lst_a = [lst_b.pop(0)] + lst_a

    return lst_a, lst_b


def rotate_list(lst: List[int]) -> List[int]:
    return lst[1:] + lst[:1]


def rotate_both_lists(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    return rotate_list(lst_a), rotate_list(lst_b)


def reverse_rotate_list(lst: List[int]) -> List[int]:
    return lst[-1:] + lst[:-1]
