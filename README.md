# Taller Integrador: Estructuras Lineales
**Estructura de Datos (ESTDA11) - Terminal de Transportes del Valle**

Este proyecto es la solucion al taller integrador del curso. Implementamos desde cero las estructuras de datos lineales vistas en clase (vectores, listas simplemente enlazadas, listas doblemente enlazadas, pilas y colas) usando nodos propios y sin librerias externas, simulando el funcionamiento diario de una terminal de transportes.

---

## 1. Archivos del proyecto

- `parte1_vectores.py`: Manejo del vector de 40 sillas del bus y las estadisticas de ventas por hora.
- `parte2_ruta.py`: Lista simplemente enlazada para las paradas del bus (agregar, buscar, insertar despues, eliminar e invertir).
- `parte3_historial.py`: Lista doblemente enlazada con capacidad maxima de 5 para guardar y navegar el historial de consultas del taquillero.
- `parte4_pilas.py`: Pila con nodos para deshacer la ultima venta de tiquetes y validar los parentesis y corchetes de los codigos de ruta.
- `parte5_colas.py`: Fila de taquilla con prioridad 2 a 1 y la plataforma de 6 bahias usando una cola circular con arreglos.
- `parte6_terminal.py`: Modulo principal que junta todas las estructuras anteriores, procesa la lista de eventos del dia e imprime el reporte final.
- `retos_opcionales.py`: Ejercicios opcionales de la entrega (calculadora posfija con pila, cola hecha con dos pilas y rotacion de vector en el mismo arreglo).
- `pruebas.py`: Archivo de pruebas con assert para revisar que todo funcione bien y cumpla las condiciones del taller.

---

## 2. Como ejecutar el codigo

Para correr todas las pruebas y verificar que pasen los casos de prueba:
```bash
python3 pruebas.py
```

Para correr la simulacion completa de los eventos de la terminal y ver el reporte por consola:
```bash
python3 parte6_terminal.py
```

---

## 3. Tabla de Complejidad Big-O

| Archivo / Estructura | Funcion o Metodo | Complejidad | Por que |
|---|---|:---:|---|
| **Parte 1 (Vectores)** | `vender_silla` | O(1) | Accedemos directo a la posicion del arreglo con `sillas[posicion]`. |
| | `sillas_libres` | O(n) | Recorremos las 40 casillas del arreglo con un ciclo for. |
| | `contar_ocupadas` | O(n) | Hacemos un ciclo para contar cuantas casillas estan en True. |
| | `sillas_juntas` | O(n) | Revisamos posicion por posicion hasta encontrar dos sillas libres seguidas. |
| | `total_ventas` | O(h) | Sumamos las ventas de las 24 horas del dia con un ciclo. |
| | `hora_pico` | O(h) | Recorremos las 24 posiciones buscando cual numero es el mayor. |
| | `horas_sobre_promedio` | O(h) | Calculamos el promedio y luego revisamos cuales horas lo superan. |
| | `mejor_franja` | O(h) | Comparamos sumas de 3 horas consecutivas recorriendo el arreglo. |
| **Parte 2 (Lista Simple)** | `agregar_final` | O(n) | Hay que empezar en `self.cabeza` y avanzar hasta llegar al ultimo nodo. |
| | `buscar` | O(n) | Recorremos la lista nodo por nodo hasta encontrar el nombre. |
| | `insertar_despues` | O(n) | Primero buscamos la parada (O(n)) y luego cambiamos los enlaces (O(1)). |
| | `eliminar` | O(n) | Buscamos la parada guardando el nodo anterior para poder desconectarla. |
| | `distancia` | O(n) | Recorremos la lista una sola vez sumando o restando los kilometros. |
| | `invertir` | O(n) | Pasamos por cada nodo cambiando el puntero siguiente hacia atras. |
| **Parte 3 (Lista Doble)** | `consultar` | O(1) | Insertamos al final con `self.cola` y si se llena quitamos con `self.cabeza`. |
| | `atras` / `adelante` | O(1) | Nos movemos directo con `self.actual.anterior` o `self.actual.siguiente`. |
| | `listar_adelante` / `atras` | O(k) | Recorremos los nodos que tenga el historial (maximo 5). |
| | `eliminar` | O(k) | Buscamos el codigo y reconectamos anterior y siguiente. |
| **Parte 4 (Pilas)** | `apilar`, `desapilar`, `cima` | O(1) | Todas las operaciones se hacen directo sobre `self.tope`. |
| | `codigo_valido` | O(L) | Recorremos cada letra del texto metiendo y sacando simbolos de la pila. |
| **Parte 5 (Colas)** | `encolar`, `desencolar`, `frente` | O(1) | Usamos referencias directas a `frente_nodo` y `final_nodo`. |
| | `siguiente_pasajero` | O(1) | Desencolamos de preferencial o general revisando el contador de 2 a 1. |
| | `ColaCircular` (todos los metodos) | O(1) | Calculamos las posiciones directo con la formula `(indice + 1) % capacidad`. |

---

## 4. Justificacion de Diseno

### 1. Plataforma de buses (Cola Circular sobre vector vs Lista Enlazada o Vector Normal)
Para la plataforma usamos una cola circular porque en la vida real la terminal solo tiene 6 bahias fijas y los buses van saliendo en el mismo orden en que llegaron (primero en entrar, primero en salir). Con la cola circular sobre un vector de tamano 6, tanto meter un bus como despacharlo se hace en tiempo inmediato O(1) cambiando los indices `inicio` y `fin`. Si hubieramos usado una lista enlazada, estariamos creando y destruyendo nodos en memoria sin aprovechar que el tamano maximo ya se conoce de antemano. Y si hubieramos usado un vector normal sin circularidad, cada vez que despachamos el bus del frente tendriamos que mover los otros 5 buses una posicion hacia adelante, lo cual costaria mas trabajo computacional O(n).

### 2. Anulacion de ventas (Pila vs Cola o Lista)
Para anular ventas usamos una pila porque el problema pide deshacer siempre la ultima venta realizada. Una pila funciona con la logica LIFO (el ultimo en entrar es el primero en salir), asi que cuando se vende un tiquete lo apilamos en O(1) en `self.tope`, y cuando el taquillero le da anular, desapilamos esa ultima venta tambien en O(1) sin tener que buscarla. Si hubieramos usado una cola, anulariamos la primera venta de la manana en vez de la ultima. Y si usaramos una lista enlazada comun sin puntero al final, nos tocaria recorrer toda la lista desde el principio hasta el final para encontrar cual fue la ultima venta vendida O(n).

### 3. Paradas de la ruta (Lista Simple vs Vector Fijo)
Para las paradas de la ruta usamos una lista simplemente enlazada porque a lo largo del dia la empresa de transporte puede necesitar agregar una parada intermedia (como meter Ginebra entre Palmira y Buga) o quitar una parada. Con la lista enlazada solo creamos un `NodoParada` nuevo y acomodamos los punteros `siguiente` de los vecinos, sin importar cuantas paradas tengamos. Si hubieramos usado un vector de tamano fijo, al insertar una parada intermedia nos tocaria correr manualmente todas las paradas que van despues para hacer un hueco, lo cual toma tiempo O(n), y ademas tendriamos el limite de que el arreglo se nos puede llenar si la ruta tiene muchas paradas.

---

## 5. Respuestas a las Preguntas Finales

### Pregunta 1
Si las sillas del bus se guardaran en una lista enlazada en vez de un vector, la funcion `vender_silla` ya no seria instantanea O(1) sino que pasaria a ser O(n), porque para marcar la silla numero 35 tendriamos que empezar en la cabeza e ir pasando nodo por nodo hasta llegar a esa posicion, perdiendo la ventaja que nos da el vector de ir directo con `sillas[posicion]`. Por el contrario, si las paradas de la ruta fueran un vector estatico, la operacion `insertar_despues` seria mas costosa porque para meter una parada en la mitad nos tocaria desplazar todos los elementos que estan a la derecha una casilla hacia adelante para abrir el espacio O(n), y si el vector se llega a llenar ya no podriamos agregar mas paradas.

### Pregunta 2
En la lista simple de la Parte 2, para eliminar la ultima parada nos toca recorrer toda la lista desde `self.cabeza` hasta llegar al penultimo nodo para poder cambiar su `siguiente` a `None` (costo O(n)), porque los nodos solo apuntan hacia adelante. En cambio, en la lista doble de la Parte 3, cada `NodoConsulta` tiene la referencia `anterior`; gracias a esto, teniendo el puntero `self.cola` podemos mirar directamente hacia atras con `self.cola.anterior` y desconectar el ultimo nodo en tiempo O(1) sin recorrer nada. Lo que se gana es rapidez y poder movernos en ambos sentidos (`atras()` y `adelante()`), pero lo que se paga es que el programa gasta mas memoria porque cada nodo tiene que guardar dos punteros en vez de uno, y ademas en el codigo hay que tener mas cuidado de actualizar bien tanto el `siguiente` como el `anterior`.

### Pregunta 3
Si la terminal necesitara anular cualquier tiquete buscando por su codigo (por ejemplo anular `T-0002` cuando ya vamos en el `T-0005`), la pila ya no nos serviria porque la pila solo nos deja ver y sacar el elemento que esta arriba en el tope (`self.tope`). Para sacar un tiquete de la mitad tendriamos que desapilar los otros tiquetes validos o romper la estructura. En su lugar, lo mas adecuado seria usar una lista enlazada (simple o doble) donde guardemos las ventas; de esa manera, para anular un tiquete cualquiera simplemente recorremos la lista buscando el codigo que coincida y reconectamos los punteros de los nodos vecinos para eliminarlo, lo cual tendria una complejidad de O(n) por la busqueda.

### Pregunta 4
Si en la taquilla siempre se le diera paso primero a los pasajeros preferenciales sin ninguna regla, en una hora pico donde no paren de llegar adultos mayores o personas con discapacidad los pasajeros de la fila general se quedarian esperando indefinidamente sin ser atendidos nunca (lo que en programacion se conoce como inanicion o bloqueo). La regla de 2 a 1 soluciona esto porque pone un limite: nuestro codigo cuenta con `conteo_preferencial` y cuando ya ha atendido a 2 preferenciales seguidos, obliga al sistema a atender a 1 pasajero de la fila general, garantizando que la fila general siempre avance y nadie se quede atrapado.

### Pregunta 5
Si la plataforma fuera un vector normal y al salir un bus corrieramos todos los buses hacia adelante, la operacion de desencolar costaria O(n) porque tendriamos que hacer un ciclo que copie cada bus a la casilla de la izquierda para llenar el vacio que dejo el bus despachado. Por otro lado, no basta con comparar si `inicio == fin` para saber si la cola esta llena o vacia porque esa condicion se cumple en los dos extremos: cuando recien creamos la cola y no hay ningun bus metido `inicio` y `fin` valen lo mismo (0), y cuando completamos los 6 buses la vuelta circular hace que `fin` vuelva a alcanzar a `inicio`. Por eso en la clase `ColaCircular` usamos la variable `self.tamano`, para saber con seguridad si esta vacia (`tamano == 0`) o si esta llena (`tamano == capacidad`).
