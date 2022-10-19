# Алгоритм быстрой сортировки 3
# Quick sort algorithm 3
# Really quick because of using memory for recursion only

def quicksort(list, first, last):
    if first >= last: return list

    i, j = first, last
    pivot = list[(first + last) // 2]

    while i <= j:
        while list[i] < pivot: i += 1
        while list[j] > pivot: j -= 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i, j = i + 1, j - 1

    quicksort(list, first, j)
    return quicksort(list, i, last)


# Test zone
my_list = [10, -2, 7, 33, 8, 12, -7, 7]
print(quicksort(my_list, 0, len(my_list) - 1))
