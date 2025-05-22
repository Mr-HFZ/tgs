from nodo import Nodo
from arbol_general import ArbolGeneral  

def main():
    # Crear el árbol con raíz 'A'
    arbol = ArbolGeneral("A")

    # Agregar hijos a la raíz
    arbol.agregar_hijo("A", "B")
    arbol.agregar_hijo("A", "C")

    # Agregar hijos a nodo 'B'
    arbol.agregar_hijo("B", "D")
    arbol.agregar_hijo("B", "E")

    # Agregar hijo a nodo 'C'
    arbol.agregar_hijo("C", "F")

    # Mostrar el árbol
    print("Árbol general:")
    arbol.mostrar_arbol()

    # Recorrido preorden
    print("\nRecorrido preorden:")
    arbol.recorrer_preorden()
    print()

    # Buscar un valor
    valor_buscar = "E"
    print(f"\n¿Está el valor '{valor_buscar}' en el árbol?:", arbol.buscar_valor(valor_buscar))

    # Eliminar un hijo
    eliminado = arbol.eliminar_hijo("B", "E")
    print(f"\n¿Se eliminó el hijo 'E' de 'B'?:", eliminado)

    # Mostrar el árbol actualizado
    print("\nÁrbol después de eliminar 'E':")
    arbol.mostrar_arbol()


if __name__ == "__main__":
    main()
