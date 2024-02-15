# Description: Tarea 1


print("Selecciona la opcion de calcular area:")
print("1. Cuadraro")
print("2. Rectangulo")
print("3. Triangulo")
print("4. Circulo")
print("5. Trapecio")
print("6. Rombo")

opcion = int(input("Opcion: "))
if (opcion == 1):
    a = input("Valor (base): ")
    print("Area: ", int(a) * int(a))
elif (opcion == 2):
    a = input("Valor (base): ")
    b = input("Valor (altura): ")
    print("Area: ", int(a) * int(b))
elif (opcion == 3):
    a = input("Valor (base): ")
    b = input("Valor (altura): ")
    print("Area: ", (int(a) * int(b)) / 2)
elif (opcion == 4):
    a= input("Valor (radio): ")
    print("Area: ", 3.1416 * int(a) * int(a))
elif (opcion == 5):
    a = input("Valor (base menor): ")
    b = input("Valor (base mayor): ")
    h = input("Valor (altura): ")
    print("Area: ", ((int(a) + int(b)) / 2) * int(h))
elif (opcion == 6):
    d = input("Valor (Distancia mayor): ")
    d1 = input("Valor (Distancia menor): ")
    print("Area: ", (int(d) * int(d1)) / 2)
else:
    print("Opcion no valida")

