xa = float(input("Digite x do primeiro vertice: "))
ya = float(input("Digite y do primeiro vertice: "))
xb = float(input("Digite x do segundo vertice: "))
yb = float(input("Digite y do segundo vertice: "))
xc = float(input("Digite x do terceiro vertice: "))
yc = float(input("Digite y do terceiro vertice: "))
ladoA = (((xa-xb)**2)+((ya-yb)**2))**(1/2)
ladoB = (((xb-xc)**2)+((yb-yc)**2))**(1/2)
ladoC = (((xa-xc)**2)+((ya-yc)**2))**(1/2)
if ladoA > ladoB or ladoA > ladoC:
     if ladoB < ladoC:
          auxiliar = ladoA
          ladoA = ladoB
          ladoB = auxiliar
     else:
          auxiliar = ladoA
          ladoA = ladoC
          ladoC = auxiliar
     if ladoB > ladoC:
          auxiliar = ladoB
          ladoB = ladoC
          ladoC = auxiliar
p = (ladoA + ladoB + ladoC)/2
area = (p*(p-ladoA)*(p-ladoB)*(p-ladoC))**(1/2)
print("Lado A: ", ladoA)
print("Lado B: ", ladoB)
print("Lado C: ", ladoC)
print("Maior lado: ", ladoC)
print("Menor lado: ", ladoA)
print("Área: ", area)
