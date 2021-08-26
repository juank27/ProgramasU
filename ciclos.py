#for i in range(0,11,3):
#   print(i)

"""ciclos.py
print("primera vez")
numero = 0
while(numero < 10):
   print(numero)
   numero = numero + 1
"""
#funciones

def ciclo(numero, numero_corte):
   while(numero < 10):
      print(numero)
      numero = numero + 1
      if numero_corte == 6:
         break


pedir_numero = int(input("EScriba un numero "))
cortar = int(input("Escriba numero para cortar ciclo: "))
print("primera ejecucion")
ciclo(cortar,pedir_numero)

print("Finalizo todo")
