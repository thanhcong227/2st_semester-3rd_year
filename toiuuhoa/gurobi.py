import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model()

# Define variables
x = model.addVar(vtype=GRB.CONTINUOUS, name="x")
y = model.addVar(vtype=GRB.CONTINUOUS, name="y")
z = model.addVar(vtype=GRB.CONTINUOUS, name="z")
t = model.addVar(vtype=GRB.CONTINUOUS, name="t")

# Set objective function
model.setObjective(5 / 3 * x - 8 / 3 * y + 2 / 3 * t + 10, GRB.MAXIMIZE)

# Add constraints
model.addConstr(-2/3 * x + 1 / 3 * y + z + 1/3*t == 2)
model.addConstr(5/3 * x + 5 / 3 * y -1/3 * t == 5)

# Solve the model
model.optimize()

# Print the optimal solution
print("Optimal solution:")
for v in model.getVars():
    print(v, "=", v.x)
print("Optimal objective value =", model.objVal)
