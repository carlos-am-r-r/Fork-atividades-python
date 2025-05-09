valor1=float(input('Selecione o primeiro valor:'))
valor2=float(input('Selecione o segundo valor:'))
valor3=float(input('selecione o terceiro valor:'))

if valor1 + valor2 > valor3 and valor1 + valor3 > valor2 and valor2 + valor3 > valor1:
   if valor1 == valor2 == valor3:
       print("é um triangulo equilatero")
   elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
       print("é um triangulo isosceles")
   elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
       print("é um triangulo escaleno")
else:
    print("n é um triangulo")