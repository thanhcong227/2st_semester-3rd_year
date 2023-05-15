def MVCS(a):
    max = a[0]
    sum = 0
    for i in range(len(a)):
        if sum + a[i] > a[i]:
            sum += a[i]
        else:
            sum = a[i]
        if sum > max:
            max = sum

    return max

print(MVCS([1, -3, 4, -2, -1, 6]))