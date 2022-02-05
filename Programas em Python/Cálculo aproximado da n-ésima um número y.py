n = int(input('Digite a ordem do índice: '))
e = float(input('Digite a precisão: '))
y = float(input('Digite radicando: '))
x = y/n
def fdex(x,n,y):
    a = (x**n)-y
    return a
def derivadadefdex(x,n):
    b = n*(x**(n-1))
    return b
def raizdey(n,y,e):
    x = y/n
    while True:
        x = (x) - (fdex(x,n,y))/(derivadadefdex(x,n))
        if abs(fdex(x,n,y)) < e:
            return x
print('Raiz ',n,'de ',y,': ',x)

