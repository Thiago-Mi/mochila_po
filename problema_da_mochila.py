import sys
import gurobipy as gp
from gurobipy import GRB

def ler_input(file_path):
    """
    Lê os dados do problema de múltiplas mochilas a partir de um arquivo de entrada.

    Args:
        file_path (str): caminho para o arquivo de entrada formatado

    Returns:
        int, int, list[float], list[tuple]: Numero de itens (n) e mochilas (m), capacidade de cada mochila (c) e lista de itens [(beneficio,peso)]
    """
    with open(file_path, 'r') as f:
        itens = []
        n, m = map(int, f.readline().strip().split())
        c = list(map(float, f.readline().strip().split()))
        
        for _ in range(n):
            beneficio, peso = map(float, f.readline().strip().split())
            itens.append((beneficio, peso))
            
    return n,m,c, itens

def mochila_inteira(n,m,c,itens):
    """
    Aplicação no Gurobi do problema lido e print de sua solução. 

    Args:
        n (int): Numero de itens
        m (int): Numero de mochilas
        c (list[float]): Capacidade das m mochilas
        itens (list[tuple]): beneficio e peso de cada item
        
    Print: 
        Valor da Função Objetivo.
        Itens da Mochila m: [itens].
    """
    model = gp.Model("problema_mochilas")
    
    # Criação das variáveis de decisão x[i, j].
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")
    # Aplicação da função objetivo multiplicando o beneficio dos itens pela sua presença ou não na mochila(0,1).
    model.setObjective(gp.quicksum(itens[i][0] * x[i,j] for i in range(n) for j in range(m)), GRB.MAXIMIZE)
    # Restrição da capacidade multiplicando o peso do item pela presença do mesmo definindo como menor ou igual.
    model.addConstrs((gp.quicksum(itens[i][1] * x[i,j] for i in range(n)) <= c[j] for j in range(m)), name="capacity")
    # Restrição para a singularidade de itens na mochila.
    model.addConstrs((gp.quicksum(x[i,j] for j in range(m)) <= 1 for i in range(n)), name="item_assignment")
    
    model.optimize()
    
    # Exibe a solução ótima
    if model.status == GRB.OPTIMAL:
        print("\n---------------------------------------------------")
        print("Solução Ótima")
        print("---------------------------------------------------")
        print(f"Valor da Função Objetivo: {model.objVal}")
        for i in range(m):
            mochila = [j for j in range(n) if x[j,i].x >= 1]
            print(f"Itens da Mochila {i+1}: {mochila}")

    


if __name__ == "__main__":
    input_file = sys.argv[1]
    n, m, c, items = ler_input(input_file)
    mochila_inteira(n, m, c, items)