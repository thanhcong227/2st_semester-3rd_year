# Dãy nhị phân: Liệt kê các dãy nhị phân có độ dài n bằng cách sử dụng backtracking.

def binary(n):
    arr = [0] * n

    def backtrack(i):
        if i == n:
            print(arr)
        else:
            for j in range(2):
                arr[i] = j
                backtrack(i + 1)
    backtrack(0)


binary(3)

