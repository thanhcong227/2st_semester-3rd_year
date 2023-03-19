
# Viết chương trình dùng kĩ thuật chia để trị cho tìm kiếm nhị phân trên mảng được sắp xếp tăng dần
from random import randint

def searchBinary(list, x):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if x == list[mid]:
            return True
        else:
            if x < list[mid]:
                return searchBinary(list[:mid], x)
            else:
                return searchBinary(list[mid + 1:], x)


# Đưa ra đánh giá (có thể bằng bảng hoặc bằng biểu đồ) sự tăng trưởng của thời
# gian thực hiện chương trình theo kích thước dữ liệu vào.

import time
import numpy as np

def timeSearchBinary(list, x):
    start = time.time()
    searchBinary(list, x)
    end = time.time()
    return end - start

arr = []

for i in range(1, 1000000, 10):
    x = timeSearchBinary(range(i), 0)
    print("Time search binary with data size", i, "is", x)
    arr.append(x)

# plot the result with matplotlib
import matplotlib.pyplot as plt

plt.plot(arr)
plt.ylabel('Time')
plt.xlabel('Data size')
plt.show()


