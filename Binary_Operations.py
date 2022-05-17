import sys

#Função para Conversão de String para Vetor
def converter_vetor(x):
    vetor = []

    for i in range(0, 32, 1):
        vetor.append(int(x[i]))

    return vetor

#Função para Conversão de Binário para Decimal (SINAL-MAGNITUDE)
def decimal_SM(x):
    numero_decimal = 0
    expoente = 0

    for i in range(31, 0, -1):
        numero_decimal = numero_decimal + ((2 ** expoente) * x[i])
        expoente = expoente + 1

    if (x[0] == 0):
        numero_decimal = numero_decimal * 1

    else:
        numero_decimal = numero_decimal * (-1)

    return numero_decimal

#Função para Comparação de Sinais (SINAL-MAGNITUDE)
def comparacao_sinais(x,y):
    if (x[0] == y[0]):
        operacao = operacao_SM_iguais(x,y)

    else:

        if (abs(decimal_SM(x)) >= abs(decimal_SM(y))):
            operacao = operacao_SM_diferentes(x, y)

        else:
            operacao = operacao_SM_diferentes(y, x)

    return operacao

#Função para Operação de Binários (SINAL-MAGNITUDE; SINAIS IGUAIS)
def operacao_SM_iguais(x,y):
    operacao_resultado = [x[0]] * 32
    excesso = 0

    for i in range(31, 0, -1):
        operacao = x[i] + y[i] + excesso

        if ((operacao == 0) or (operacao == 2)):
            indice_valor = 0

        else:
            indice_valor = 1

        if (operacao > 1):
            excesso = 1

        else:
            excesso = 0

        operacao_resultado[i] = indice_valor

    return operacao_resultado

#Função para Operação de Binários (SINAL-MAGNITUDE; SINAIS DIFERENTES)
def operacao_SM_diferentes(x,y):
    operacao_resultado = [x[0]] * 32
    empresta = 0

    for i in range(31, 0, -1):
        operacao = x[i] - y[i] - empresta

        if (operacao == 0 or operacao == -2):
            indice_valor = 0

        else:
            indice_valor = 1

        if (operacao < 0):
            empresta = 1

        else:
            empresta = 0

        operacao_resultado[i] = indice_valor

    return operacao_resultado

#Função para Analisar o Sinal (Complemento de 2)
def decimal_C2(x):
    if (x[0] == 0):
        numero_decimal = decimal_SM(x)

    else:
        numero_invertido = inverter_numero(x)
        numero_decimal = 0
        expoente = 0

        for i in range(31, -1, -1):
            numero_decimal = numero_decimal + ((2 ** expoente) * numero_invertido[i])
            expoente = expoente + 1

        numero_decimal = numero_decimal * (-1)

    return numero_decimal

#Função para Inverter o Número
def inverter_numero(x):
    numero_invertido = [0] * 32

    for i in range(0, 32, 1):

        if (x[i] == 1):
            numero_invertido[i] = 0

        else:
            numero_invertido[i] = 1

    excesso = 1

    for i in range(31, -1, -1):
        soma = numero_invertido[i] + excesso

        if ((soma == 0) or (soma == 2)):
            indice_valor = 0

        else:
            indice_valor = 1

        if (soma > 1):
            excesso = 1

        else:
            excesso = 0

        numero_invertido[i] = indice_valor

    return numero_invertido

#Função para Operação de Binários (COMPLEMENTO DE 2)
def operacao_C2(x,y):
    operacao_resultado = [0] * 32
    excesso = 0

    for i in range(31, -1, -1):
        operacao = x[i] + y[i] + excesso

        if ((operacao == 0) or (operacao == 2)):
            indice_valor = 0

        else:
            indice_valor = 1

        if (operacao > 1):
            excesso = 1

        else:
            excesso = 0

        operacao_resultado[i] = indice_valor

    return operacao_resultado

#Manipulação do Arquivo de Texto

nome_do_arquivo = sys.argv[1]
manipulador = open(nome_do_arquivo, "r")
total_de_linhas = sum(1 for line in open(nome_do_arquivo))
contador = 0

#Laço do Programa
while (contador < total_de_linhas):

    #Atribuição dos Valores do Arquivo de Texto
    n1_string = str(manipulador.readline())
    n2_string = str(manipulador.readline())

    n1 = converter_vetor(n1_string)
    n2 = converter_vetor(n2_string)

    #Saída dos Números em Decimal (SINAL-MAGNITUDE)
    dec_n1_SM = decimal_SM(n1)
    dec_n2_SM = decimal_SM(n2)

    print(dec_n1_SM)
    print(dec_n2_SM)
    print()

    #Soma dos Binários (SINAL-MAGNITUDE)
    soma_n1_n2 = comparacao_sinais(n1,n2)

    #Subtração dos Binários (SINAL-MAGNITUDE)
    if(n2[0] == 1):
        n2_sinal_invertido = [0]

    else:
        n2_sinal_invertido = [1]

    for i in range(1, 32, 1):
        n2_sinal_invertido.append(n2[i])

    subtracao_n1_n2 = comparacao_sinais(n1,n2_sinal_invertido)

    #Saída dos Resultados das Operações em Binário (SINAL-MAGNITUDE)
    print(*soma_n1_n2, sep="")
    print(*subtracao_n1_n2, sep="")
    print()

    #Saída dos Resultados das Operações em Decimal (SINAL-MAGNITUDE)
    print(dec_n1_SM + dec_n2_SM)
    print(dec_n1_SM - dec_n2_SM)
    print()

    #Saída dos Números em Decimal (COMPLEMENTO DE 2)
    dec_n1_C2 = decimal_C2(n1)
    dec_n2_C2 = decimal_C2(n2)

    print(dec_n1_C2)
    print(dec_n2_C2)
    print()

    #Soma dos Binários (COMPLEMENTO DE 2)
    soma_n1_n2 = operacao_C2(n1,n2)

    #Subtração dos Binários (COMPLEMENTO DE 2)
    n2_invertido = inverter_numero(n2)

    subtracao_n1_n2 = operacao_C2(n1,n2_invertido)

    #Saída dos do Resultado das Operações em Binário (COMPLEMENTO DE 2)
    print(*soma_n1_n2, sep="")
    print(*subtracao_n1_n2, sep="")
    print()

    #Saída dos Resultados das Operações em Decimal (COMPLEMENTO DE 2)
    print(dec_n1_C2 + dec_n2_C2)
    print(dec_n1_C2 - dec_n2_C2)
    print()

    #Pular a Linha em Branco e Conferir Continuidade do Código
    manipulador.readline()
    contador = contador + 3