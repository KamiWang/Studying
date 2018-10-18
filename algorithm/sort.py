#!/usr/bin/env python

# 快速排序
def qsort(arr):
    def get_pivot(left, right):
        # 把基准放在数组第一位
        nonlocal arr
        mid = (left + right) // 2
        if arr[left] > arr[mid]:
            arr[left], arr[mid] = arr[mid], arr[left]
        if arr[mid] > arr[right]:
            arr[mid], arr[right] = arr[right], arr[mid]
        if arr[left] < arr[mid]:
            arr[left], arr[mid] = arr[mid], arr[left]

    def partition(left, right):
        nonlocal arr
        if left >= right:
            return
        i, j = left, right
        if j - i > 3:
            get_pivot(i, j)
        pivot = arr[i]
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot
        partition(left, i-1)
        partition(i+1, right)

    partition(0, len(arr)-1)


# 冒泡排序
def bubble_sort(arr):
    length = len(arr)
    if arr is None or 0 == length:
        return
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    c = [5, 4, 3, 2, 1]

    qsort(c)
    print(c)
