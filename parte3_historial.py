class NodoConsulta:
    def __init__(self, codigo):
        self.codigo = codigo
        self.anterior = None
        self.siguiente = None


class Historial:
    def __init__(self, capacidad=5):
        self.cabeza = None
        self.cola = None
        self.actual = None
        self.tamano = 0
        self.capacidad = capacidad

    def consultar(self, codigo):
        nuevo = NodoConsulta(codigo)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
            self.actual = nuevo
        self.tamano = self.tamano + 1

        if self.tamano > self.capacidad:
            if self.actual == self.cabeza:
                self.actual = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamano = self.tamano - 1

    def atras(self):
        if self.actual is None:
            return None
        if self.actual.anterior is None:
            return None
        self.actual = self.actual.anterior
        return self.actual.codigo

    def adelante(self):
        if self.actual is None:
            return None
        if self.actual.siguiente is None:
            return None
        self.actual = self.actual.siguiente
        return self.actual.codigo

    def listar_adelante(self):
        lista = []
        actual = self.cabeza
        while actual is not None:
            lista.append(actual.codigo)
            actual = actual.siguiente
        return lista

    def listar_atras(self):
        lista = []
        actual = self.cola
        while actual is not None:
            lista.append(actual.codigo)
            actual = actual.anterior
        return lista

    def eliminar(self, codigo):
        actual = self.cabeza
        while actual is not None:
            if actual.codigo == codigo:
                if actual == self.actual:
                    if actual.anterior is not None:
                        self.actual = actual.anterior
                    elif actual.siguiente is not None:
                        self.actual = actual.siguiente
                    else:
                        self.actual = None

                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                self.tamano = self.tamano - 1
                return True
            actual = actual.siguiente
        return False
