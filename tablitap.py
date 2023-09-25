# Función para ingresar los datos de un elemento químico
def ingresar_elemento():
    nombre = input("Ingrese el nombre del elemento: ")
    simbolo = input("Ingrese el símbolo químico: ")
    numero_atomico = int(input("Ingrese el número atómico: "))
    masa_atomica = float(input("Ingrese la masa atómica: "))
    return {"nombre": nombre, "simbolo": simbolo, "numero_atomico": numero_atomico, "masa_atomica": masa_atomica}

# Inicializar listas para almacenar elementos químicos
elementos = []

# Solicitar al usuario la cantidad de elementos a ingresar
n = int(input("Ingrese la cantidad de elementos químicos a ingresar: "))

# Ingresar datos de los elementos químicos
for _ in range(n):
    elemento = ingresar_elemento()
    elementos.append(elemento)

# Encontrar el elemento con mayor y menor masa atómica
elemento_mayor_masa = max(elementos, key=lambda x: x["masa_atomica"])
elemento_menor_masa = min(elementos, key=lambda x: x["masa_atomica"])

# Encontrar el elemento con menor y mayor número atómico
elemento_menor_numero_atomico = min(elementos, key=lambda x: x["numero_atomico"])
elemento_mayor_numero_atomico = max(elementos, key=lambda x: x["numero_atomico"])

# Calcular el promedio de masa atómica
suma_masas = sum(elemento["masa_atomica"] for elemento in elementos)
promedio_masa_atomica = suma_masas / n

# Calcular el porcentaje de elementos con masa atómica entre 88.9 y 200.59
elementos_dentro_del_rango = [elemento for elemento in elementos if 88.9 <= elemento["masa_atomica"] <= 200.59]
porcentaje_en_rango = (len(elementos_dentro_del_rango) / n) * 100

# Mostrar resultados
print("\nResultados esperados:")
print("Elemento con mayor masa atómica:", elemento_mayor_masa["nombre"], "-", elemento_mayor_masa["simbolo"])
print("Elemento con menor masa atómica:", elemento_menor_masa["nombre"], "-", elemento_menor_masa["simbolo"])
print("Elemento con menor número atómico:", elemento_menor_numero_atomico["nombre"], "-", elemento_menor_numero_atomico["simbolo"])
print("Elemento con mayor número atómico:", elemento_mayor_numero_atomico["nombre"], "-", elemento_mayor_numero_atomico["simbolo"])
print("Promedio de masa atómica:", promedio_masa_atomica)
print("Porcentaje de elementos con masa atómica entre 88.9 y 200.59:", porcentaje_en_rango, "%")
