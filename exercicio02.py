# exercicio desafio
# sistema de consulta de preço

precos = [1500, 1000, 800, 2000]
produtos = ["celular","camera","fone de ouvido","monitor"]

produto_cliente = input("Digite o nome de um produto:")
produto_cliente = produto_cliente.lower()

# if produto_cliente in produtos:
#     if produtos[0] == produto_cliente:
#         print("O preço do produto digitado é:", precos[0])
#     elif produtos[1] == produto_cliente:
#         print("O preço do produto digitado é:", precos[1])
#     elif produtos[2] == produto_cliente:
#         print("O preço do produto digitado é:", precos[2])
#     elif produtos[3] == produto_cliente:
#         print("O preço do produto digitado é:", precos[3])
# else:
#     print("Produto não cadastrado")

if produto_cliente in produtos:
    posicao = produtos.index(produto_cliente)
    print("O preço do produto é:", precos[posicao])

else:
    print("Produto não cadastrado")
