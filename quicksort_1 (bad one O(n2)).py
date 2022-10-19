# Grokking algorithms, page 92
# Алгоритм быстрой сортировки / Quick sort algorithm
# Not a good one because of "O big" = O(n^2). Reason - pivot is the first value of the list
# (see explanation in the book)

def quick_sort(list):
    if len(list) < 2: return list

    pivot = list[0]
    less = [i for i in list[1:] if i <= pivot]
    greater = [i for i in list[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


# Test zone
print(quick_sort([10, -2, 7, 33, 8, 12]))
