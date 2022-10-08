# Binary Search Algorithm from the bool "Grokking algorithms"

def binary_search(sorted_list, number_to_guess):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess_try = sorted_list[middle]

        if guess_try == number_to_guess:
            return middle
        if guess_try > number_to_guess:
            high = middle - 1
        else:
            low = middle + 1
    return None


# Test zone
my_list = [1, 2, 3, 10, 28, 46, 56, 89, 100]
print(my_list)
print(binary_search(my_list, 56))
