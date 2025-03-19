import datetime
from collections import defaultdict
from datetime import datetime
#   AS TABELAS DE CLIENTES E TRANSACOES

TbCliente = [
    {"CD_CLIENTE": 1, "NM_CLIENTE": "João"},
    {"CD_CLIENTE": 2, "NM_CLIENTE": "Maria"},
    {"CD_CLIENTE": 3, "NM_CLIENTE": "José"},
    {"CD_CLIENTE": 4, "NM_CLIENTE": "Adilson"},
    {"CD_CLIENTE": 5, "NM_CLIENTE": "Cleber"},
]
TbTransacoes = [
    {"CD_CLIENTE": 1, "DT_TRANSACAO": "2021-8-28", "CD_TRANSACAO": 000, "VR_TRANSACAO": 20.00},
    {"CD_CLIENTE": 1, "DT_TRANSACAO": "2021-9-9", "CD_TRANSACAO": 110, "VR_TRANSACAO": 78.90},
    {"CD_CLIENTE": 1, "DT_TRANSACAO": "2021-9-17", "CD_TRANSACAO": 220, "VR_TRANSACAO": 58.00},
    {"CD_CLIENTE": 1, "DT_TRANSACAO": "2021-11-15", "CD_TRANSACAO": 110, "VR_TRANSACAO": 178.90},
    {"CD_CLIENTE": 1, "DT_TRANSACAO": "2021-12-24", "CD_TRANSACAO": 220, "VR_TRANSACAO": 110.37},
    {"CD_CLIENTE": 5, "DT_TRANSACAO": "2021-10-28", "CD_TRANSACAO": 110, "VR_TRANSACAO": 220.00},
    {"CD_CLIENTE": 5, "DT_TRANSACAO": "2021-11-7", "CD_TRANSACAO": 110, "VR_TRANSACAO": 380.00},
    {"CD_CLIENTE": 5, "DT_TRANSACAO": "2021-12-5", "CD_TRANSACAO": 220, "VR_TRANSACAO": 398.86},
    {"CD_CLIENTE": 5, "DT_TRANSACAO": "2021-12-14", "CD_TRANSACAO": 220, "VR_TRANSACAO": 33.90},
    {"CD_CLIENTE": 5, "DT_TRANSACAO": "2021-12-21", "CD_TRANSACAO": 220, "VR_TRANSACAO": 16.90},
    {"CD_CLIENTE": 3, "DT_TRANSACAO": "2021-10-5", "CD_TRANSACAO": 110, "VR_TRANSACAO": 720.90},
    {"CD_CLIENTE": 3, "DT_TRANSACAO": "2021-11-5", "CD_TRANSACAO": 110, "VR_TRANSACAO": 720.90},
    {"CD_CLIENTE": 3, "DT_TRANSACAO": "2021-12-5", "CD_TRANSACAO": 110, "VR_TRANSACAO": 720.90},
    {"CD_CLIENTE": 4, "DT_TRANSACAO": "2021-10-9", "CD_TRANSACAO": 000, "VR_TRANSACAO": 50.00},
    ]

# anotando os tipos de transacoes para me localizar quando preciso
transacao_tipo = {
    000: "CashBack",
    110: "CashIn",
    220: "CashOut"
}

print("1- Qual cliente teve o maior saldo médio no mês 11?")
# aqui estou começando a função para responder a primeira pergunta
def calcular_saldo_medio(mes, ano):
    saldo_medio_por_cliente = {}
    dias_no_mes = 30  # aqui estou considerando ser 30 dias o mes

    for cliente in TbCliente:
        cd_cliente = cliente["CD_CLIENTE"]
        
        # aqui estou filtrando as transações do cliente no mes e ano citados
        transacoes_mes = [
            t for t in TbTransacoes
            if t["CD_CLIENTE"] == cd_cliente and 
               t["DT_TRANSACAO"].startswith(f"{ano}-{str(mes).zfill(2)}") #aqui to usando o metodo "zfill" para preencher com zeros na esquerda até ter o tamanho que preciso.
        ]

        # aqui eu estou calculando entradas e saidas de forma básica
        entradas = sum(t["VR_TRANSACAO"] for t in transacoes_mes if t["CD_TRANSACAO"] in [000, 110])
        saidas = sum(t["VR_TRANSACAO"] for t in transacoes_mes if t["CD_TRANSACAO"] == 220)

        # aqui estou calculando o saldo médio = (Entradas - Saídas) / dias no mês (metamtica simples)
        saldo_medio = (entradas - saidas) / dias_no_mes
        saldo_medio_por_cliente[cd_cliente] = saldo_medio

    # descobrindo o cliente com maior saldo médio
    cliente_com_maior_saldo = max(saldo_medio_por_cliente, key=saldo_medio_por_cliente.get)
    saldo_maximo = saldo_medio_por_cliente[cliente_com_maior_saldo]

    # encontrando o nome do cliente
    nome_cliente = next(cliente["NM_CLIENTE"] for cliente in TbCliente if cliente["CD_CLIENTE"] == cliente_com_maior_saldo)

    # mostrar a resposta para a primeira pergunta: Qual cliente teve o maior saldo médio no mês 11?
    print(f"O cliente com maior saldo médio no mês {mes}/{ano} foi {nome_cliente} com saldo médio de R${saldo_maximo:.2f}")

# chamando a função para novembro de 2021
calcular_saldo_medio(11, 2021)
print("\n")

print("2- Qual é o saldo de cada cliente?")
# agora vou para a segunda pergunta: Qual é o saldo de cada cliente?
def calcular_saldo_clientes():
    saldos = {}

    # iniciando o saldo de cada cliente como 0
    for cliente in TbCliente:
        saldos[cliente["CD_CLIENTE"]] = 0

    # analisando todas as transacoes e atualizando o saldo de cada cliente
    for transacao in TbTransacoes:
        cd_cliente = transacao["CD_CLIENTE"]
        valor = transacao["VR_TRANSACAO"]

        if transacao["CD_TRANSACAO"] in [000, 110]:  # CashBack e CashIn soma saldo
            saldos[cd_cliente] += valor
        elif transacao["CD_TRANSACAO"] == 220:  # CashOut tira do saldo
            saldos[cd_cliente] -= valor

    # mostrar o saldo de cada cliente
    print("Saldo dos clientes:")
    for cliente in TbCliente:
        cd_cliente = cliente["CD_CLIENTE"]
        nome = cliente["NM_CLIENTE"]
        saldo = saldos[cd_cliente]
        print(f"Cliente: {nome} | Saldo: R${saldo:.2f}")

# chamando a funcao para calcular e mostrar os saldos
calcular_saldo_clientes()
print("\n")

print("3- Qual é o saldo médio de clientes que receberam CashBack?")

def calcular_saldo_medio_cashback():
    saldos = {}
    clientes_com_cashback = set()  # aqui eu uso um conjunto para armazenar os clientes que receberam CashBack.

    # novamente, comecando com o saldo 0 de cada cliente
    for cliente in TbCliente:
        saldos[cliente["CD_CLIENTE"]] = 0

    # analisando todas as transacoes e atualizando o saldo de cada cliente novamente
    for transacao in TbTransacoes:
        cd_cliente = transacao["CD_CLIENTE"]
        valor = transacao["VR_TRANSACAO"]

        if transacao["CD_TRANSACAO"] == 000:  # localizando clientes que receberam CashBack
            clientes_com_cashback.add(cd_cliente)
            saldos[cd_cliente] += valor
        elif transacao["CD_TRANSACAO"] == 110:  # CashIn soma saldo
            saldos[cd_cliente] += valor
        elif transacao["CD_TRANSACAO"] == 220:  # CashOut tira saldo
            saldos[cd_cliente] -= valor

    # filtrando apenas os clientes que receberam CashBack
    saldos_cashback = [saldos[cd_cliente] for cd_cliente in clientes_com_cashback]

    # aqui estou calculando o saldo medio dos ultimos clientes
    if len(saldos_cashback) > 0:
        saldo_medio = sum(saldos_cashback) / len(saldos_cashback)
    else:
        saldo_medio = 0  # se nenhum cliente recebeu CashBack o saldo médio fica 0

    print(f"O saldo médio dos clientes que receberam CashBack é R${saldo_medio:.2f}")

# chamando a funcao para calcular e exibir a resposta da terceira pergunta.
calcular_saldo_medio_cashback()
print("\n")

print("4- Qual o ticket médio das quatro últimas movimentações dos usuários?")
def calcular_ticket_medio_ultimas_4():
    ticket_medio_clientes = {}

    # juntas as transacoes do clientes em oredm de data
    transacoes_por_cliente = {}
    for transacao in sorted(TbTransacoes, key=lambda x: x["DT_TRANSACAO"]):
        cd_cliente = transacao["CD_CLIENTE"]
        if cd_cliente not in transacoes_por_cliente:
            transacoes_por_cliente[cd_cliente] = []
        transacoes_por_cliente[cd_cliente].append(transacao["VR_TRANSACAO"])

    # calculando o ticket medio para cada cliente considerando as ultimas 4 transacoes
    for cd_cliente, transacoes in transacoes_por_cliente.items():
        ultimas_4 = transacoes[-4:]  # peguei as 4 ultimas transacoes
        if len(ultimas_4) == 4:
            ticket_medio = sum(ultimas_4) / 4
        else:
            ticket_medio = sum(ultimas_4) / len(ultimas_4)  # se houver menos de 4 faz a media com o que tem
        ticket_medio_clientes[cd_cliente] = ticket_medio

    # mostrar a resposta da quarta questao
    print("Ticket médio das quatro últimas movimentações:")
    for cliente in TbCliente:
        cd_cliente = cliente["CD_CLIENTE"]
        nome = cliente["NM_CLIENTE"]
        ticket_medio = ticket_medio_clientes.get(cd_cliente, 0)
        print(f"Cliente: {nome} | Ticket Médio: R${ticket_medio:.2f}")

# chamando a funcao para calcular e mostrar o ticket medio
calcular_ticket_medio_ultimas_4()
print("\n")

print("5- Qual é a proporção entre Cash In/Out mensal?")

def proporcao_cash_in_out():
    proporcao_mensal = defaultdict(lambda: {"CashIn": 0, "CashOut": 0})

    for transacao in TbTransacoes:
        mes = transacao["DT_TRANSACAO"][:7]  # formato em YYYY-MM
        if transacao["CD_TRANSACAO"] == 110:
            proporcao_mensal[mes]["CashIn"] += transacao["VR_TRANSACAO"]
        elif transacao["CD_TRANSACAO"] == 220:
            proporcao_mensal[mes]["CashOut"] += transacao["VR_TRANSACAO"]
# a proporcao foi calculada como: proporcao = total CashIn no mes / total CashOut no mes
    print("Proporção Cash In/Out por mês:")
    for mes, valores in proporcao_mensal.items():
        cash_in = valores["CashIn"]
        cash_out = valores["CashOut"]
        proporcao = cash_in / cash_out if cash_out > 0 else float('inf')
        print(f"{mes}: {proporcao:.2f}")

proporcao_cash_in_out()
print("\n")

print("6- Qual a última transação de cada tipo para cada usuário?")

def ultima_transacao_por_tipo():  # dicionario para armazenar a ultima transacao de cada tipo para cada cliente
    ultimas = {}

    # analisando todas as transacoes na tabela TbTransacoes
    for transacao in TbTransacoes:
        cd_cliente = transacao["CD_CLIENTE"] #usando o codigo do cliente
        tipo = transacao["CD_TRANSACAO"]     #usando o tipo de transacao (000, 110, 220)
        chave = (cd_cliente, tipo)           #criando uma chave unica baseada no cliente e tipo de transacao


        #se a chave ainda nao estiver no dicionario ou se a transacao for mais recente, atualizar
        if chave not in ultimas or transacao["DT_TRANSACAO"] > ultimas[chave]["DT_TRANSACAO"]:
            ultimas[chave] = transacao


    #mostrando os resultados
    print("Última transação de cada tipo por usuário:")
    for chave, transacao in ultimas.items():
        print(f"Cliente {chave[0]} | Tipo {chave[1]} | Data {transacao['DT_TRANSACAO']} | Valor R${transacao['VR_TRANSACAO']:.2f}")

#chamando a funcao
ultima_transacao_por_tipo()
print("\n")

print("7- Qual a última transação de cada tipo para cada usuário por mês?")

def ultima_transacao_por_tipo_mes():
    ultimas = {}

    for transacao in TbTransacoes:
        mes = transacao["DT_TRANSACAO"][:7]                                # retirando apenas o ano e o mes da data (YYYY-MM)
        chave = (transacao["CD_CLIENTE"], transacao["CD_TRANSACAO"], mes)  # criando uma chave unica (cliente, tipo de transacao, mes

        if chave not in ultimas or transacao["DT_TRANSACAO"] > ultimas[chave]["DT_TRANSACAO"]:
            ultimas[chave] = transacao

    print("Última transação de cada tipo por usuário por mês:")
    for chave, transacao in ultimas.items():
        print(f"Cliente {chave[0]} | Tipo {chave[1]} | Mês {chave[2]} | Data {transacao['DT_TRANSACAO']} | Valor R${transacao['VR_TRANSACAO']:.2f}")

ultima_transacao_por_tipo_mes()
print("\n")

print("8- Qual quatidade de usuários que movimentaram a conta?")

def qtd_usuarios_movimentaram_conta(): # criando um conjunto (set) para armazenar os clientes que realizaram transacoes
    usuarios = {transacao["CD_CLIENTE"] for transacao in TbTransacoes}
    print(f"Quantidade de usuários que movimentaram a conta: {len(usuarios)}")

qtd_usuarios_movimentaram_conta()
print("\n")

print("9- Qual o balanço do final de 2021?")

def balanco_final_2021():        
    saldo = defaultdict(float)  # aqui criei um dicionario com valores padrao float (0.0) para armazenar o saldo dos clientes

    for transacao in TbTransacoes:
        if transacao["DT_TRANSACAO"][:4] == "2021": # verificando se a transacao ocorreu no ano de 2021
            if transacao["CD_TRANSACAO"] in [000, 110]:   # se a transacao for do tipo CashBack (000) ou CashIn (110), adicionamos ao saldo do cliente
                saldo[transacao["CD_CLIENTE"]] += transacao["VR_TRANSACAO"] # se a transacao for do tipo CashOut (220), subtraimos do saldo do cliente
            elif transacao["CD_TRANSACAO"] == 220:
                saldo[transacao["CD_CLIENTE"]] -= transacao["VR_TRANSACAO"]

    balanco_total = sum(saldo.values())  # calculando o balanco total somando os saldos de todos os clientes
    print(f"Balanço total do final de 2021: R${balanco_total:.2f}")

balanco_final_2021()
print("\n")

print("10- Quantos usuários que receberam CashBack continuaram interagindo com este banco?")

def usuarios_cashback_interagiram():
    usuarios_cashback = {t["CD_CLIENTE"] for t in TbTransacoes if t["CD_TRANSACAO"] == 000}
    usuarios_movimentaram = {t["CD_CLIENTE"] for t in TbTransacoes} # criando um conjunto com todos os clientes que realizaram qualquer tipo de transacao
    interagiram = usuarios_cashback & usuarios_movimentaram  # encontrando a intersecao dos dois conjuntos, clientes que receberam CashBack e continuaram movimentando a conta

    print(f"Usuários que receberam CashBack e continuaram interagindo: {len(interagiram)}")

usuarios_cashback_interagiram()
print("\n")

print("11- Qual a primeira e a última movimentação dos usuários com saldo maior que R$100?")

def primeira_ultima_movimentacao_saldo_maior_100():
    saldo = defaultdict(float)
    transacoes_cliente = defaultdict(list)

    for transacao in TbTransacoes:
        cd_cliente = transacao["CD_CLIENTE"]
        transacoes_cliente[cd_cliente].append(transacao)
        if transacao["CD_TRANSACAO"] in [000, 110]: # se for CashBack (000) ou CashIn (110), adicionamos ao saldo
            saldo[cd_cliente] += transacao["VR_TRANSACAO"]
        elif transacao["CD_TRANSACAO"] == 220:      # se for CashOut (220), subtraímos do saldo
            saldo[cd_cliente] -= transacao["VR_TRANSACAO"]

    for cd_cliente, transacoes in transacoes_cliente.items():
        if saldo[cd_cliente] > 100:  # verificando se o saldo do cliente e maior que R$100
            transacoes.sort(key=lambda x: x["DT_TRANSACAO"]) # ordenando as transacoes do cliente por data (do mais antigo para o mais recente)
           
            # pegando a primeira e a ultima transacao apos a ordenacao
            print(f"Cliente {cd_cliente}:")
            print(f"  Primeira: {transacoes[0]['DT_TRANSACAO']} | R${transacoes[0]['VR_TRANSACAO']:.2f}")
            print(f"  Última: {transacoes[-1]['DT_TRANSACAO']} | R${transacoes[-1]['VR_TRANSACAO']:.2f}")

primeira_ultima_movimentacao_saldo_maior_100()
print("\n")

print("12- Qual o balanço das últimas quatro movimentações de cada usuário?")

def balanco_ultimas_4_mov():
    for cd_cliente in {t["CD_CLIENTE"] for t in TbTransacoes}:                         
        ultimas_4 = sorted([t for t in TbTransacoes if t["CD_CLIENTE"] == cd_cliente], key=lambda x: x["DT_TRANSACAO"])[-4:]     # ordenando as transacoes por data, garantindo que as mais recentes fiquem no final
        balanco = sum(t["VR_TRANSACAO"] if t["CD_TRANSACAO"] in [000, 110] else -t["VR_TRANSACAO"] for t in ultimas_4)           # calculando o balanco das ultimas 4 movimentacoes
        print(f"Cliente {cd_cliente} | Balanço das últimas 4 movimentações: R${balanco:.2f}")

balanco_ultimas_4_mov()
print("\n")

print("13- Qual o ticket médio das últimas quatro movimentações de cada usuário?")

def ticket_medio_ultimas_4():
    for cd_cliente in {t["CD_CLIENTE"] for t in TbTransacoes}:
        ultimas_4 = sorted([t["VR_TRANSACAO"] for t in TbTransacoes if t["CD_CLIENTE"] == cd_cliente], reverse=True)[:4] # filtrando todas as transações do cliente e as ordena pelas maiores para as menores.
        ticket_medio = sum(ultimas_4) / len(ultimas_4) if ultimas_4 else 0    # calculando o ticket medio (media das 4 maiores transacoes)
        print(f"Cliente {cd_cliente} | Ticket Médio das últimas 4 movimentações: R${ticket_medio:.2f}")

ticket_medio_ultimas_4()
