#Definição das variáveis
matricula = str(input("Digite a matrícula: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
#Leitura dos dados
#Leia matricula,Nota1,Nota2,Nota3
#Calculo da nota final
notaFinal = (nota1+(2*nota2)+(3*nota3))/6
print(matricula,": ",notaFinal)
#Avaliação
if notaFinal >= 90:
  print("Aluno aprovado com conceito A")
elif notaFinal >= 80:
  print("Aluno aprovado com conceito B")
elif notaFinal >= 70:
  print("Aluno aprovado com conceito C")
elif notaFinal >= 60:
  print("Aluno aprovado com conceito D")
elif notaFinal >= 40:
  print("Aluno em recuperação - fazer Exame especial")
else:
  print("Aluno reprovado")
