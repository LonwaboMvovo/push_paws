def swap_first_two_elements(lst):
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]

    return lst


def swap_both_first_two_elements(lst_a, lst_b):
    return swap_first_two_elements(lst_a), swap_first_two_elements(lst_b)


def push_to_a(lst_a, lst_b):
    return lst_a, lst_b
