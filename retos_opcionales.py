from parte4_pilas import Pila


def evaluar_posfija(expresion):
    tokens = expresion.split()
    if len(tokens) == 0:
        raise ValueError("Expresion vacia")

    pila = Pila()
    for i in range(len(tokens)):
        token = tokens[i]
        if token == "+" or token == "-" or token == "*" or token == "/":
            if pila.tamano() < 2:
                raise ValueError("Expresion mal formada")
            b = pila.desapilar()
            a = pila.desapilar()
            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                resultado = a // b
            pila.apilar(resultado)
        else:
            try:
                numero = int(token)
                pila.apilar(numero)
            except ValueError:
                raise ValueError("Token no valido")

    if pila.tamano() != 1:
        raise ValueError("Expresion mal formada")

    return pila.desapilar()


class ColaConPilas:
    def __init__(self):
        self.pila_entrada = Pila()
        self.pila_salida = Pila()

    def encolar(self, valor):
        self.pila_entrada.apilar(valor)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Cola vacia")
        if self.pila_salida.esta_vacia():
            while not self.pila_entrada.esta_vacia():
                elemento = self.pila_entrada.desapilar()
                self.pila_salida.apilar(elemento)
        return self.pila_salida.desapilar()

    def frente(self):
        if self.esta_vacia():
            raise IndexError("Cola vacia")
        if self.pila_salida.esta_vacia():
            while not self.pila_entrada.esta_vacia():
                elemento = self.pila_entrada.desapilar()
                self.pila_salida.apilar(elemento)
        return self.pila_salida.cima()

    def esta_vacia(self):
        if self.pila_entrada.esta_vacia() and self.pila_salida.esta_vacia():
            return True
        return False

    def tamano(self):
        return self.pila_entrada.tamano() + self.pila_salida.tamano()


def rotar(ventas, k):
    n = len(ventas)
    if n <= 1:
        return
    k = k % n
    for vez in range(k):
        ultimo = ventas[n - 1]
        for i in range(n - 1, 0, -1):
            ventas[i] = ventas[i - 1]
        ventas[0] = ultimo
