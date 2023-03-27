from random import randint


def QSort(array, start, stop):
    if start >= stop:
        return
    pivot = get_pivot(array, start, stop)
    QSort(array, start, pivot-1)
    QSort(array, pivot, stop)


def get_pivot(array, start, stop):
    pivot = array[stop]
    curr_pos = start
    for i in range(start, stop+1):
        if array[i] <= pivot:
            array[i], array[curr_pos] = array[curr_pos], array[i]
            curr_pos += 1
    if curr_pos > stop:
        curr_pos -= 1
    return curr_pos


arr = [randint(1, 10000) for _ in range(50)]
QSort(arr, 0, len(arr)-1)
print(arr)

