faturamento = dict({'SP': dict({'valor': 67836.43}), 'RJ': dict({'valor':36678.66}), 'MG': dict({'valor':29229.88}), 'ES': dict({'valor':27165.48}), 'Outros': dict({'valor':19849.53})})

total = 0


for x in faturamento.keys():
    total += faturamento[x]['valor']


print('valor total (100%) : ' + str(total))

for x in faturamento.keys():
    valor = faturamento[x]['valor']
    print('Porcentagem de '+ x + ' e : '+ str((100*valor)/total) + "%")
