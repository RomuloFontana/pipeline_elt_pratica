Explicação do Pseudocódigo
<!-- Importar bibliotecas: -->

Você pode usar a biblioteca csv para ler e escrever arquivos CSV.
Se quiser, pode usar pandas para facilitar a manipulação dos dados.

<!-- Ler o arquivo CSV: -->

Use open() para abrir o arquivo e csv.DictReader() para ler os dados em formato de dicionário.

Armazene os dados em uma lista de dicionários, onde cada dicionário representa uma venda.

<!-- Processar os dados: -->

Para calcular o total de vendas, some todos os valores da coluna de vendas.

Para encontrar o produto mais vendido, conte quantas vezes cada produto aparece na lista.

Para calcular a média de vendas, agrupe as vendas por data (dia, semana ou mês) e calcule a média.

<!-- Gerar relatório: -->

Crie um arquivo TXT ou CSV usando open() e csv.writer().

Escreva os resultados no arquivo.

Finalização:

Fechar os arquivos e exibir uma mensagem indicando que o processo foi concluído.