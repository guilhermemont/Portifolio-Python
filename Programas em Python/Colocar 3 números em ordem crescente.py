a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
if a > b or a > c:
    if b < c:
    auxiliar = a
    a = b
    b = auxiliar
else:
    auxiliar = a
    a = c
    c = auxiliar
    if b > c:
    auxiliar = b
    b = c
    c = auxiliar
print(f"\na = {a:d}", f"\nb = {b:d}", f"\nc = {c:d}")
print( "\nPrograma executado com sucesso")
