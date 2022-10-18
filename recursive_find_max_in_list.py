# Grokking algorithms, p. 85, exercise 4.3
# Рекурсивная функция нахождения максимального числа в списке

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    return list[0] if list[0] > max(list[1:]) else max(list[1:])


# Test zone
print(max([10, 7, 34, 5, -5, 13, 98, 11]))  # -> 98
