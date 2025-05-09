valor1=float(input('Selecione o primeiro valor:'))
valor2=float(input('Selecione o segundo valor:'))
valor3=float(input('selecione o terceiro valor:'))
if valor1 >= valor2:
    if valor1 >= valor3:
        print(f"o valor {valor1} é o maior")
    else:
        print(f"o valor {valor3} é maior")
elif valor1 <= valor2:
    if valor2 >= valor3:
        print(f"o valor {valor2} é o maior")
    else:
        print(f"o valor {valor3}é o maior")

