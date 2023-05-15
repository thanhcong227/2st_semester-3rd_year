def MVCS(a):
    max = a[0]
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum < 0:
            sum = 0
            continue
        if sum > max:
            max = sum

    return max

print(MVCS([1, -3, 4, -2, -1, 6]))