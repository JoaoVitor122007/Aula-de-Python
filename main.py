print("---Bem vindo à calculadora feita em Python---\n")

while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("Escolha a operação que você deseja realizar com os dois números anteriores:")
    print("Adição(1) \nSubtração(2) \nMultiplicação(3) \nDivisão(4) \nSair(5)")

    escolha = int(input())

    if escolha == 1:
        print("Resultado:", num1 + num2)
    elif escolha == 2:
        print("Resultado:", num1 - num2)
    elif escolha == 3:
         print("Resultado:", num1 * num2)
    elif escolha == 4:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Impossível dividir por zero!")
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Escolha inválida, tente novamente")
