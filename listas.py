lista = [1,2,3,"hola", 'a', 2.5]
lista2 = [5, "lista anidada", 1]
lista3 = [1,2,3]
lista4 = [1,2,3]
union_lista = lista +lista2
#print(lista3 ==  lista4)

#print(lista[-2])
"""
#buscando en una lista
print(lista)
if "holA" not in lista:
   print("no esta ")
else:
   print("si esta")
"""
#iterar lista
#for tipo in lista:
#   print(tipo, end=", ")

comprencion_de_lista = [x for x in range(0,3)]
#print(comprencion_de_lista)

#asignacion a variables
a = comprencion_de_lista[0]
#print(a)

#longitud
lista_nueva = [1,2,3,4,5,5,2]
#print(len(lista_nueva))
#agregando al final
#lista_nueva.append("6")
#print(lista_nueva)

#insertando
#lista_nueva.insert(4, "hola")
#lista_nueva.insert(0, "hola")
#remover
#lista_nueva.remove("hola")
#lista_nueva.remove("hola")
#slice
#print(lista_nueva[::-1])

#contar
#print(lista_nueva.count(5))

#index
#print(lista_nueva.index(2))

#max y min
#print(min(lista_nueva))
listaaa = [1,3,-3]
listaaa.sort()
lista_nueva.sort(reverse=True)
#print(lista_nueva)

#list
cadena = "hola a todos"
lista_cadena = list(cadena)
#print(lista_cadena)
#remueve una posicion
lista_borrar = ["n", "a", "d", "a"]
lista_borrar.pop(0)
print(lista_borrar)
