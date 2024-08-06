import sys
import gurobipy as gp
from gurobipy import GRB


def read_input(file_path):
    # Lê os dados do problema
    with open(file_path, 'r') as f:
        # Lê o número de itens (n) e de mochilas (m)
        n, m = map(int, f.readline().strip().split())
        
        # Lê as capacidades das mochilas
        capacities = list(map(float, f.readline().strip().split()))
        
        # Lê os benefícios e pesos dos itens e guarda na lista items
        items = []
        for _ in range(n):
            benefit, weight = map(float, f.readline().strip().split())
            items.append((benefit, weight))
            
    return n,m,capacities, items

def mochila_inteira(n,m,capacities,items):
    # Criação do modelo
    model = gp.Model("problema_mochilas")
    
    # Criação das variáveis de decisão x[i, j]
    x = model.addVars(n, m, vtype=GRB.BINARY, name="x")
    
    # Função objetivo: maximizar a soma dos benefícios que é o indice 0 na lista de itens 
    model.setObjective(gp.quicksum(items[i][0] * x[i,j] for i in range(n) for j in range(m)), GRB.MAXIMIZE)
    
    # Restrição 1: A soma dos pesos dos itens em cada mochila deve ser menor ou igual à capacidade
    model.addConstrs((gp.quicksum(items[i][1] * x[i,j] for i in range(n)) <= capacities[j] for j in range(m)), name="capacity")
    
    # Restrição 2: Cada item só pode ser colocado em uma mochila
    model.addConstrs((gp.quicksum(x[i,j] for j in range(m)) <= 1 for i in range(n)), name="item_assignment")
    
    # Otimiza o modelo
    model.optimize()
    
    # Exibe a solução ótima
    if model.status == GRB.OPTIMAL:
        print("---------------------------------------------------")
        print("Solução Ótima")
        print("---------------------------------------------------")
        print(f"Valor da Função Objetivo: {model.objVal}")
        for j in range(m):
            mochila = [i for i in range(n) if x[i,j].x > 0.5]
            print(f"Itens da Mochila {j}: {mochila}")
    else:
        print("Nenhuma solução ótima encontrada.")
    


if __name__ == "__main__":
    # Verifica se o caminho do arquivo foi fornecido como argumento de linha de comando
    if len(sys.argv) != 2:
        print("Uso: python problema_da_mochila.py <caminho_para_o_arquivo_input>")
        sys.exit(1)
    input_file = sys.argv[1]

    # Leia o arquivo de entrada
    n, m, capacities, items = read_input(input_file)

    # Resolva o problema
    mochila_inteira(n, m, capacities, items)