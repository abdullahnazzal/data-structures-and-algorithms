# Quick Sort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

## Trace

## Sample Array: ```[8,4,23,42,16,15]```

### Pass 1

quick_sort:

arr = ```[8,4,23,42,16,15]```

left = 0

right = 5

arr_f=```[8, 4, 15, 42, 16, 23]```

### Pass 2

quick_sort:

arr = ```[8, 4, 15, 42, 16, 23]```

left = 0

right = 1

arr_f=```[4, 8, 15, 42, 16, 23]```

### Pass 3

quick_sort:

arr = ```[4, 8, 15, 42, 16, 23]```

left = 3

right = 5

arr_f=```[4, 8, 15, 16, 23, 42]```

