#7-1
def bubble_sort(A):
    """function for sorting arrays by bubble_sort method"""

    last_el = len(A)-1
    for i in range(0, last_el):
        for x in range(0, last_el - i):
            if A[x] < A[x+1]:
                A[x+1], A[x] = A[x], A[x+1]
    return A


my_list = [23, 12, 9, 16, 8, 7]
print(bubble_sort(my_list))