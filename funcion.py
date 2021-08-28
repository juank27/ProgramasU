def minmax(a,b):
   if a < b:
      return [a, b]
   else:
      return[b, a]


aa = int(input("numero 1 = "))
bb = int(input("numero 2 = "))

min, max = minmax(aa,bb)
print("minimo = ", min, ", ", "max = ", max)