import time

def findMin(data):
    if len(data) == 1:
        return data[0]
    else:
        mid = len(data) // 2
        return min(findMin(data[:mid]), findMin(data[mid:]))

def findMax(data):
    if len(data) == 1:
        return data[0]
    else:
        mid = len(data) // 2
        return max(findMax(data[:mid]), findMax(data[mid:]))

def timeFindMin(data):
    start = time.time()
    findMin(data)
    end = time.time()
    return end - start

def timeFindMax(data):
    start = time.time()
    findMax(data)
    end = time.time()
    return end - start


arr = []
for i in range(1, 10000, 10):
    x = timeFindMax(range(i))
    print("Time find max with data size", i, "is", x)
    arr.append(x)

# plot the result with matplotlib
import matplotlib.pyplot as plt

plt.plot(arr)
plt.ylabel('Time')
plt.xlabel('Data size')
plt.show()