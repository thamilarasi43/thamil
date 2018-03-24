def countOccurrences(arr, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res
arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
n = len(arr)
x = 2
print (countOccurrences(arr, n, x))
