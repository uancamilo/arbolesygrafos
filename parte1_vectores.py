def vender_silla(sillas, n):
    if n < 1:
        raise ValueError("Silla fuera de rango")
    if n > len(sillas):
        raise ValueError("Silla fuera de rango")
    posicion = n - 1
    if sillas[posicion] == True:
        raise ValueError("La silla ya esta ocupada")
    sillas[posicion] = True


def sillas_libres(sillas):
    resultado = []
    for i in range(len(sillas)):
        if sillas[i] == False:
            resultado.append(i + 1)
    return resultado


def contar_ocupadas(sillas):
    conteo = 0
    for i in range(len(sillas)):
        if sillas[i] == True:
            conteo = conteo + 1
    return conteo


def sillas_juntas(sillas):
    for i in range(len(sillas) - 1):
        if sillas[i] == False and sillas[i + 1] == False:
            return i + 1
    return -1


def total_ventas(ventas):
    suma = 0
    for i in range(len(ventas)):
        suma = suma + ventas[i]
    return suma


def hora_pico(ventas):
    mayor = ventas[0]
    hora = 0
    for i in range(len(ventas)):
        if ventas[i] > mayor:
            mayor = ventas[i]
            hora = i
    return hora


def horas_sobre_promedio(ventas):
    total = total_ventas(ventas)
    promedio = total / 24
    lista = []
    for i in range(len(ventas)):
        if ventas[i] > promedio:
            lista.append(i)
    return lista


def mejor_franja(ventas):
    mayor_suma = 0
    hora_inicio = 0
    for i in range(len(ventas) - 2):
        suma_tres = ventas[i] + ventas[i + 1] + ventas[i + 2]
        if suma_tres > mayor_suma:
            mayor_suma = suma_tres
            hora_inicio = i
    return hora_inicio
