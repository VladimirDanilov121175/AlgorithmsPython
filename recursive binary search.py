# Grokking algorithms, p. 85, exercise 4.4
# Рекурсивная функция бинарного поиска

def binary(list, value):
    if len(list) == 1:
        if list[0] == value:
            return value
        else:
            return None

    mid = (len(list) - 1) // 2

    while len(list) > 0:
        if list[mid] == value: return value
        if list[mid] > value:
            return binary(list[:mid - 1], value)
        else:
            return binary(list[mid + 1:], value)


# Test zone
print(binary([1, 2, 3, 4, 5, 10, 21, 56], 10))  # -> 10
print(binary([1, 2, 3, 4, 5, 10, 21, 56], 7))  # -> None
