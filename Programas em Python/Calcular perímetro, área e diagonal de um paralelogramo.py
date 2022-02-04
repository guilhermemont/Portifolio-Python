import math
ladoBase = float(input("Digite o valor do lado da base: "))
ladoAltura = float(input("Digite o valor da altura: "))
area =ladoBase*ladoAltura
perimetro = 2 * (ladoBase+ladoAltura)
diagonal = math.sqrt((ladoBase**2)+(ladoAltura**2))
print("\n Valores lidos: ")
print("\n Base: ", ladoBase, "\n Altura: ", ladoAltura)
print("\n Valores Calculados \n ")
print("\n Area: ",area, "\n Perimetro: ", perimetro, "\n Diagonal: ", diagonal)
print("\nPrograma executado com sucesso")
