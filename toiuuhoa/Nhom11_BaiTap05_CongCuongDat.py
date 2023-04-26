"""
    Nhóm 11: Bài tập 05
    Thành viên:     Lê Thành Công - 20000530 - K65TT
                    Lã Mạnh Cường - 20000532 - K65TT
                    Nguyễn Tiến Đạt - 20000542 - K65TT

    Đề bài: Xây dựng mô hình tối ưu sử dụng Gurobi để tìm cách tô màu cho bài toán Color(8, 2) (xem
            định nghĩa của bài toán tổng quát Color(N, k) trong phiếu bài tập lần 4).
"""

import gurobipy as gp
from gurobipy import GRB

model = gp.Model()

# Create variables
x1 = model.addVar(vtype=GRB.BINARY, name='x1')
x2 = model.addVar(vtype=GRB.BINARY, name='x2')
x3 = model.addVar(vtype=GRB.BINARY, name='x3')
x4 = model.addVar(vtype=GRB.BINARY, name='x4')
x5 = model.addVar(vtype=GRB.BINARY, name='x5')
x6 = model.addVar(vtype=GRB.BINARY, name='x6')
x7 = model.addVar(vtype=GRB.BINARY, name='x7')
x8 = model.addVar(vtype=GRB.BINARY, name='x8')

# Set objective
model.setObjective(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8, GRB.MAXIMIZE)
# GRB.MINIMIZE also works

# Add constraints
model.addConstr(x1 + x2 + x3 <= 2)
model.addConstr(x1 + x3 + x4 <= 2)
model.addConstr(x1 + x4 + x5 <= 2)
model.addConstr(x1 + x5 + x6 <= 2)
model.addConstr(x1 + x6 + x7 <= 2)
model.addConstr(x1 + x7 + x8 <= 2)
model.addConstr(x2 + x3 + x5 <= 2)
model.addConstr(x2 + x4 + x6 <= 2)
model.addConstr(x2 + x5 + x7 <= 2)
model.addConstr(x2 + x6 + x8 <= 2)
model.addConstr(x3 + x4 + x7 <= 2)
model.addConstr(x3 + x5 + x8 <= 2)

model.addConstr(x1 + x2 + x3 >= 1)
model.addConstr(x1 + x3 + x4 >= 1)
model.addConstr(x1 + x4 + x5 >= 1)
model.addConstr(x1 + x5 + x6 >= 1)
model.addConstr(x1 + x6 + x7 >= 1)
model.addConstr(x1 + x7 + x8 >= 1)
model.addConstr(x2 + x3 + x5 >= 1)
model.addConstr(x2 + x4 + x6 >= 1)
model.addConstr(x2 + x5 + x7 >= 1)
model.addConstr(x2 + x6 + x8 >= 1)
model.addConstr(x3 + x4 + x7 >= 1)
model.addConstr(x3 + x5 + x8 >= 1)

# Optimize model
model.optimize()

# Print solution
if model.status == GRB.OPTIMAL:
    print('Optimal objective: %g' % model.objVal)
    for v in model.getVars():
        print('%s = %g' % (v.varName, v.x))
else:
    print('Status: %d' % model.status)

"""Terminal output:
Restricted license - for non-production use only - expires 2024-10-28
Gurobi Optimizer version 10.0.1 build v10.0.1rc0 (linux64)

CPU model: Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz, instruction set [SSE2|AVX|AVX2]
Thread count: 4 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 24 rows, 8 columns and 72 nonzeros
Model fingerprint: 0x9401dd02
Variable types: 0 continuous, 8 integer (8 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [1e+00, 1e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 2e+00]
Presolve time: 0.00s
Presolved: 24 rows, 8 columns, 72 nonzeros
Variable types: 0 continuous, 8 integer (8 binary)
Found heuristic solution: objective 4.0000000

Root relaxation: objective 5.333333e+00, 9 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 infeasible    0         4.00000    4.00000  0.00%     -    0s

Explored 1 nodes (9 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 1: 4 

Optimal solution found (tolerance 1.00e-04)
Best objective 4.000000000000e+00, best bound 4.000000000000e+00, gap 0.0000%
Optimal objective: 4
x1 = 0
x2 = 0
x3 = 1
x4 = 0
x5 = 1
x6 = 1
x7 = 1
x8 = 0
"""