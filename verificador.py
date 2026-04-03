def primeiro_digito(numeros_cpf):
    nove_digitos = numeros_cpf[:9]
    soma = 0
    multiplicador = 10

    for i in nove_digitos:
        soma += int(i) * multiplicador
        multiplicador -= 1

    soma_mult = soma * 10
    digito_teste = soma_mult % 11
    digito_final_1 = digito_teste if digito_teste <= 9 else 0
    return digito_final_1


def segundo_digito(numeros_cpf, digito_final_1):
    dez_digitos = numeros_cpf[:9] + str(digito_final_1)
    soma = 0
    multiplicador = 11

    for i in dez_digitos:
        soma += int(i) * multiplicador
        multiplicador -= 1

    soma_mult = soma * 10
    digito_teste = soma_mult % 11
    digito_final_2 = digito_teste if digito_teste <= 9 else 0
    return digito_final_2


coleta_cpf = input('Digite o CPF: ')
apenas_numeros_cpf = "".join([num for num in coleta_cpf if num.isdigit()])

if len(apenas_numeros_cpf) != 11:
    print('CPF inválido - Tamanho incorreto.')
else:
    d1 = primeiro_digito(apenas_numeros_cpf)
    d2 = segundo_digito(apenas_numeros_cpf, d1)

    real_d1 = int(apenas_numeros_cpf[9])
    real_d2 = int(apenas_numeros_cpf[10])

    if d1 == real_d1 and d2 == real_d2:
        print('CPF válido.')
    else:
        print('CPF inválido - Dígitos verificadores não correspondem.')
