soma = 0
num = 5
atividade = int(input("Digite o numero corresponde a atividade:\n atividade1 \n atividade2 \n atividade3 \n atividade4 \n atividade5 \n atividade6"))
if atividade == 1:
    print("Fahrenheit | Celsius")
    print("-----------|---------")
    for f in range (45,81):
        c = (5 *  (f-32))/9
        print(f" {f:.1f} Fº | {c:.3f} Cº")
if atividade == 2:
    valor = int(input("Digite o valor em fahrenheit"))
    print("Fahrenheit | Celsius")
    print("-----------|---------")

    for f in range(valor,80,1):
        c = (5 * (valor - 32)) / 9
        print(f" {valor:.1f} Fº | {c:.3f} Cº")
if atividade == 3:
    for f in range(1,501):
        soma += f
    print("a soma dos números de 1 a 500 é:", soma)
if atividade == 4:
    for numero in range(1, 501):
        if numero % 2 != 0 and numero % 3 == 0:
            soma += numero
    print("A soma dos números ímpares e múltiplos de 3 de 1 a 500 é:", soma)
if atividade == 5:
    for i in range(1, 11):
        resultado = i * num
        print(f"{i:>2}  x  {num}  =  {resultado:>3}")
if atividade == 6:
    numero = int(input("Digite um número inteiro para ver sua tabuada: "))
    print(f"\nTabuada do {numero}:\n")
    for i in range(1, 11):
        resultado = i * numero
        print(f"{i:>2}  x  {numero}  =  {resultado:>3}")

