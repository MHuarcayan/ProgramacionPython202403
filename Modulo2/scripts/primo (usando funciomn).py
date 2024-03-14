
import math

def evaluar_primo(x):
    es_primo=True
    for i in range(2,x):
        if x % i==0:
            es_primo=False
            
    return es_primo


# solicitar al usuario numero 
numero = int(input("Ingresar un numero: "))

es_primo = evaluar_primo(x=numero)

if es_primo and numero>1:
    print("el numero es primo")
else:
    print("El numero no es primo")