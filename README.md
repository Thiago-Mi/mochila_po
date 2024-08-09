<a name="readme-topo"></a>

<h1 align='center'>
   Problema das Múltiplas Mochilas Binárias
</h1>

<div align='center'>

[![IDE][vscode-badge]][vscode-url]

[![Python][python-badge]][python-url]

<h3> Pesquisa Operacional </h3>

</div>



## 🔍 Introdução

<div align="justify">

Este trabalho foi proposto na disciplina de Pesquisa Operacional e tem como objetivo aplicar a teoria apresentada em sala na implementação de modelos de programação linear utilizando o solver Gurobi.
</div>



## 🎯 Objetivos

<div align="justify">

A principal finalidade deste trabalho é resolver o Problema das Múltiplas Mochilas Binárias (ou 0-1) utilizando o solver Gurobi. O problema consiste em selecionar itens de maneira que a soma dos benefícios seja maximizada, sem exceder a capacidade das mochilas disponíveis. O programa desenvolvido deve ser capaz de ler os dados de entrada a partir de um arquivo de texto e, ao final do processo de otimização, exibir a solução ótima, ou seja, quais itens serão levados em cada uma das mochilas.
Além de: 
  - Controle de entradas e saídas de arquivos;
  - Organização de código e boas práticas de programação.

</div>


### Arquivos

<div align="justify">

Para a solução proposta, os seguintes diretórios/arquivos foram utilizados:

  - [`input.txt`][input-ref]: arquivo de entrada contendo os dados do problema (número de itens, número de mochilas, capacidades das mochilas, pesos e benefícios dos itens);
  - [`problema_da_mochila.py`][main-ref]: arquivo principal em Python que contém a implementação da solução utilizando o solver Gurobi;


### Bibliotecas

A seguir estão as bibliotecas incluídas no programa e que são essenciais para o funcionamento dele.

`gurobipy`: biblioteca que integra o solver Gurobi ao código Python;

`sys`: biblioteca utilizada para manipular argumentos de linha de comando, incluindo o caminho para o arquivo de entrada;



### Pré-requisitos

Inicialmente, algumas considerações importantes sobre como se deve preparar o ambiente para compilar e executar o programa:

> [!NOTE]
> Instale o Gurobi e a biblioteca Python gurobipy, conforme as instruções disponíveis na documentação oficial;
Garanta que o Python 3 e o pip estejam instalados no seu ambiente.


### Instalando e executando

Com o ambiente preparado, os seguintes passos são para a instalação, compilação e execução do programa localmente:

<!-- Ensinar a clonar a pasta do repositório -->
1. Clone o repositório no diretório a seguir:
  ```console
https://github.com/Thiago-Mi/mochila_po.git
  ```
2. Navegue até o diretório do projeto:
  ```console
  cd mochila_po
  ```
3. Execute o programa passando o arquivo de entrada como argumento:
  ```console
  python3 problema_da_mochila.py input.txt

  ```

<p align="right">(<a href="#readme-topo">voltar ao topo</a>)</p>

[vscode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[vscode-url]: https://code.visualstudio.com/docs/?dv=linux64_deb
[python-badge]: https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
