def is_sorted(input_list):
    return input_list == sorted(input_list)

if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4]
    unsorted_list = [1, 3, 2, 4]

    print(is_sorted(sorted_list))
    print(is_sorted(unsorted_list))
