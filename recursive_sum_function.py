# Grokking algorithms, page 85, exercise 4.1
# Рекурсивная функция поиска суммы всех элементов списка
def find_sum(mylist):
    if not mylist:
        return 0
    return mylist[0] + find_sum(mylist[1:])

# Test zone
print(find_sum([1, 2, 30, 4, 5, 6]))
