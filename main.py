import json
import timeit

# Función para cargar datos desde un archivo JSON
def cargar_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos['numeros']

# Función Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Función Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Cargar datos desde el archivo JSON "Data.json"
datos = cargar_datos('Data.json')

# Realizar análisis de complejidad para Merge Sort
datos_merge_sort = datos.copy()

# Peor caso para Merge Sort
tiempo_merge_sort_peor = timeit.timeit(lambda: merge_sort(datos_merge_sort.copy()), number=1)
print("Análisis de complejidad para Merge Sort - Peor Caso:")
print("Tiempo de ejecución:", tiempo_merge_sort_peor)
print("Orden en el peor caso:", datos_merge_sort)

# Mejor caso para Merge Sort
datos_merge_sort_mejor = sorted(datos_merge_sort)
tiempo_merge_sort_mejor = timeit.timeit(lambda: merge_sort(datos_merge_sort_mejor.copy()), number=1)
print("\nAnálisis de complejidad para Merge Sort - Mejor Caso:")
print("Tiempo de ejecución:", tiempo_merge_sort_mejor)
print("Orden en el mejor caso:", datos_merge_sort_mejor)

# Caso promediado para Merge Sort
tiempo_merge_sort_promedio = sum(timeit.timeit(lambda: merge_sort(datos_merge_sort.copy()), number=1) for _ in range(10)) / 10
print("\nAnálisis de complejidad para Merge Sort - Caso Promediado:")
print("Tiempo de ejecución promedio:", tiempo_merge_sort_promedio)

# Realizar análisis de complejidad para Quick Sort
datos_quick_sort = datos.copy()

# Peor caso para Quick Sort
tiempo_quick_sort_peor = timeit.timeit(lambda: quick_sort(datos_quick_sort.copy()), number=1)
print("\nAnálisis de complejidad para Quick Sort - Peor Caso:")
print("Tiempo de ejecución:", tiempo_quick_sort_peor)
print("Orden en el peor caso:", datos_quick_sort)

# Mejor caso para Quick Sort
datos_quick_sort_mejor = sorted(datos_quick_sort)
tiempo_quick_sort_mejor = timeit.timeit(lambda: quick_sort(datos_quick_sort_mejor.copy()), number=1)
print("\nAnálisis de complejidad para Quick Sort - Mejor Caso:")
print("Tiempo de ejecución:", tiempo_quick_sort_mejor)
print("Orden en el mejor caso:", datos_quick_sort_mejor)

# Caso promediado para Quick Sort
tiempo_quick_sort_promedio = sum(timeit.timeit(lambda: quick_sort(datos_quick_sort.copy()), number=1) for _ in range(10)) / 10
print("\nAnálisis de complejidad para Quick Sort - Caso Promediado:")
print("Tiempo de ejecución promedio:", tiempo_quick_sort_promedio)
