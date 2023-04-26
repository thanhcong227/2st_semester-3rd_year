import math


def func(x, y):
    func = math.sin(y)  # Example of ordinary differential equation
    return func


def midpoint():
    ##Initial Conditions
    x = 0  # Independent variable
    y = 1
    ##Integration Limit
    xi = 0
    xf = 0.3
    h = 0.1  # stepsize
    original_ans = [5, 4.37, 2.76]
    print("Iteration", 0)
    print("x:", x)
    print("estimated y:", y)
    print("original y:", original_ans[0])
    print("-------")

    i = 1
    n = (xf - xi) / h  # number of iterations
    while i <= n:  # This loop will run until the number of iterations are completed
        k1 = func(x, y)  # K1
        k2 = func(x + (h / 2), y + (k1 * h / 2))  # K2
        y = y + (k2 * h)  # Midpoint formula to update y
        x = x + h

        print("Iteration", i)
        print("x:", x)
        print("estimated y:", y)
        # print("original y:", original_ans[i])
        print("--------------------")
        i = i + 1


def main():
    midpoint()

main()