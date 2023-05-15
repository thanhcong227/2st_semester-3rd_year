def MVCS(a):
    max = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum > max:
                max = sum

    return max

print(MVCS([1, -3, 4, -2, -1, 6]))