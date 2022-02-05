salariominimo = float(input("Digite o salário mínimo: "))
salario = float(input("Digite o salário: "))
if (salario/salariominimo) <= 10:
    emprestimomaximo = float((salario*0.2)*24)
    prestação = float(emprestimomaximo/24)
    numerodeprestacoes = int(24)
else:
    emprestimomaximo = float((salario*0.3)*36)
    prestação = float(emprestimomaximo/36)
    numerodeprestacoes = int(36)
print(f"\nSALÁRIO MÍNIMO: {salariominimo}", f"\nSALÁRIO: {salario}", f"\nEMPRESTIMO MÁXIMO: {emprestimomaximo}", f"\nPRESTAÇÃO: {prestação}", f"\nNÚMERO DE PRESTAÇÕES: {numerodeprestacoes}") 
