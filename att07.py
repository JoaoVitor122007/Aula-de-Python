fatorial = int(input("Digite um número: "))

contador = 1
resultado = 1
while contador <= fatorial:
    resultado *= contador
    contador += 1

print(resultado)
