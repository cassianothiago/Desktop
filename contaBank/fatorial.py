
'''print('='*120)
print('bem vindo ao fatorial')
fat=int(input('digite o numero: '))
cont=1
z=1
while cont<fat:
    cont=cont+1
    z=cont*z
print(z)
print('='*120)'''

def fatorial(n):
    if n==1:
        return 1
    else:
        return n*fatorial(n-1)
    
numero=5
result=fatorial(numero)
print(result) 