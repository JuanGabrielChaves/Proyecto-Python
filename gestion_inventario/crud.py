import sqlite3
from database import conectar_db
from utils import color_exito, color_error, color_info, color_titulo, color_menu

# ============================================================================
# FUNCIONES CRUD (Crear, Leer, Actualizar, Eliminar)
# ============================================================================


def registrar_producto():
    """Registra un nuevo producto en el inventario."""
    print(color_titulo("\n═══ REGISTRO DE NUEVO PRODUCTO ═══\n"))

    # 1. Solicitar y validar datos
    nombre = input(color_info("Nombre del producto: ")).strip()
    if not nombre:
        print(color_error("Error: El nombre no puede estar vacío."))
        return

    descripcion = input(color_info("Descripción: ")).strip()

    try:
        cantidad = int(input(color_info("Cantidad disponible: ")))
        if cantidad < 0:
            print(color_error("Error: La cantidad no puede ser negativa."))
            return
    except ValueError:
        print(color_error("Error: La cantidad debe ser un número entero."))
        return

    try:
        precio = float(input(color_info("Precio: ")))
        if precio < 0:
            print(color_error("Error: El precio no puede ser negativo."))
            return
    except ValueError:
        print(color_error("Error: El precio debe ser un número válido."))
        return

    categoria = input(color_info("Categoría: ")).strip()

    # 2. Insertar en DB
    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                VALUES (?, ?, ?, ?, ?)
            """,
                (nombre, descripcion, cantidad, precio, categoria),
            )
            conexion.commit()
            print(color_exito(f"\n✓ Producto '{nombre}' registrado exitosamente."))
    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al registrar: {e}"))


def visualizar_productos():
    """Muestra todos los productos registrados en el inventario en formato de tabla."""
    print(color_titulo("\n═══ LISTADO DE PRODUCTOS ═══\n"))

    productos = []
    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos ORDER BY id")
            productos = cursor.fetchall()
    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al visualizar: {e}"))
        return

    if not productos:
        print(color_info("No hay productos registrados en el inventario."))
        return

    # Mostrar encabezado de la tabla
    print(
        color_menu(
            f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cantidad':<10} {'Precio':<12} {'Categoría':<15}"
        )
    )
    print(color_menu("─" * 90))

    # Mostrar cada producto
    for producto in productos:
        id_prod, nombre, descripcion, cantidad, precio, categoria = producto
        # Lógica de truncamiento
        descripcion = (
            descripcion[:22] + "..."
            if len(descripcion or "") > 25
            else (descripcion or "")
        )
        nombre = nombre[:17] + "..." if len(nombre) > 20 else nombre
        categoria = (
            (categoria or "")[:12] + "..."
            if len(categoria or "") > 15
            else (categoria or "")
        )

        print(
            f"{id_prod:<5} {nombre:<20} {descripcion:<25} {cantidad:<10} ${precio:<11.2f} {categoria:<15}"
        )

    print(color_info(f"\nTotal de productos: {len(productos)}"))


def actualizar_cantidad():
    """Actualiza la cantidad disponible de un producto específico utilizando su ID."""
    print(color_titulo("\n═══ ACTUALIZAR CANTIDAD DE PRODUCTO ═══\n"))

    try:
        id_producto = int(input(color_info("ID del producto a actualizar: ")))
    except ValueError:
        print(color_error("Error: El ID debe ser un número entero."))
        return

    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()

            # Verificar si el producto existe
            cursor.execute(
                "SELECT nombre, cantidad FROM productos WHERE id = ?", (id_producto,)
            )
            producto = cursor.fetchone()

            if not producto:
                print(
                    color_error(
                        f"Error: No se encontró un producto con ID {id_producto}."
                    )
                )
                return

            nombre_actual, cantidad_actual = producto
            print(
                color_info(
                    f"Producto: {nombre_actual} | Cantidad actual: {cantidad_actual}"
                )
            )

            # Solicitar nueva cantidad
            try:
                nueva_cantidad = int(input(color_info("Nueva cantidad: ")))
                if nueva_cantidad < 0:
                    print(color_error("Error: La cantidad no puede ser negativa."))
                    return
            except ValueError:
                print(color_error("Error: La cantidad debe ser un número entero."))
                return

            # Actualizar la cantidad
            cursor.execute(
                "UPDATE productos SET cantidad = ? WHERE id = ?",
                (nueva_cantidad, id_producto),
            )
            conexion.commit()
            print(
                color_exito(
                    f"\n✓ Cantidad actualizada: {cantidad_actual} → {nueva_cantidad}"
                )
            )

    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al actualizar: {e}"))


def eliminar_producto():
    """Elimina un producto del inventario utilizando su ID."""
    print(color_titulo("\n═══ ELIMINAR PRODUCTO ═══\n"))

    try:
        id_producto = int(input(color_info("ID del producto a eliminar: ")))
    except ValueError:
        print(color_error("Error: El ID debe ser un número entero."))
        return

    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()

            # Verificar si el producto existe
            cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_producto,))
            producto = cursor.fetchone()

            if not producto:
                print(
                    color_error(
                        f"Error: No se encontró un producto con ID {id_producto}."
                    )
                )
                return

            nombre = producto[0]

            # Solicitar confirmación
            confirmacion = (
                input(color_error(f"¿Está seguro de eliminar '{nombre}'? (s/n): "))
                .strip()
                .lower()
            )

            if confirmacion == "s":
                cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
                conexion.commit()
                print(color_exito(f"\n✓ Producto '{nombre}' eliminado exitosamente."))
            else:
                print(color_info("Operación cancelada."))
    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al eliminar: {e}"))


def buscar_producto():
    """Busca productos por ID, nombre o categoría y muestra los resultados."""
    print(color_titulo("\n═══ BUSCAR PRODUCTO ═══\n"))
    print(color_menu("1.") + " Buscar por ID")
    print(color_menu("2.") + " Buscar por nombre")
    print(color_menu("3.") + " Buscar por categoría")
    print(color_menu("0.") + " Volver al menú principal")

    opcion = input(color_info("\nSeleccione una opción: ")).strip()
    productos = []

    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()

            if opcion == "1":
                # Búsqueda por ID
                try:
                    id_producto = int(input(color_info("Ingrese el ID: ")))
                    cursor.execute(
                        "SELECT * FROM productos WHERE id = ?", (id_producto,)
                    )
                    productos = cursor.fetchall()
                except ValueError:
                    print(color_error("Error: El ID debe ser un número entero."))
                    return

            elif opcion == "2":
                # Búsqueda por nombre (parcial, insensible a mayúsculas)
                nombre = input(color_info("Ingrese el nombre a buscar: ")).strip()
                cursor.execute(
                    "SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",)
                )
                productos = cursor.fetchall()

            elif opcion == "3":
                # Búsqueda por categoría (parcial, insensible a mayúsculas)
                categoria = input(color_info("Ingrese la categoría a buscar: ")).strip()
                cursor.execute(
                    "SELECT * FROM productos WHERE categoria LIKE ?",
                    (f"%{categoria}%",),
                )
                productos = cursor.fetchall()

            elif opcion == "0":
                return
            else:
                print(color_error("Opción no válida."))
                return

    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al buscar: {e}"))
        return

    # Mostrar resultados (Lógica de impresión de tabla)
    if productos:
        print(color_titulo("\n═══ RESULTADOS DE BÚSQUEDA ═══\n"))
        print(
            color_menu(
                f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cantidad':<10} {'Precio':<12} {'Categoría':<15}"
            )
        )
        print(color_menu("─" * 90))

        for producto in productos:
            id_prod, nombre, descripcion, cantidad, precio, categoria = producto
            descripcion = (
                descripcion[:22] + "..."
                if len(descripcion or "") > 25
                else (descripcion or "")
            )
            nombre = nombre[:17] + "..." if len(nombre) > 20 else nombre
            categoria = (
                (categoria or "")[:12] + "..."
                if len(categoria or "") > 15
                else (categoria or "")
            )

            print(
                f"{id_prod:<5} {nombre:<20} {descripcion:<25} {cantidad:<10} ${precio:<11.2f} {categoria:<15}"
            )

        print(color_info(f"\nProductos encontrados: {len(productos)}"))
    else:
        print(
            color_info("\nNo se encontraron productos con los criterios especificados.")
        )


def reporte_bajo_stock():
    """Genera un reporte de productos con stock igual o inferior a un límite especificado."""
    print(color_titulo("\n═══ REPORTE DE BAJO STOCK ═══\n"))

    try:
        limite = int(input(color_info("Ingrese el límite de stock: ")))
        if limite < 0:
            print(color_error("Error: El límite no puede ser negativo."))
            return
    except ValueError:
        print(color_error("Error: El límite debe ser un número entero."))
        return

    productos = []
    try:
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC",
                (limite,),
            )
            productos = cursor.fetchall()
    except sqlite3.Error as e:
        print(color_error(f"Error de base de datos al generar reporte: {e}"))
        return

    if productos:
        print(color_error(f"\n⚠ Productos con stock ≤ {limite}:\n"))
        print(
            color_menu(f"{'ID':<5} {'Nombre':<25} {'Cantidad':<10} {'Categoría':<15}")
        )
        print(color_menu("─" * 65))

        for producto in productos:
            id_prod, nombre, _, cantidad, _, categoria = producto
            nombre = nombre[:22] + "..." if len(nombre) > 25 else nombre
            categoria = (
                (categoria or "")[:12] + "..."
                if len(categoria or "") > 15
                else (categoria or "")
            )

            # Resaltar productos con stock crítico (0)
            if cantidad == 0:
                print(
                    color_error(
                        f"{id_prod:<5} {nombre:<25} {cantidad:<10} {categoria:<15} ← SIN STOCK"
                    )
                )
            else:
                print(f"{id_prod:<5} {nombre:<25} {cantidad:<10} {categoria:<15}")

        print(color_info(f"\nTotal de productos con bajo stock: {len(productos)}"))
    else:
        print(
            color_exito(f"\n✓ No hay productos con stock igual o inferior a {limite}.")
        )
