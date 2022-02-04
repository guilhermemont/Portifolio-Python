Comprimento = (float(input("Digite o valor do comprimento em mm: ")))/100
Largura = (float(input("Digite o valor da largura em mm: ")))/100
Altura = (float(input("Digite o valor da altura em mm: ")))/100
areadaCaixa = ((Comprimento*Largura) + (2*Largura*Altura) + (2*Comprimento*Altura))
volumetotal = Comprimento*Largura*Altura
volumeporcompartimento = volumetotal/2
diagonal = (((Comprimento**2)+(Largura**2))**(1/2))
areaDivisoria = (diagonal*Altura)
materialnecessario = areaDivisoria + areadaCaixa
print("CARACTERÍSTICAS DA CAIXA:")
print("Altura: ", Altura,"m")
print("Largura: ", Largura,"m")
print("Comprimento: ", Comprimento,"m")
print("Área da divisória: ",(areaDivisoria),"m2")
print("Volume Total: ",(volumetotal),"m3")
print("Volume por compartimento: ", (volumeporcompartimento),"m3")
print("Área de material necessário : ",(materialnecessario),"m2")
