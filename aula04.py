#if else 

#idade = int( input("Informe a sua idade: "))

#if idade >= 18:
    #print("PERMITIDO")
#else:
    #print("BLOQUEADO")

salario = float(input("Informe o seu salario: "))

if salario <= 3000:
    print("Programador júnior")
elif salario > 3000 and salario <= 7000:
    print("Programador pleno")
elif salario > 7000 and salario <= 15000:
    print("Programador senior")
else:
    print("Gerente de projetos")