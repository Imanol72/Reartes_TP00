"""  multiplicando = int(input("Ingrese el número que desea multiplicar: "))
multiplicador = int(input("Ingrese el número por el cual desea multiplicarlo: "))
counter = multiplicador
producto = 0

while counter != 0:
    producto += multiplicando
    counter -= 1 

print("El resultado de la multiplicación es igual a", producto)
 """
dividiendo = int(input("Ingrese el número que desea dividir: "))
divisor = int(input("Ingrese el número por el cual desea dividirlo: "))
counter = 0
producto = 0

while counter != divisor:
    dividiendo -= dividiendo
    counter += 1
print("El resultado de la división es:",counter,"y el resto es", dividiendo)