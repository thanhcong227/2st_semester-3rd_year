arr = []
arr.append(2)
arr.append(2)

def T(n):
    if n == 1 or n == 0:
        return 2

    elif n < 0:
        return 0

    else:
        for i in range(2, n+1):
            k = 0
            arr
            for j in range(1, i):
                k += 2 * T(j) * T(j-1)
            arr.append(k)

        return arr[n]

print(T(3))



