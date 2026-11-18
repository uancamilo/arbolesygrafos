class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
        self.contador = 0

    def apilar(self, valor):
        nuevo = NodoPila(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.contador = self.contador + 1

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        valor = self.tope.dato
        self.tope = self.tope.siguiente
        self.contador = self.contador - 1
        return valor

    def cima(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        return self.tope.dato

    def esta_vacia(self):
        if self.contador == 0:
            return True
        return False

    def tamano(self):
        return self.contador


class Taquilla:
    def __init__(self):
        self.sillas = [False] * 40
        self.ventas = Pila()

    def vender(self, n):
        if n < 1:
            raise ValueError("Silla fuera de rango")
        if n > 40:
            raise ValueError("Silla fuera de rango")
        if self.sillas[n - 1] == True:
            raise ValueError("Silla ya ocupada")
        self.sillas[n - 1] = True
        self.ventas.apilar(n)

    def deshacer(self):
        if self.ventas.esta_vacia():
            return None
        silla = self.ventas.desapilar()
        self.sillas[silla - 1] = False
        return silla


def codigo_valido(texto):
    pila = Pila()
    for i in range(len(texto)):
        caracter = texto[i]
        if caracter == "(" or caracter == "[" or caracter == "{":
            pila.apilar(caracter)
        elif caracter == ")" or caracter == "]" or caracter == "}":
            if pila.esta_vacia():
                return False
            apertura = pila.desapilar()
            if caracter == ")" and apertura != "(":
                return False
            if caracter == "]" and apertura != "[":
                return False
            if caracter == "}" and apertura != "{":
                return False
    if pila.esta_vacia():
        return True
    return False
