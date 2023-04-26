import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model()

# Create variables
x = m.addVar(name="x", lb=-GRB.INFINITY, ub=GRB.INFINITY)
y = m.addVar(name="y", lb=-GRB.INFINITY, ub=GRB.INFINITY)

d = m.addVar(name="d", lb=0, ub=GRB.INFINITY)

m.setObjective((x-3)*(x-3)+(y-4)*(y-4), sense=GRB.MINIMIZE)
m.addConstr(x*x/3 + y*y == 4)
m.Params.NonConvex = 2
m.optimize()
print(x.x)
print(y.x)
print(m.objVal)