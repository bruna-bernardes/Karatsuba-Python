# ✨ Projeto Algoritmo de Karatsuba (FPAA)

## 📖 O que é este projeto?
Este projeto implementa o **Algoritmo de Karatsuba** em Python para multiplicação eficiente de números inteiros grandes.  
O trabalho faz parte da disciplina **Fundamentos de Projeto e Análise de Algoritmos (FPAA)** e inclui a implementação em código, a explicação linha a linha e a análise de complexidade.  

---

## 🧮 O que é o Algoritmo de Karatsuba?
O algoritmo de Karatsuba foi criado por Anatolii Karatsuba em 1960 e é um método de multiplicação mais rápido que o tradicional.  
Ele usa a técnica de **divisão e conquista (divide and conquer)** para reduzir o número de multiplicações necessárias.

🔑 Principais pontos:
- Reduz a complexidade de **O(n²)** (método tradicional) para **O(n^1.585)**.  
- Divide os números em **parte alta** e **parte baixa**.  
- Usa apenas **3 multiplicações recursivas** em vez de 4.  

---

## ▶️ Como executar o projeto

### Pré-requisitos
- **Python 3.9+** instalado.
- Este projeto **não** tem dependências externas.

### 1) Clonar o repositório
git clone https://github.com/bruna-bernardes/algoritmo-karatsuba-fpaa.git

cd algoritmo-karatsuba-fpaa

### 2) (Opcional) Criar e ativar um ambiente virtual
- Windows

python -m venv .venv
.venv\Scripts\activate

- Linus/macOS

python3 -m venv .venv
source .venv/bin/activate

### 3) Executar o programa
- Windows

python main.py

- Linux/macOS

python3 main.py

### 4) Exemplo de uso
Digite o primeiro número inteiro: 1234

Digite o segundo número inteiro: 5678

Resultado da multiplicação (Karatsuba):
1234 * 5678 = 7006652

### Observações:
Informe inteiros (positivos ou negativos).

Para números muito grandes, o Python lida nativamente sem configurações extras.

---

## ⚙️ Complexidade Ciclomática
A **complexidade ciclomática** é uma métrica que quantifica quantos caminhos independentes existem no código.  

Para a função `karatsuba`, temos:
- **Nós (N):** 6  
- **Arestas (E):** 7  
- **Componentes (P):** 1

Grafo do Karatsuba

![Grafo do Karatsuba](docs/Grafo_Karatsuba.svg)


📌 Fórmula:  
\[
M = E - N + 2P = 7 - 6 + 2(1) = 3
\]

⚠️ Quanto maior o valor da complexidade ciclomática, mais difícil é entender e manter o código.  
👉 Nesse caso, a complexidade é **3**, considerada baixa.

---

## 📊 Complexidade Assintótica
O tempo de execução do algoritmo segue a recorrência:  
\[
T(n) = 3T\left(\frac{n}{2}\right) + O(n)
\]

🔎 Resultado:
- **Melhor caso:** \( O(1) \), quando os números têm 1 dígito.  
- **Caso médio e pior caso:** \( O(n^{\log_2 3}) \approx O(n^{1.585}) \).  
- **Espaço:** \( O(\log n) \), devido à recursão.

---

## 📝 Explicação do Código

### 1. Separação em dígitos
num_digitos pega a quantidade de dígitos do maior entre x_abs e y_abs.
metade define o ponto de corte para dividir cada número.

### 2. Divisão em parte alta e baixa
divmod(n, 10**metade) retorna (parte_alta, parte_baixa).

### 3. Três multiplicações recursivas
produto_baixas: multiplica as partes baixas.
produto_altas: multiplica as partes altas.
produto_somas: multiplica as somas das partes — usado para obter o termo cruzado.

### 4. Combinação dos resultados
Recompõe o produto total:
produto_altas * 10^(2*metade): desloca a parte alta para a esquerda.
(produto_somas - produto_altas - produto_baixas) * 10^metade: termo intermediário (cruzado).
produto_baixas: parte baixa.

---

## 📦 Dependências

### Python 3.11.9 (sem bibliotecas externas).

---

## 📚 Documentação e Links úteis

Artigo original do McCabe: “A Complexity Measure” (1976) – DO: https://doi.org/10.1109/TSE.1976.233837

Karatsuba: implementação e análise (CP-Algorithms): https://cp-algorithms.com/algebra/karatsuba.html

Master Theorem: https://cp-algorithms.com/algebra/master-theorem.html

---

## ✅ Conclusão
O algoritmo de Karatsuba é um exemplo claro de **divide and conquer**: ao substituir quatro multiplicações grandes por **três** menores, reduz a complexidade temporal de \(O(n^2)\) para \(O(n^{\log_2 3}) \approx O(n^{1{,}585})\), com uso de espaço \(O(\log n)\) devido à profundidade da recursão. 
Na prática, ele é **vantajoso para operações grandes**, para tamanhos pequenos, o custo de dividir e combinar pode superar o ganho, por isso foi adotado um **caso base** com multiplicação direta.


Implementações de produção tendem a ser **híbridas**: usam a multiplicação “escolar” para valores pequenos, **Karatsuba** para tamanhos intermediários e para números gigantes.
Assim, este projeto evidencia **quando** e **por que** Karatsuba é preferível, além de apresentar sua análise assintótica e o **grafo de fluxo de controle** correspondente.
