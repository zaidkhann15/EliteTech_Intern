# optimization.py
import pulp
import numpy as np

def solve_product_mix(machine_hours=100, material=90, profitA=40, profitB=30):
    # 1) Define LP problem (maximize)
    prob = pulp.LpProblem("Product_Mix", pulp.LpMaximize)

    # 2) Decision variables (non-negative)
    x = pulp.LpVariable('x_A', lowBound=0, cat='Continuous')  # units of Product A
    y = pulp.LpVariable('y_B', lowBound=0, cat='Continuous')  # units of Product B

    # 3) Objective function
    prob += profitA * x + profitB * y, "Total_Profit"

    # 4) Constraints
    prob += 2 * x + 1 * y <= machine_hours, "MachineHours"
    prob += 1 * x + 1.5 * y <= material, "Material"

    # 5) Solve
    prob.solve()

    # 6) Prepare results
    result = {
        'status': pulp.LpStatus[prob.status],
        'x_A': pulp.value(x),
        'y_B': pulp.value(y),
        'objective': pulp.value(prob.objective),
        'constraints': {name: constraint.value() for name, constraint in prob.constraints.items()}
    }
    return result

if __name__ == "__main__":
    res = solve_product_mix()
    print("Status:", res['status'])
    print("Produce x_A (Product A) =", res['x_A'])
    print("Produce y_B (Product B) =", res['y_B'])
    print("Maximum profit = $", res['objective'])
    print("Constraint slacks:")
    for k,v in res['constraints'].items():
        print(f"  {k}: slack = {v}")