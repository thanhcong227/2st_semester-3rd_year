"""
 NHÓM 11: Bài tập 03
 HỌ VÀ TÊN: Lê Thành Công - 20000530
            Lã Mạnh Cường - 20000532
            Nguyễn Tiến Đạt - 20000542
 Lớp : A2K65 Toán tin
"""

print("Bài 1 --------------------------")

import gurobipy as gp
from matplotlib import cm

# Create a new model
model = gp.Model()

# Define variables
x = model.addVar(name="x")
y = model.addVar(name="y")
z = model.addVar(name="z")

# A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [3, 6, 2]])
# b = np.array([[3], [2], [5], [25]])
# c = np.array([[2], [2], [1]])

# Set objective function
model.setObjective(2 * x + 2 * y + z, gp.GRB.MAXIMIZE)

# Add constraints
model.addConstr(x <= 3)
model.addConstr(y <= 2)
model.addConstr(z <= 5)
model.addConstr(3 * x + 6 * y + 2 * z <= 25)

# Solve the model
model.optimize()

# Print the optimal solution
print("Optimal solution:")
for v in model.getVars():
    print(v, "=", v.x)
print("Optimal objective value =", model.objVal)

# Bài tập 2:
print("Bài 2 --------------------------")
'''
a) Viết một hàm xác định phương trình đường thẳng đi qua hai điểm phân biệt trong mặt phẳng
Oxy.
Đầu vào: hai tuple biểu diễn toạ độ hai điểm trên mặt phẳng.
Đầu ra: một tuple gồm ba hệ số a, b, c của phương trình đường thẳng ax + by = c.

b) Viết một hàm xác định phương trình mặt phẳng đi qua ba điểm phân biệt không thẳng hàng
trong không gian Oxyz.
Đầu vào: ba tuple biểu diễn toạ độ ba điểm không thẳng hàng trong không gian.
Đầu ra: một tuple gồm bốn hệ số a, b, c, d của phương trình mặt phẳng ax + by + cz = d.
'''


# a)
def line_equation(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    return a, b, c


# b)
def plane_equation(point1, point2, point3):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    a = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    b = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    d = a * x1 + b * y1 + c * z1
    return a, b, c, d

print('Nhập tọa độ 2 điểm trên mặt phẳng Oxy : ')
point1 = tuple(map(int, input().split()))
point2 = tuple(map(int, input().split()))
print('Phương trình đường thẳng đi qua 2 điểm trên là : ')
a, b, c = line_equation(point1, point2)
print(f'{a}x + {b}y = {c}')

print('Nhập tọa độ 3 điểm không thẳng hàng trong không gian Oxyz : ')
point1 = tuple(map(int, input().split()))
point2 = tuple(map(int, input().split()))
point3 = tuple(map(int, input().split()))
print('Phương trình mặt phẳng đi qua 3 điểm trên là : ')
a, b, c, d = plane_equation(point1, point2, point3)
print(f'{a}x + {b}y + {c}z = {d}')

