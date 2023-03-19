# Median of two sorted arrays of different sizes.

def median_of_two_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        return median_of_two_sorted_arrays(arr2, arr1)
    k = (n1 + n2 + 1) // 2
    left = 0
    right = n1
    while left < right:
        m1 = left + (right - left) // 2
        m2 = k - m1
        if arr1[m1] < arr2[m2 - 1]:
            left = m1 + 1
        else:
            right = m1
    m1 = left
    m2 = k - m1
    c1 = max(arr1[m1 - 1] if m1 > 0 else float('-inf'),
             arr2[m2 - 1] if m2 > 0 else float('-inf'))
    if (n1 + n2) % 2 == 1:
        return c1
    c2 = min(arr1[m1] if m1 < n1 else float('inf'),
             arr2[m2] if m2 < n2 else float('inf'))
    return (c1 + c2) / 2

def main():
    arr1 = [1,3,5]
    arr2 = [2,4,8,11,20]
    n = median_of_two_sorted_arrays(arr1, arr2)
    print(n)

import time

def timeMedianOfTwoSortedArrays(arr1, arr2):
    start = time.time()
    median_of_two_sorted_arrays(arr1, arr2)
    end = time.time()
    return end - start

arr = []
for i in range(1, 1000000, 10):
    x = timeMedianOfTwoSortedArrays(range(i), range(i))
    print("Time median of two sorted arrays with data size", i, "is", x)
    arr.append(x)

# plot the result with matplotlib
import matplotlib.pyplot as plt

plt.plot(arr)
plt.ylabel('Time')
plt.xlabel('Data size')
plt.show()