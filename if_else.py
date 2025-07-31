def caixa_eletronico():
    saldo = int( input("digite o saldo bancario"))
    saque = int( input("digite o valor do saque")) 
    if saldo >= saque:
        saldo -= saque 
        print("voce realizou um saque com sucesso.",saldo)
    else: 
        print("voce nao possui saldo suficiente para realizar essa operaçao",saldo)
#caixa_eletronico()

def caixa_eletronico_deposito():
    saldo = int(input("digite o valor do saldo bancario"))
    deposito = int(input("diguite o valor do deposito"))
    if saldo >= deposito:
        saldo += deposito 
        print("voce realizou um deposito com sucesso.",saldo)
    else:
        print("ocorreu um erro ao depositar",saldo)
#caixa_eletronico_deposito() 

def porcentagem():
    valor_parte = float(input("insira o valor parte: "))
    porcentagem = float(input("insira o valor da porcentagem: "))
    if porcentagem<= 0.0:
        print("insira um numero maior que 0")
    else:
        valor_total = valor_parte * (porcentagem/100)
        print(valor_total)
porcentagem()

