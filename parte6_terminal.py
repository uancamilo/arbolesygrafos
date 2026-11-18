from parte1_vectores import hora_pico
from parte2_ruta import Ruta
from parte3_historial import Historial
from parte4_pilas import Pila
from parte5_colas import FilaTaquilla, ColaCircular


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.sillas = [False] * 40

    def primera_silla_libre(self):
        for i in range(len(self.sillas)):
            if self.sillas[i] == False:
                return i + 1
        return -1


class Terminal:
    def __init__(self):
        self.plataforma = ColaCircular(6)
        self.fila = FilaTaquilla()
        self.ventas = [0] * 24
        self.ruta = Ruta()
        self.ruta.agregar_final("Cali", 0)
        self.ruta.agregar_final("Palmira", 28)
        self.ruta.agregar_final("Buga", 74)
        self.pila_ventas = Pila()
        self.historial = Historial(5)
        self.contador_tiquetes = 0
        self.total_vendidos = 0
        self.total_anulados = 0

    def procesar(self, evento):
        tipo_evento = evento[0]

        if tipo_evento == "BUS":
            placa = evento[2]
            if self.plataforma.esta_llena():
                print("Aviso: Plataforma llena, no puede ingresar el bus", placa)
            else:
                bus = Bus(placa)
                self.plataforma.encolar(bus)

        elif tipo_evento == "LLEGA":
            nombre = evento[2]
            tipo_pasajero = evento[3]
            self.fila.llegar(nombre, tipo_pasajero)

        elif tipo_evento == "ATIENDE":
            hora_str = evento[1]
            if self.plataforma.esta_vacia():
                print("Aviso: No hay buses en plataforma para atender")
                return

            bus_actual = self.plataforma.frente()
            silla = bus_actual.primera_silla_libre()
            if silla == -1:
                print("Aviso: El bus al frente esta lleno")
                return

            pasajero = self.fila.siguiente_pasajero()
            if pasajero is None:
                print("Aviso: Fila vacia, no hay pasajeros por atender")
                return

            bus_actual.sillas[silla - 1] = True
            self.contador_tiquetes = self.contador_tiquetes + 1
            num_str = str(self.contador_tiquetes)
            while len(num_str) < 4:
                num_str = "0" + num_str
            codigo_tiquete = "T-" + num_str

            partes = hora_str.split(":")
            hora = int(partes[0])
            self.ventas[hora] = self.ventas[hora] + 1
            self.total_vendidos = self.total_vendidos + 1
            self.pila_ventas.apilar((bus_actual, silla, hora, codigo_tiquete))

        elif tipo_evento == "ANULA":
            if self.pila_ventas.esta_vacia():
                print("Aviso: No hay ventas para anular")
            else:
                venta = self.pila_ventas.desapilar()
                bus = venta[0]
                silla = venta[1]
                hora = venta[2]
                bus.sillas[silla - 1] = False
                self.ventas[hora] = self.ventas[hora] - 1
                self.total_anulados = self.total_anulados + 1

        elif tipo_evento == "PARADA":
            nombre = evento[1]
            km = evento[2]
            referencia = evento[3]
            self.ruta.insertar_despues(referencia, nombre, km)

        elif tipo_evento == "CONSULTA":
            codigo = evento[1]
            self.historial.consultar(codigo)

        elif tipo_evento == "DESPACHA":
            if self.plataforma.esta_vacia():
                print("Aviso: No hay buses en plataforma para despachar")
            else:
                self.plataforma.desencolar()

    def reporte(self):
        print("Tiquetes vendidos:", self.total_vendidos)
        print("Tiquetes anulados:", self.total_anulados)
        pico = hora_pico(self.ventas)
        if pico < 10:
            hora_str = "0" + str(pico) + ":00"
        else:
            hora_str = str(pico) + ":00"
        print("Hora pico del dia:", hora_str)
        print("Ruta final:", str(self.ruta))

        sin_atender = []
        p = self.fila.siguiente_pasajero()
        while p is not None:
            sin_atender.append(p)
            p = self.fila.siguiente_pasajero()
        print("Pasajeros sin atender:", sin_atender)

        consultas = self.historial.listar_adelante()
        print("Historial de consultas:", consultas)


if __name__ == "__main__":
    EVENTOS = [
        ("BUS", "06:30", "B-101"),
        ("BUS", "06:40", "B-102"),
        ("LLEGA", "07:00", "Ana", "P"),
        ("LLEGA", "07:01", "Luis", "G"),
        ("LLEGA", "07:02", "Marta", "P"),
        ("LLEGA", "07:03", "Pedro", "P"),
        ("ATIENDE", "07:05"),
        ("ATIENDE", "07:06"),
        ("ANULA", "07:07"),
        ("CONSULTA", "T-0001"),
        ("PARADA", "Ginebra", 52, "Palmira"),
        ("ATIENDE", "08:10"),
        ("ATIENDE", "08:12"),
        ("ATIENDE", "08:15"),
        ("DESPACHA", "09:00"),
        ("LLEGA", "09:10", "Sofía", "G"),
        ("LLEGA", "09:11", "Jorge", "G"),
        ("ATIENDE", "09:15"),
        ("CONSULTA", "T-0004"),
        ("CONSULTA", "T-0005"),
    ]

    terminal = Terminal()
    for evento in EVENTOS:
        terminal.procesar(evento)
    terminal.reporte()
