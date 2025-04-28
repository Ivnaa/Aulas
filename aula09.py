#listas

nome = "Joao Lira"
vendas = [100, 50, 130, 80, 120]


print(vendas[0])

# ultimo elemento da lista
print(vendas[-1])

#outras funcoes
total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print(posicao)

print(vendas[:2])


produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

#editando um valor de uma lista
print("iphone" in produtos)
precos[0]=4500
precos[0]= precos[0]*1.1
print(precos)

#adicionando um valor em uma lista
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

#removendo um item
produtos.remove("macbook") #pelo valor
precos.pop(-1) #pelo indice
print(produtos)
print(precos)

#adicionando um item em um indice
produtos.insert(1,"airpod")
print(produtos)

#contando valores
print(produtos.count("airpod"))

#ordenar
precos.sort(reverse=True)
print(precos)