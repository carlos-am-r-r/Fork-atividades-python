m= 0
f= 0
atividade = int(input("coloque o valor que corresponde a qual atividade vc vai:\n 1-atividade1\n 2-atividade2\n 3-atividade3\n 4-atividade4\n 5-atividade5"))
if atividade == 1:
    valor1 = float(input("digite o valor do raio:"))
    media_da_esfera = (4 * 3.14 * valor1 ** 3) / 3
    print("media_da_esfera", media_da_esfera)
if atividade == 2:
    valor2 = float(input("digite seu peso:"))
    valor_do_peso = valor2 *0.03
    print(f'a quantidade de água que você deve consumir é {valor_do_peso}')
if atividade == 3:
    plano1 = float(input("digite o valor do x1:"))
    plano2 = float(input("digite o valor do y1:"))
    plano3 = float(input("digite o valor do x2:"))
    plano4 = float(input("digite o valor do y2:"))
    distancia = ((plano1 - plano3)**2 + (plano2 - plano4)**2)**0.5
    print(f"a distância dos pontos no plano cartesiano é {distancia}")
if atividade == 4:
    valor3 = int(input("digite o valor:"))
    valor4 = int(input("digite o valor:"))
    if valor3 > valor4:
        print(f"o {valor3} é maior que {valor4}")
    else:
        print(f"o {valor4} é maior que {valor3}")
if atividade == 5:
    genero = input("coloque seu genero [m/f}:")
    if genero == "m":
        valor5 = float(input("digite a sua altura:"))
        resultado1 = (72.7*valor5)-58
        print(f"o seu peso ideal é {resultado1}")
    if genero == "f":
        valor6 = float(input("digite a sua altura:"))
        resultado2 = (62.1 * valor6) - 44,7
        print(f" o seu peso ideal é {resultado2}")
    







