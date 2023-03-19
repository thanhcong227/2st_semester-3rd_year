import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Tìm phần tử nhỏ nhất trong đoạn chưa sắp xếp
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên trong đoạn chưa sắp xếp
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def test_selection_sort(n):
    arr = [random.randint(1, n) for _ in range(n)]
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    return end_time - start_time


# Đo thời gian thực hiện sắp xếp mảng từ bé đến lớn với các kích thước khác nhau
sizes = [1000, 2000, 3000, 4000, 5000]
times = []
for size in sizes:
    time_taken = test_selection_sort(size)
    times.append(time_taken)
    print(f"Sorting an array of size {size} takes {time_taken} s")

# Vẽ biểu đồ thời gian thực hiện sắp xếp theo kích thước mảng
import matplotlib.pyplot as plt
plt.plot(sizes, times)
plt.xlabel('Array size')
plt.ylabel('Time (s)')
plt.title('Time taken to sort an array')
plt.show()
