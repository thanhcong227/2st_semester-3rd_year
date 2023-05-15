def T(n):

    if n == 1 or n == 0:
        return 2

    elif n < 0:
        return 0

    else:
        sum_T = 0
        for i in range(n):
            sum_T += 2 * T(i) * T(i - 1)
        return sum_T
