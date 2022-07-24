# recursive implementation of binary search

arr1 = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
tar1 = 22


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            return binary_search(data, target, mid+1, high)
        else:
            return binary_search(data, target, low, mid-1)

print(binary_search(arr1, tar1, 0, len(arr1)-1))
