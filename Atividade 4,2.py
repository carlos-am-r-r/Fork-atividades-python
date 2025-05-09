valor1 = int(input("coloque o valor:"))
calculo = int(input("selecione a operação\n1+ adição\n2- subtração\n3* multiplicação\n4/ divisão\n"))
if calculo == 1:
    valor2 =int(input("coloque o valor:"))
    resultado = valor1 + valor2
    print("resultado =",resultado)
if calculo == 2:
    valor2 = int(input("coloque o valor:"))
    resultado = valor1 - valor2
    print("resultado =", resultado)
if calculo == 3:
    valor2 = int(input("coloque o valor:"))
    resultado = valor1 * valor2
    print("resultado =", resultado)
if calculo == 4:
    valor2 = int(input("coloque o valor:"))
    resultado = valor1 / valor2
    print("resultado =", resultado)