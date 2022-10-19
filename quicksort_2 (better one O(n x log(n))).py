# Алгоритм быстрой сортировки 2
# Quick sort algorithm 2.
# A good one with O-big = O(n * log(n))

def quicksort(list):
    if len(list) < 2: return list

    pivot = list[len(list) // 2]  # approximately in the middle of the list

    # initialize 3 new lists - for elements lower than the pivot, greater and equal
    lower = []
    greater = []
    equal = []

    for i in list:
        if i < pivot:
            lower.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)

    return quicksort(lower) + equal + quicksort(greater)


# Test zone
print(quicksort([10, -2, 7, 33, 8, 12, -7, 7]))
