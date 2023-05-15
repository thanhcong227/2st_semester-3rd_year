def MVCS(a):
    max = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum = 0
            for k in range(i, j+1):
                sum += a[k]
            if sum > max:
                max = sum

    return max

print(MVCS([1, -3, 4, -2, -1, 6]))