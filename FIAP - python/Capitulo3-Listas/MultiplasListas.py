equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Serial: ')))
    departamentos.append(input('Departamentos: '))
    resposta = input('Digite "S" para continuar: ').upper()

for indice in range(0, len(equipamentos)):
    print('Equipamento...: ', [indice+1])
    print('Nome..........: ', equipamentos[indice])
    print('Valor.........: ', valores[indice])
    print('Serial........:', seriais[indice])
    print('Departamento..:', departamentos[indice])

busca = input('Digite o nome do Equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..: ', valores[indice])
        print('Serial.:', seriais[indice])

