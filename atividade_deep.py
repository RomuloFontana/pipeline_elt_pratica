import csv
import statistics as st
import json as js
import sys
import matplotlib.pyplot as plt

#Abrindo e lendo os dados
dados = []

try:
    with open("vendas.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit()

#Processar os dados

calc_total_vendas = lambda quant,valor : quant * valor
total_das_vendas = {}

for indice in dados:
    produto = indice["produto"]
    total = calc_total_vendas(int(indice["quantidade"]), float(indice["valor"]))
    if produto in total_das_vendas:
        total_das_vendas[produto] += total
    else:
        total_das_vendas[produto] = total

#Total das vendas

soma_total_valor = 0
for valor in total_das_vendas.values():
    soma_total_valor += valor

#Produto mais vendido

prod_quant_vendas = {}
for index in dados:
    produto = index["produto"]
    quantidade = int(index["quantidade"])
    if produto in prod_quant_vendas:
        prod_quant_vendas[produto] += quantidade
    else:
        prod_quant_vendas[produto] = quantidade

top_quant = max(prod_quant_vendas.values())
prod_mais_vend = {}
for i,j in prod_quant_vendas.items():
    if j == top_quant:
        prod_mais_vend[i] = j 

#Adicionando as métricas estatísticas
#por dia/venda

dic_data_vendas = {}
for index in dados:
    produto = index["data"]
    quantidade = int(index["quantidade"])
    if produto in dic_data_vendas:
        dic_data_vendas[produto] += [quantidade]
    else:
        dic_data_vendas[produto] = [quantidade]

#Média
media_venda_dia = {}
for dia, quant in dic_data_vendas.items():
    media_quant = st.mean(quant)
    media_venda_dia[dia] = media_quant

#Mediana
mediana_venda_dia = {}
for dia, quant in dic_data_vendas.items():
    mediana_quant = st.median(quant)
    mediana_venda_dia[dia] = mediana_quant

#Desvio de Padrão
desv_padrao = {}
for dia, quant in dic_data_vendas.items():
    desv = st.stdev(quant)
    desv_padrao[dia] = desv

desv_arredond = {i : round(j,4) for i,j in desv_padrao.items()}

#Montando o gráfico de barras
mais_20k = list(filter(lambda x: x > 20000, total_das_vendas.values()))

total_20 = {}
for chave, valor in total_das_vendas.items():
    if valor in mais_20k:
        total_20[chave] = valor

plt.bar(total_20.keys(), total_20.values())



#Salvando para colocar no json
resultados = {
    "Total das vendas" : f"R$ {soma_total_valor:,.2f}",
    "Produto mais vendido" : prod_mais_vend,
    "Media das vendas por dia" : media_venda_dia,
    "Mediana das vendas por dia": mediana_venda_dia,
    "Desvio de padrao" : desv_arredond
}

with open("relatorio_final.json", 'w') as arquivo_json:
    js.dump(resultados,arquivo_json, indent=4)
    print("Relatório feito com sucesso")

