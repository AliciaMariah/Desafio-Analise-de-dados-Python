# Desafio de Análise de Dados

## Descrição
Este desafio consiste na análise de um conjunto de dados financeiros fictícios, representando transações bancárias de clientes. O objetivo é responder a diversas perguntas relacionadas ao comportamento financeiro dos clientes, como saldo médio, última transação, balanço mensal e proporção entre tipos de transações.

## Estrutura dos Dados
O conjunto de dados é composto por duas tabelas:

### 1. Tabela de Clientes (`TbCliente`)
Contém informações sobre os clientes:

| CD_CLIENTE | NM_CLIENTE |
|------------|------------|
| 1          | João       |
| 2          | Maria      |
| 3          | José       |
| 4          | Adilson    |
| 5          | Cleber     |

### 2. Tabela de Transações (`TbTransacoes`)
Registra as transações bancárias realizadas pelos clientes:

| CD_CLIENTE | DT_TRANSACAO | CD_TRANSACAO | VR_TRANSACAO |
|------------|--------------|--------------|--------------|
| 1          | 2021-08-28   | 000          | 020.00       |
| 1          | 2021-09-09   | 110          | 078.90       |
| 1          | 2021-09-17   | 220          | 058.00       |
| 1          | 2021-11-15   | 110          | 178.90       |
| 1          | 2021-12-24   | 220          | 110.37       |
| 5          | 2021-10-28   | 110          | 220.00       |
| 5          | 2021-11-07   | 110          | 380.00       |
| 5          | 2021-12-05   | 220          | 398.86       |
| 5          | 2021-12-14   | 220          | 033.90       |
| 5          | 2021-12-21   | 220          | 016.90       |
| 3          | 2021-10-05   | 110          | 720.90       |
| 3          | 2021-11-05   | 110          | 720.90       |
| 3          | 2021-12-05   | 110          | 720.90       |
| 4          | 2021-10-09   | 000          | 050.00       |

Os tipos de transação são:
- **000**: CashBack
- **110**: CashIn
- **220**: CashOut

## Perguntas de Análise
As seguintes perguntas devem ser respondidas com base nas tabelas fornecidas:

1. Qual cliente teve o maior saldo médio no mês 11?
2. Qual é o saldo de cada cliente?
3. Qual é o saldo médio de clientes que receberam CashBack?
4. Qual o ticket médio das quatro últimas movimentações dos usuários?
5. Qual a proporção entre Cash In/Out mensal?
6. Qual a última transação de cada tipo para cada usuário?
7. Qual a última transação de cada tipo para cada usuário por mês?
8. Qual a quantidade de usuários que movimentaram a conta?
9. Qual o balanço do final de 2021?
10. Quantos usuários que receberam CashBack continuaram interagindo com este banco?
11. Qual a primeira e a última movimentação dos usuários com saldo maior que R$100?
12. Qual o balanço das últimas quatro movimentações de cada usuário?
13. Qual o ticket médio das últimas quatro movimentações de cada usuário?

## Tecnologia Utilizada
O desafio será resolvido utilizando ![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
, aproveitando bibliotecas como:
- `datetime` para gerenciamento de datas
- `collections` para operações com dicionários

## Conclusão
Este projeto simula um cenário real de análise de dados bancários e demonstra a importância do uso de programação para extrair insights financeiros de um conjunto de dados estruturados.
