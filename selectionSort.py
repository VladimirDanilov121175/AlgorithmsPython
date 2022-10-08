"""
Сортировка выбором // Selection sort
from the book "Grokking algorithms"
"""


def find_smallest_number_in_list(my_list):
    smallest_number_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < my_list[smallest_number_index]:
            smallest_number_index = i
    return smallest_number_index


def selection_sort(my_list):
    new_list = []

    for i in range(len(my_list)):
        smallest = find_smallest_number_in_list(my_list)
        new_list.append(my_list.pop(smallest))
    return new_list


# Test zone
initial_list = [10, 33, 28, 5, 129, 3, 13, 6, 98]
print(initial_list)
print(selection_sort(initial_list))
