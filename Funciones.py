def validador(lista):
    apellido = input("Ingrese su apellido: ")
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    altura = int(input("Ingrese su altura (en centímetros): "))
    if año_nacimiento <= 2010:
        lista.append("Verdadero")
    else:
        lista.append("Falso")

    if altura >= 180:
        lista.append("Verdadero")
    else:
        lista.append("Falso")

    return lista