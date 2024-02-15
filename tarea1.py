#💁Autor: Dante Silva Calderon (2012019)
#📕 Materia: Ciencia de datos
#🧑‍🏫 Profesor: Coria Ramírez Aurelio Amaury

# Creo un arreglo con los nombres de cinco estudiantes
nombres = ["Dante", "Jorge", "Imanol", "Brenda", "Daniel"]
# Creo un arreglo con las notas de los cinco estudiantes
notas = [10.0, 8.0, 8.0, 8.0, 8.0]
# Creo una variable para guardar el promedio de las notas
promedio = 0

# Defino una función que calcula el promedio de un arreglo de números
def calcular_promedio(lista):
  # Creo una variable local para guardar la suma de los elementos de la lista
  suma = 0
  # Recorro todos los elementos de la lista con un ciclo
  for elemento in lista:
    # Sumo el elemento actual a la variable suma
    suma = suma + elemento
  # Divido la suma entre la cantidad de elementos de la lista y devuelvo el resultado
  return suma / len(lista)

# Llamo a la función calcular_promedio con el arreglo notas como argumento y guardo el resultado en la variable promedio
promedio = calcular_promedio(notas)

# Imprimo el promedio en la pantalla
print(f"El promedio de las notas es {promedio}")

# Defino una función que muestra los nombres y las notas de los estudiantes que tienen una nota mayor o igual al promedio
def mostrar_aprobados(nombres, notas, promedio):
  # Imprimo un mensaje indicando el criterio de aprobación
  print(f"Los estudiantes que tienen una nota mayor o igual a {promedio} son:")
  # Recorro los arreglos nombres y notas al mismo tiempo con un ciclo usando la función zip
  for nombre, nota in zip(nombres, notas):
    # Verifico si la nota es mayor o igual al promedio con un condicional
    if nota >= promedio:
      # Imprimo el nombre y la nota del estudiante
      print(f"{nombre}: {nota}")

# Llamo a la función mostrar_aprobados con los arreglos nombres y notas y la variable promedio como argumentos
mostrar_aprobados(nombres, notas, promedio)
