# Brindar un listado de los numeros primos del 1 al 100

def evaluar_primo(x):
    es_primo=True
    for i in range(2,x):
        if x % i==0:
            es_primo=False
            
    return es_primo

# lo que voy a evaluar es los numeros del 1 al 100
listado_primos = []
for i in range(1,101):
    # evaluare cada numero
    es_primo = evaluar_primo(i)

    if es_primo:
        listado_primos.append(i)
print(listado_primos)