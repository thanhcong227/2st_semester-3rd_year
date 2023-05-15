"""
    Nhóm 11: Bài tập 07
    Thành viên:     Lê Thành Công - 20000530 - K65TT
                    Lã Mạnh Cường - 20000532 - K65TT
                    Nguyễn Tiến Đạt - 20000542 - K65TT
"""


'''
    Bài 2: Cho f(x, y) = 5x^2 + y^2. Hãy lập trình thuật toán gradient descent với độ dài bước cố định và với độ dài
    bước sử dụng thuật toán backtracking tìm cực tiểu của f.
'''

print("Bài 2: Cho f(x, y) = 5x^2 + y^2. Hãy lập trình thuật toán gradient descent với độ dài bước cố định và với độ dài "
      "bước sử dụng thuật toán backtracking tìm cực tiểu của f.")

# Gradient Descent với độ dài bước cố định:

def f(x, y):
    return 5 * x ** 2 + y ** 2

def gradient_descent_constant_step(f, initial_point, learning_rate, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [10 * point[0], 2 * point[1]]
        point = [point[0] - learning_rate * gradient[0], point[1] - learning_rate * gradient[1]]
    return point

# Sử dụng thuật toán Gradient Descent với độ dài bước cố định
initial_point = [0, 0]  # Điểm khởi tạo
learning_rate = 0.1  # Độ dài bước cố định
num_iterations = 100  # Số lần lặp
min_point = gradient_descent_constant_step(f, initial_point, learning_rate, num_iterations)
print("Sử dụng thuật toán Gradient Descent với độ dài bước cố định:")
print("Điểm cực tiểu:", min_point)
print("Giá trị nhỏ nhất:", f(min_point[0], min_point[1]))

# Gradient Descent với độ dài bước sử dụng thuật toán backtracking:
def gradient_descent_backtracking(f, initial_point, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [10 * point[0], 2 * point[1]]  # Tính gradient của hàm f(x, y)
        learning_rate = backtracking_line_search(f, point, gradient)  # Tìm độ dài bước sử dụng backtracking
        point[0] -= learning_rate * gradient[0]  # Cập nhật x
        point[1] -= learning_rate * gradient[1]  # Cập nhật y
    return point

def backtracking_line_search(f, point, gradient, alpha=0.5, beta=0.8):
    learning_rate = 1.0
    while f(point[0] - learning_rate * gradient[0], point[1] - learning_rate * gradient[1]) > f(point[0], point[1]) - alpha * learning_rate * sum([g * g for g in gradient]):
        learning_rate *= beta
    return learning_rate

# Sử dụng thuật toán Gradient Descent với độ dài bước backtracking
initial_point = [0, 0]  # Điểm khởi tạo
num_iterations = 100  # Số lần lặp
min_point = gradient_descent_backtracking(f, initial_point, num_iterations)
print("Sử dụng thuật toán Gradient Descent với độ dài bước backtracking:")
print("Điểm cực tiểu:", min_point)
print("Giá trị nhỏ nhất:", f(min_point[0], min_point[1]))

print("----------------------------------------------")

'''
    # Bài 3: Cho hàm số f(x1,x2) = 100(x2-x1)^2 + (1-x1)^2 và hai điểm A(1,2) and B(-1,0)
    # 1. Lập trình thuật toán gradient descent với backtracking line search tìm điểm cực tiểu của f với các thông số sau
'''

print("Bài 3: Cho hàm số f(x1,x2) = 100(x2-x1)^2 + (1-x1)^2 và hai điểm A(1,2) and B(-1,0)")
print("1. Lập trình thuật toán gradient descent với backtracking line search tìm điểm cực tiểu của f với các thông số sau")
print("* Giá trị bước ban đầu cho thuật toán backtracking line search alpha = 1.")

# Giá trị bước ban đầu cho thuật toán backtracking line search alpha = 1.

def f(x1, x2):
    return 100 * (x2 - x1) ** 2 + (1 - x1) ** 2

def gradient_descent_backtracking(f, initial_point, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [200 * point[0] - 200 * point[1] - 2, 200 * point[1] - 200 * point[0]]  # Tính gradient của hàm f(x, y)
        learning_rate = backtracking_line_search(f, point, gradient)  # Tìm độ dài bước sử dụng backtracking
        point[0] -= learning_rate * gradient[0]  # Cập nhật x
        point[1] -= learning_rate * gradient[1]  # Cập nhật y
    return point

def backtracking_line_search(f, point, gradient, alpha=0.5, beta=0.8):
    learning_rate = 1.0
    while f(point[0] - learning_rate * gradient[0], point[1] - learning_rate * gradient[1]) > f(point[0], point[1]) - alpha * learning_rate * sum([g * g for g in gradient]):
        learning_rate *= beta
    return learning_rate


print("* Điểm xuất phát cho thuật toán gradient descent lần lượt là x0 = A và x0 = B")

print("----------------------------------------------")
# Điểm xuất phát cho thuật toán gradient descent lần lượt là x0 = A và x0 = B

initial_point_A = [1, 2]  # Điểm khởi tạo A
initial_point_B = [-1, 0]  # Điểm khởi tạo B
num_iterations = 100  # Số lần lặp
min_point_A = gradient_descent_backtracking(f, initial_point_A, num_iterations)
min_point_B = gradient_descent_backtracking(f, initial_point_B, num_iterations)
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát A:", min_point_A)
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát A:", f(min_point_A[0], min_point_A[1]))
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát B:", min_point_B)
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát B:", f(min_point_B[0], min_point_B[1]))

print("----------------------------------------------")

print("* Thuât toán dừng khi số bước lặp vượt quá 1000 hoặc ∥∇f(x^k)∥ < 10^−4 với x^k là điểm tìm được ở bước lặp thứ k.")
# Thuật toán dừng khi số bước lặp vượt quá 1000 hoặc ∥∇f(x^k)∥ < 10^−4 với x^k là điểm tìm được ở bước lặp thứ k.

import numpy as np
def norm(gradient):
    return np.sqrt(sum([g * g for g in gradient]))


def gradient_descent_backtracking(f, initial_point, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [200 * point[0] - 200 * point[1] - 2, 200 * point[1] - 200 * point[0]]  # Tính gradient của hàm f(x, y)
        learning_rate = backtracking_line_search(f, point, gradient)  # Tìm độ dài bước sử dụng backtracking
        point[0] -= learning_rate * gradient[0]  # Cập nhật x
        point[1] -= learning_rate * gradient[1]  # Cập nhật y
        if norm(gradient) < 10 ** (-4):
            break
    return point

def backtracking_line_search(f, point, gradient, alpha=0.5, beta=0.8):
    learning_rate = 1.0
    while f(point[0] - learning_rate * gradient[0], point[1] - learning_rate * gradient[1]) > f(point[0], point[1]) - alpha * learning_rate * sum([g * g for g in gradient]):
        learning_rate *= beta
    return learning_rate

print("----------------------------------------------")

print("Hãy lập trình thuật toán Newton với backtracking tìm nghiệm cực tiểu của f dùng tiêu chuẩn dừng như trên.")
'''
    # 2. Hãy lập trình thuật toán Newton với backtracking tìm nghiệm cực tiểu của f dùng tiêu chuẩn dừng như trên.
'''

# Sử dụng thuật toán Newton với độ dài bước backtracking
def f(x1, x2):
    return 100 * (x2 - x1) ** 2 + (1 - x1) ** 2

def gradient_descent_backtracking(f, initial_point, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [200 * point[0] - 200 * point[1] - 2, 200 * point[1] - 200 * point[0]]  # Tính gradient của hàm f(x, y)
        learning_rate = backtracking_line_search(f, point, gradient)  # Tìm độ dài bước sử dụng backtracking
        point[0] -= learning_rate * gradient[0]  # Cập nhật x
        point[1] -= learning_rate * gradient[1]  # Cập nhật y
    return point

def backtracking_line_search(f, point, gradient, alpha=0.5, beta=0.8):
    learning_rate = 1.0
    while f(point[0] - learning_rate * gradient[0], point[1] - learning_rate * gradient[1]) > f(point[0], point[1]) - alpha * learning_rate * sum([g * g for g in gradient]):
        learning_rate *= beta
    return learning_rate

def hessian(x1, x2):
    return [[1200 * x1 ** 2 - 400 * x2 + 2, -400 * x1], [-400 * x1, 200]]

def newton_backtracking(f, initial_point, num_iterations):
    point = initial_point
    for _ in range(num_iterations):
        gradient = [200 * point[0] - 200 * point[1] - 2, 200 * point[1] - 200 * point[0]]  # Tính gradient của hàm f(x, y)
        hess = hessian(point[0], point[1])  # Tính ma trận hessian của hàm f(x, y)
        learning_rate = backtracking_line_search(f, point, gradient)  # Tìm độ dài bước sử dụng backtracking
        point[0] -= learning_rate * np.dot(np.linalg.inv(hess), gradient)[0]  # Cập nhật x
        point[1] -= learning_rate * np.dot(np.linalg.inv(hess), gradient)[1]  # Cập nhật y
    return point

print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát A:", newton_backtracking(f, initial_point_A, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát A:", f(newton_backtracking(f, initial_point_A, num_iterations)[0], newton_backtracking(f, initial_point_A, num_iterations)[1]))
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát B:", newton_backtracking(f, initial_point_B, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát B:", f(newton_backtracking(f, initial_point_B, num_iterations)[0], newton_backtracking(f, initial_point_B, num_iterations)[1]))

print("----------------------------------------------")

print("So sánh tốc độ và chất lượng nghiệm của các thuật toán đã lập trình ở trên.")

# 3. So sánh tốc độ và chất lượng nghiệm của các thuật toán đã lập trình ở trên.
import time
start_time = time.time()
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát A:", gradient_descent_backtracking(f, initial_point_A, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát A:", f(gradient_descent_backtracking(f, initial_point_A, num_iterations)[0], gradient_descent_backtracking(f, initial_point_A, num_iterations)[1]))
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát B:", gradient_descent_backtracking(f, initial_point_B, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát B:", f(gradient_descent_backtracking(f, initial_point_B, num_iterations)[0], gradient_descent_backtracking(f, initial_point_B, num_iterations)[1]))
print("Thời gian chạy thuật toán Gradient Descent với backtracking:", time.time() - start_time)

start_time = time.time()
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát A:", newton_backtracking(f, initial_point_A, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát A:", f(newton_backtracking(f, initial_point_A, num_iterations)[0], newton_backtracking(f, initial_point_A, num_iterations)[1]))
print("Điểm cực tiểu của f(x1, x2) với điểm xuất phát B:", newton_backtracking(f, initial_point_B, num_iterations))
print("Giá trị nhỏ nhất của f(x1, x2) với điểm xuất phát B:", f(newton_backtracking(f, initial_point_B, num_iterations)[0], newton_backtracking(f, initial_point_B, num_iterations)[1]))
print("Thời gian chạy thuật toán Newton với backtracking:", time.time() - start_time)


print("----------------------------------------------")
print("Bài tập 4. (Bài tập lập trình) Xây dựng một mô hình quy hoạch phi tuyến và sử dụng Gurobi giải quyết bài toán sau: Cho n điểm dữ liệu (x1, y1),(x2, y2), . . . ,(xn, yn). Tìm tham số a, b làm cực tiểu hóa đại lượng S = ∑ni=1(yi − axi − b)^2.")
'''
Bài tập 4. (Bài tập lập trình) Xây dựng một mô hình quy hoạch phi tuyến và sử dụng Gurobi giải quyết bài toán sau: Cho n điểm dữ liệu (x1, y1),(x2, y2), . . . ,(xn, yn). Tìm tham số a, b làm cực tiểu hóa đại lượng S = ∑ni=1(yi − axi − b)^2.
'''

from gurobipy import *
import numpy as np
import matplotlib.pyplot as plt

# 1. Xây dựng mô hình quy hoạch phi tuyến.
def nonlinear_regression(x, y):
    model = Model("Nonlinear Regression")
    a = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="a")
    b = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="b")
    S = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="S")
    model.setObjective(S, GRB.MINIMIZE)
    model.addConstr(S == sum([(y[i] - a * x[i] - b) ** 2 for i in range(len(x))]))
    model.optimize()
    return a.x, b.x

# 2. Tạo dữ liệu và giải bài toán.
x = np.random.rand(100)
y = 2 * x + 1 + np.random.rand(100)
a, b = nonlinear_regression(x, y)
print("a =", a)
print("b =", b)

# 3. Vẽ đồ thị.
plt.scatter(x, y)
plt.plot(x, a * x + b, color="red")
plt.show()



