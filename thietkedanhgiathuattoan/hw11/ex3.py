def T(n):
    if n == 1 or n == 0:
        return 2
    if n == 2:
        return 2 * T(1) * T(0)
    else:
        sum = 0
    for i in range(3, n + 1):
        sum += T(i - 1) + 2 * T(i-1) * T(i - 2)
    return sum

