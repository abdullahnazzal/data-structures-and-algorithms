def merge(left, right, arr):
    i=j=k=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        # print("merge_sort(left) dd")
        merge_sort(right)
        merge(left, right, arr)
        return arr


arr = [8,4,23,42,16,15]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

merge_sort(arr)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),

# This code is contributed by Mohit Kumra
