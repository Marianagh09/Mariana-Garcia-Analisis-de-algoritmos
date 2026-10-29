"""Lista enlazada y tabla hash para consultar guias de envio."""
class Nodo:
    def __init__(self, guia: int, estado: str) -> None:
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None
class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Nodo | None = None
        self.tamano = 0
    def insertar(self, guia: int, estado: str) -> None:
        # TODO: cree el nodo, enlacelo con la cabeza actual y actualice
        pass
    def buscar(self, guia: int) -> str | None:
        # TODO: recorra desde la cabeza con un ciclo while (iterativo)
        pass
class TablaHash:
    def __init__(self, m: int) -> None:
        self.m = m
        self.casillas: list[ListaEnlazada] = [ListaEnlazada() for _ in range(m)]
        self.tamano = 0
    def hash(self, guia: int) -> int:
        # TODO: h(k) = k mod m
        pass
    def insertar(self, guia: int, estado: str) -> None:
        # TODO: calcule la casilla y delegue en la lista de esa casilla
        pass
    def buscar(self, guia: int) -> str | None:
        # TODO: calcule la casilla y busque solo en su lista
        pass
    def factor_carga(self) -> float:
        # TODO: devuelva n / m
        pass