def T(n):
    if n == 1 or n == 0:
        return 2
    for i in range(2,n+1):
        sum = 0
        for j in range(1,i):
            sum += 2 * T(j) * T(j-1)

    return sum

