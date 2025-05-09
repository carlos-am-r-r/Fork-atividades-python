ct= 0
ctpar = 0
ctimpar= 0
somapar = 0
somaimpar = 0
print(" digite 0 para sair")
while True:
     valor = int(input("digite o valor:"))
     if valor == 0:
         break
     ct = ct + 1
     if valor % 2 == 0:
         ctpar= ctpar + 1
         somapar = somapar + valor
     if valor % 2 == 1:
         ctimpar= ctimpar + 1
         somaimpar= ctimpar + valor

mediapar = somapar/ctpar
mediaimpar = somaimpar/ ctimpar
print("media dos impares:",mediaimpar)
print("media dos par:",mediapar)





