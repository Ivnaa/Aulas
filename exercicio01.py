#exercícios
nome = "Ivna de Carvalho Façanha"
email = "ivnacd@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
print(posicao)
servidor = email[posicao:]
print(servidor)

# pegar o 1º nome do usuário
posicao2 = nome.find(" ")
print(posicao2)
firstname = nome[:posicao2]
print(firstname)

# construa uma mensagem: Usuario primeiro_nome cadstrado com sucesso com o email tal
print(f"{firstname} cadastrado com sucesso no email {email}")

# construa uma mensagem: Enviamos um link de confirmação para o email i***@gmail.com
primeiraletra = email[0]
emailconfirmacao = primeiraletra + "***" + servidor
print(f"Enviamos uma mensagem de confirmação para o email {emailconfirmacao}")