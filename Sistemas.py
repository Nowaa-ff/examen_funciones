from Funciones import validador
print("-- CLUB DE BASQUETBOL - PRUEBA DE REQUERIMIENTOS --")
lista = []
resultado = validador(lista)

if resultado[0] == "Falso":
    print("No cumple con la edad requerida.")
else:
    print("Cumple con la edad requerida.")

if resultado[1] == "Falso":
    print("No cumple con la altura requerida.")
else:
    print("Cumple con la altura requerida.")