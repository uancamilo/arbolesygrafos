class NodoParada:
    def __init__(self, nombre, km):
        self.nombre = nombre
        self.km = km
        self.siguiente = None


class Ruta:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar_final(self, nombre, km):
        nuevo = NodoParada(nombre, km)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano = self.tamano + 1

    def buscar(self, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def insertar_despues(self, referencia, nombre, km):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == referencia:
                nuevo = NodoParada(nombre, km)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                self.tamano = self.tamano + 1
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, nombre):
        if self.cabeza is None:
            return False

        if self.cabeza.nombre == nombre:
            self.cabeza = self.cabeza.siguiente
            self.tamano = self.tamano - 1
            return True

        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.nombre == nombre:
                anterior.siguiente = actual.siguiente
                self.tamano = self.tamano - 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def __str__(self):
        texto = ""
        actual = self.cabeza
        while actual is not None:
            dato_parada = actual.nombre + " (" + str(actual.km) + ")"
            if texto == "":
                texto = dato_parada
            else:
                texto = texto + " -> " + dato_parada
            actual = actual.siguiente
        return texto

    def distancia(self, origen, destino):
        actual = self.cabeza
        km_inicio = -1
        while actual is not None:
            if km_inicio == -1:
                if actual.nombre == destino and actual.nombre != origen:
                    return -1
                if actual.nombre == origen:
                    km_inicio = actual.km
                    if origen == destino:
                        return 0
            else:
                if actual.nombre == destino:
                    return actual.km - km_inicio
            actual = actual.siguiente
        return -1

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
