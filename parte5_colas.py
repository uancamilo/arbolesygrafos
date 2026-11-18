class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente_nodo = None
        self.final_nodo = None
        self.contador = 0

    def encolar(self, valor):
        nuevo = NodoCola(valor)
        if self.esta_vacia():
            self.frente_nodo = nuevo
            self.final_nodo = nuevo
        else:
            self.final_nodo.siguiente = nuevo
            self.final_nodo = nuevo
        self.contador = self.contador + 1

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Cola vacia")
        valor = self.frente_nodo.dato
        self.frente_nodo = self.frente_nodo.siguiente
        if self.frente_nodo is None:
            self.final_nodo = None
        self.contador = self.contador - 1
        return valor

    def frente(self):
        if self.esta_vacia():
            raise IndexError("Cola vacia")
        return self.frente_nodo.dato

    def esta_vacia(self):
        if self.contador == 0:
            return True
        return False

    def tamano(self):
        return self.contador


class FilaTaquilla:
    def __init__(self):
        self.preferencial = Cola()
        self.general = Cola()
        self.conteo_preferencial = 0

    def llegar(self, nombre, tipo):
        if tipo == "P":
            self.preferencial.encolar(nombre)
        else:
            self.general.encolar(nombre)

    def siguiente_pasajero(self):
        if self.preferencial.esta_vacia() and self.general.esta_vacia():
            return None

        if self.preferencial.esta_vacia():
            self.conteo_preferencial = 0
            return self.general.desencolar()

        if self.general.esta_vacia():
            self.conteo_preferencial = 0
            return self.preferencial.desencolar()

        if self.conteo_preferencial < 2:
            self.conteo_preferencial = self.conteo_preferencial + 1
            return self.preferencial.desencolar()
        else:
            self.conteo_preferencial = 0
            return self.general.desencolar()


class ColaCircular:
    def __init__(self, capacidad=6):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.inicio = 0
        self.fin = 0
        self.tamano = 0

    def encolar(self, valor):
        if self.tamano == self.capacidad:
            raise OverflowError("Cola circular llena")
        self.datos[self.fin] = valor
        self.fin = (self.fin + 1) % self.capacidad
        self.tamano = self.tamano + 1

    def desencolar(self):
        if self.tamano == 0:
            raise IndexError("Cola circular vacia")
        valor = self.datos[self.inicio]
        self.datos[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidad
        self.tamano = self.tamano - 1
        return valor

    def frente(self):
        if self.tamano == 0:
            raise IndexError("Cola circular vacia")
        return self.datos[self.inicio]

    def esta_vacia(self):
        if self.tamano == 0:
            return True
        return False

    def esta_llena(self):
        if self.tamano == self.capacidad:
            return True
        return False
