# Grokking algorithms, p. 85, exercise 4.2
# Рекурсивная функция подсчета элементов в списке

def count_elements(my_list):
    if not my_list:
        return 0
    return 1 + count_elements(my_list[1:])


# test zone
print(count_elements([1, 2, 3, 4, 5, 6]))  # -> 6
