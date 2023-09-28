from typing import List, Tuple


def swap_first_two_elements(lst: List[int]) -> List[int]:
    """
    Swap the first two elements of a list of integers.

    Args:
        lst (List[int]): The list of integers to be modified.

    Returns:
        List[int]: The modified list with the first two elements swapped.
        If the list has fewer than two elements, it remains unchanged.
    """
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]

    return lst


def swap_both_first_two_elements(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    """
    Swap the first two elements of two lists of integers.

    Args:
        lst_a (List[int]): The first list of integers to be modified.
        lst_b (List[int]): The second list of integers to be modified.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing the modified lists with the first two
        elements swapped. If either list has fewer than two elements, it remains unchanged.
    """
    return swap_first_two_elements(lst_a), swap_first_two_elements(lst_b)


def push_to_another_list(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    """
    Push the first element of one list onto the front of another list.

    Args:
        lst_a (List[int]): The target list to which the element will be pushed.
        lst_b (List[int]): The source list from which the first element will be removed
                        and pushed onto lst_a.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing the modified lists after pushing
        the first element from lst_b onto the front of lst_a. If lst_b is empty, the
        lists remain unchanged.
    """
    if lst_b:
        lst_a = [lst_b.pop(0)] + lst_a

    return lst_a, lst_b


def rotate_list(lst: List[int]) -> List[int]:
    """
    Shift up the elements of a list by one position.

    Args:
        lst (List[int]): The list of integers to be rotated.

    Returns:
        List[int]: The modified list with its elements shifted up by one position.
    """
    return lst[1:] + lst[:1]


def rotate_both_lists(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    """
    Shift up the elements of two lists by one position each.

    Args:
        lst_a (List[int]): The first list of integers to be rotated.
        lst_b (List[int]): The second list of integers to be rotated.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing the modified lists with their elements
        shifted up by one position each.
    """
    return rotate_list(lst_a), rotate_list(lst_b)


def reverse_rotate_list(lst: List[int]) -> List[int]:
    """
    Shift down the elements of a list by one position.

    Args:
        lst (List[int]): The list of integers to be reverse rotated.

    Returns:
        List[int]: The modified list with its elements shifted down by one position.
    """
    return lst[-1:] + lst[:-1]


def reverse_rotate_both_lists(lst_a: List[int], lst_b: List[int]) -> Tuple[List[int], List[int]]:
    """
    Shift down the elements of two lists by one position each.

    Args:
        lst_a (List[int]): The first list of integers to be reverse rotated.
        lst_b (List[int]): The second list of integers to be reverse rotated.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing the modified lists with their elements
        shifted down by one position each.
    """
    return reverse_rotate_list(lst_a), reverse_rotate_list(lst_b)
