# Check for Majority Element in a sorted array. by divide and conquer

def checkMajorityElementArrSorted(arr, x):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if x == arr[mid]:
            return True
        else:
            if x < arr[mid]:
                return checkMajorityElementArrSorted(arr[:mid], x)
            else:
                return checkMajorityElementArrSorted(arr[mid + 1:], x)


def main():
    arr = [3, 3, 3, 7, 8, 10]
    print(checkMajorityElementArrSorted(arr, 3))


import time

def timeCheckMajorityElementArrSorted(arr, x):
    start = time.time()
    checkMajorityElementArrSorted(arr, x)
    end = time.time()
    return end - start

arr = []

for i in range(1, 1000000, 10):
    x = timeCheckMajorityElementArrSorted(range(i), 0)
    print("Time check majority element with data size", i, "is", x)
    arr.append(x)

# plot the result with matplotlib
import matplotlib.pyplot as plt

plt.plot(arr)
plt.ylabel('Time')
plt.xlabel('Data size')
plt.show()

