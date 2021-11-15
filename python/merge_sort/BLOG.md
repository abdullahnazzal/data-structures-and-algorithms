# Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves.

## Trace

## Sample Array: [8,4,23,42,16,15]

### Pass 1

Mergesort:
arr = [8,4,23,42,16,15]
left = [8,4,23]
right = [42,16,15]

### Pass 2

Mergesort:
arr = [8,4,23]
left = [8]
right = [4,23]

### Pass 3

Mergesort:
arr = [8]
pass

### Pass 4

Mergesort:
arr = [4,23]
left = [8]
right = [23]

### Pass 5

Mergesort:
arr = [4]
pass

### Pass 6

Mergesort:
arr = [23]
pass

### Pass 7

Merge:
arr = [4,23], left = [4], right = [23]
arr = [4,23]

### Pass 8

Merge:
arr = [8,4,23], left = [8], right = [4,23]
arr = [4,8,23]

### Pass 9

Mergesort:
arr = [42,16,15]
left = [42]
right = [16,15]

### Pass 10

Mergesort:
arr = [42]
pass

### Pass 11

Mergesort:
arr = [16,15]
left = [16]
right = [15]

### Pass 12

Merge:
arr = [16,15], left = [16], right = [15]
arr = [15,16]

### Pass 13

Merge:
arr = [42,16,15], left = [42], right = [16,15]
arr = [15,16,42]

### Pass 14

Merge:
arr = [8,4,23,42,16,15], left = [4,8,23], right = [15,16,42]
arr = [4,8,15,16,23,42]
