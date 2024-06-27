def calculadora():
    # Solicita os numeros ao usuario
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Solicita a operacao ao usuario
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = int(input("Digite o número da operação desejada: "))
    
    # Realiza a operacao escolhida
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0


resultado = calculadora()
print("Resultado:", resultado)
