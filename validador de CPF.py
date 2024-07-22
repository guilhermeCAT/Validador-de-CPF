import re
import sys

cpf = input('Digite seu CPF: ')
verificador_cpf = re.sub(r'[^0-9]','',cpf)
nove_digitos_do_CPF = cpf[:9]
contador_regressivo_1 = 10 

caracter_sequencial = cpf == cpf[0] *len(cpf)

if caracter_sequencial:
    print('Voce enviou dados sequenciais')
    sys.exit()

resultado_digito_1 = 0
for numero in nove_digitos_do_CPF:
    resultado_digito_1 += int(numero) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos_do_CPF = nove_digitos_do_CPF + str(primeiro_digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for numero in dez_digitos_do_CPF:
    resultado_digito_2 += int(numero) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo_digito = (resultado_digito_2 * 10) % 11 
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

CPF_gerado = f'{nove_digitos_do_CPF}{primeiro_digito}{segundo_digito}'

if cpf == CPF_gerado:
    print(f'CPF: {nove_digitos_do_CPF[:3]}.{nove_digitos_do_CPF[3:6]}'\
    f'.{nove_digitos_do_CPF[6:9]}-{primeiro_digito}{segundo_digito} e valido')
else:
    print('CPF invalido')
