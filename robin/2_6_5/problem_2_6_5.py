'''
    quick sort
    time complexity: O(NlogN)
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(input_array):

    if len(input_array) <= 1:
        return input_array

    pivot = input_array[0]
    tail = input_array[1:]

    left_side = [ x for x in tail if x <= pivot ]
    right_side = [ x for x in tail if x > pivot ]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
