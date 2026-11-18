from parte1_vectores import (
    vender_silla,
    sillas_libres,
    contar_ocupadas,
    sillas_juntas,
    total_ventas,
    hora_pico,
    horas_sobre_promedio,
    mejor_franja,
)
from parte2_ruta import Ruta
from parte3_historial import Historial
from parte4_pilas import Pila, Taquilla, codigo_valido
from parte5_colas import Cola, FilaTaquilla, ColaCircular
from parte6_terminal import Terminal, Bus
from retos_opcionales import evaluar_posfija, ColaConPilas, rotar


def probar_parte1():
    sillas = [True] * 40
    sillas[0] = False
    sillas[1] = True
    sillas[2] = False
    sillas[3] = True
    sillas[4] = False
    sillas[5] = False

    assert sillas_juntas(sillas) == 5

    try:
        vender_silla(sillas, 2)
        assert False
    except ValueError:
        assert True

    vender_silla(sillas, 1)
    assert sillas[0] is True

    try:
        vender_silla(sillas, 45)
        assert False
    except ValueError:
        assert True

    sillas_test = [False] * 40
    sillas_test[0] = True
    sillas_test[9] = True
    assert contar_ocupadas(sillas_test) == 2
    libres = sillas_libres(sillas_test)
    assert len(libres) == 38
    assert 1 not in libres
    assert 10 not in libres

    ventas = [0] * 24
    ventas[7] = 10
    ventas[8] = 12
    ventas[16] = 8
    ventas[17] = 12
    ventas[18] = 9

    assert total_ventas(ventas) == 51
    assert hora_pico(ventas) == 8
    assert horas_sobre_promedio(ventas) == [7, 8, 16, 17, 18]
    assert mejor_franja(ventas) == 16


def probar_parte2():
    ruta = Ruta()
    ruta.agregar_final("Cali", 0)
    ruta.agregar_final("Palmira", 28)
    ruta.agregar_final("Buga", 74)

    assert ruta.distancia("Palmira", "Buga") == 46
    assert ruta.distancia("Buga", "Cali") == -1
    assert ruta.distancia("Cali", "Medellin") == -1

    ruta.insertar_despues("Palmira", "Ginebra", 52)
    assert str(ruta) == "Cali (0) -> Palmira (28) -> Ginebra (52) -> Buga (74)"
    assert ruta.tamano == 4

    eliminado = ruta.eliminar("Ginebra")
    assert eliminado is True
    assert ruta.tamano == 3
    assert str(ruta) == "Cali (0) -> Palmira (28) -> Buga (74)"

    ruta.invertir()
    assert str(ruta) == "Buga (74) -> Palmira (28) -> Cali (0)"
    assert ruta.tamano == 3


def probar_parte3():
    historial = Historial(5)
    historial.consultar("A")
    historial.consultar("B")
    historial.consultar("C")
    historial.consultar("D")

    assert historial.atras() == "C"
    assert historial.atras() == "B"
    assert historial.adelante() == "C"

    historial.consultar("E")
    historial.consultar("F")

    assert historial.listar_adelante() == ["B", "C", "D", "E", "F"]
    assert historial.listar_atras() == ["F", "E", "D", "C", "B"]
    assert historial.listar_atras() == list(reversed(historial.listar_adelante()))

    assert historial.eliminar("D") is True
    assert historial.listar_adelante() == ["B", "C", "E", "F"]
    assert historial.tamano == 4


def probar_parte4():
    pila = Pila()
    assert pila.esta_vacia() is True
    pila.apilar(10)
    pila.apilar(20)
    assert pila.tamano() == 2
    assert pila.cima() == 20
    assert pila.desapilar() == 20
    assert pila.desapilar() == 10
    assert pila.esta_vacia() is True

    taquilla = Taquilla()
    taquilla.vender(5)
    taquilla.vender(6)
    anulada = taquilla.deshacer()
    assert anulada == 6
    assert taquilla.sillas[4] is True
    assert taquilla.sillas[5] is False

    assert codigo_valido("CAL[PAL(BUG){TUL}]") is True
    assert codigo_valido("CAL[PAL(BUG]}") is False
    assert codigo_valido("((") is False
    assert codigo_valido("][") is False


def probar_parte5():
    cola = Cola()
    assert cola.esta_vacia() is True
    cola.encolar(1)
    cola.encolar(2)
    assert cola.frente() == 1
    assert cola.desencolar() == 1
    assert cola.desencolar() == 2
    assert cola.esta_vacia() is True

    fila = FilaTaquilla()
    for i in range(1, 6):
        fila.llegar(f"P{i}", "P")
    for j in range(1, 5):
        fila.llegar(f"G{j}", "G")

    orden_esperado = ["P1", "P2", "G1", "P3", "P4", "G2", "P5", "G3", "G4"]
    orden_obtenido = []
    pasajero = fila.siguiente_pasajero()
    while pasajero is not None:
        orden_obtenido.append(pasajero)
        pasajero = fila.siguiente_pasajero()
    assert orden_obtenido == orden_esperado

    circular = ColaCircular(6)
    for i in range(6):
        circular.encolar(f"Bus{i}")
    circular.desencolar()
    circular.desencolar()
    circular.encolar("Bus6")
    circular.encolar("Bus7")

    assert circular.inicio == 2
    assert circular.fin == 2
    assert circular.tamano == 6


def probar_parte6():
    eventos = [
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
    for evento in eventos:
        terminal.procesar(evento)

    assert terminal.total_vendidos == 5
    assert terminal.total_anulados == 1
    assert terminal.ventas[7] == 1
    assert terminal.ventas[8] == 2
    assert terminal.ventas[9] == 1
    assert str(terminal.ruta) == "Cali (0) -> Palmira (28) -> Ginebra (52) -> Buga (74)"
    assert terminal.historial.listar_adelante() == ["T-0001", "T-0004", "T-0005"]


def probar_retos_opcionales():
    assert evaluar_posfija("12000 3 * 5000 +") == 41000

    try:
        evaluar_posfija("12000 +")
        assert False
    except ValueError:
        assert True

    cola = ColaConPilas()
    cola.encolar(100)
    cola.encolar(200)
    assert cola.frente() == 100
    assert cola.desencolar() == 100
    assert cola.desencolar() == 200
    assert cola.esta_vacia() is True

    arreglo = [1, 2, 3, 4, 5]
    rotar(arreglo, 2)
    assert arreglo == [4, 5, 1, 2, 3]


if __name__ == "__main__":
    probar_parte1()
    probar_parte2()
    probar_parte3()
    probar_parte4()
    probar_parte5()
    probar_parte6()
    probar_retos_opcionales()
    print("Todas las pruebas pasaron exitosamente.")
