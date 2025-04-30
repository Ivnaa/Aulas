# faturamento = 1000
# custo = 2000

# lucro = faturamento - custo

# if lucro > 0:
#     print("Lucro:",lucro) 
# elif lucro == 0:
#     print("Não houve prejuizo nem lucro")

# else:
#     print("Prejuizo", lucro)



# produtos = ["iphone","ipad","airpod"]
# novo_produto = input("Digite aqui o produto:")
# novo_produto = novo_produto.lower()

# if novo_produto in produtos:
#     print("produto já cadastrado")
# else:
#     print("Produto cadastrado com sucesso")
#     produtos.append(novo_produto)

# print(produtos)


#acima de 15000 -> 500 de bonus
#acima de 10000 -> 150 de bonus 
#acima de 5000 -> 50 bonus


# vendas = 6000

# if vendas > 15000:
#     bonus = 500
# elif vendas > 10000:
#     bonus = 150
# elif vendas > 5000:
#     bonus = 50
# else:
#     bonus = 0

# print("Bonus", bonus)


#acima de 15000 -> 500 de bonus
#acima de 10000 -> 150 de bonus 
#acima de 5000 -> 50 bonus
#vendas empresa > 50000 

vendas = 16000
vendas_empresa = 60000
meta_empresa = 50000


if vendas > 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas > 10000 and vendas_empresa > meta_empresa:
    bonus = 150
elif vendas > 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0

print(bonus)



