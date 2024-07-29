import gurobipy as gp
from gurobipy import GRB


def read_input():
    # Lê os dados do problema
    with open('ks_toy.txt', 'r') as f:
        n = int(f.readline())
        m = int(f.readline())
        b = float(f.readline())
        w = [None for i in range(n)]
        p = [None for i in range(n)]
        for i in range(n):
            line = f.readline().split(' ')
            w[i] = float(line[0])
            p[i] = float(line[1])
    return n,m,b,w,p

def mochila_inteira(n,m,b,w,p):
    model = gp.Model()
    model.setParam(GRB.Param.LogToConsole,0)
    
    x = [model.addVar(lb=0, ub=GRB.INFINITY,vtype=GRB.INTEGER) for _ in range(n)]
    obj = gp.LinExpr()
    for i in range(n):
        obj += w[i] + x[i]
    model.setObjective(obj,sense=GRB.MAXIMAZE)
    
    #adicionar a criação de n mochilas
    # Define a restrição de capacidade da mochila
    expr1 = [(gp.LinExpr()) for _ in range(m)]
    for j in range(m):
        for i in range(n):
            expr1[m] += p[i] * x[i] 
    for _ in range(m):
        model.addConstr(expr1[m] <= b)
        
    for _ in range(n):
        model.addConstr(x[i] <=3)
    

# Cria um novo modelo
model = gp.Model()
model.setParam(GRB.Param.LogToConsole, 0)
# Cria as variáveis do problema
x1 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)
x2 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)
x3 = model.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)
# Define a função objetivo
model.setObjective(2*x1 + 5*x2 + x3, sense=GRB.MAXIMIZE)
# Define as restrições
model.addConstr(x1 + x2 <= 6)
model.addConstr(x2 - x3 >= 4)
model.addConstr(4*x1 + 2*x2 + x3 <= 15)
# Resolve o problema!
model.optimize()
# Dados da solução encontrada
print(f'Valor da função objetivo: {model.objVal}')
print(f'Valor das variáveis: x1={x1.X}, x2={x2.X}, x3={x3.X}')