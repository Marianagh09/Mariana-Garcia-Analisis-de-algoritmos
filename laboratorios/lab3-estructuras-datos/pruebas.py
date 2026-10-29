from estructuras import ListaEnlazada, TablaHash
 
tabla = TablaHash(7)
for guia in (10, 24, 17):
    tabla.insertar(guia, "en bodega")
 
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(99) is None
assert tabla.factor_carga() == 3 / 7