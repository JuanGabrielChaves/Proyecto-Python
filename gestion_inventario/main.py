from utils import color_titulo, color_menu, color_info, color_error, color_exito
from database import crear_tabla
from crud import (
    registrar_producto,
    visualizar_productos,
    actualizar_cantidad,
    eliminar_producto,
    buscar_producto,
    reporte_bajo_stock,
)


def mostrar_menu():
    """Muestra el menú principal de la aplicación."""
    print(color_titulo("\n╔════════════════════════════════════════╗"))
    print(color_titulo("║   SISTEMA DE GESTIÓN DE INVENTARIO     ║"))
    print(color_titulo("╚════════════════════════════════════════╝\n"))

    print(color_menu("1.") + " Registrar nuevo producto")
    print(color_menu("2.") + " Visualizar todos los productos")
    print(color_menu("3.") + " Actualizar cantidad de producto")
    print(color_menu("4.") + " Eliminar producto")
    print(color_menu("5.") + " Buscar producto")
    print(color_menu("6.") + " Reporte de bajo stock")
    print(color_menu("0.") + " Salir")


def main():
    """
    Función principal que ejecuta el bucle del menú
    y gestiona las opciones del usuario.
    """
    crear_tabla()

    while True:
        mostrar_menu()
        opcion = input(color_info("\nSeleccione una opción: ")).strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            visualizar_productos()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "0":
            print(color_exito("\n¡Hasta luego! Gracias por usar el sistema.\n"))
            break
        else:
            print(color_error("\nOpción no válida. Por favor, intente de nuevo."))

        input(color_info("\nPresione Enter para continuar..."))


if __name__ == "__main__":
    main()
