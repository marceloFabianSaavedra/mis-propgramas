import json

productos = []

while True:
    opciones = input("A - Agregar\nR - Remover\nL - Listar\nS - Salir\n").strip().upper()

    match opciones:
      
        case "A":
            productoAgregar = input("\nProducto a agregar: ").strip().capitalize()
            precio = float(input("\nPrecio: "))
            categoria = input("\nCategoria: ").strip().capitalize()

            fruta = [productoAgregar,precio,categoria]
            productos.append(fruta)

        case "R":
            quitar = input("\nRemover:  ").strip().capitalize()
            for producto in productos:
                if producto[0] == quitar:
                    productos.remove(producto)
                    print(f"{producto[0]} removido con exito!!\n")
        case "L":
            for laFruta in productos:
                print(f"Producto: {laFruta[0]} | Precio: {laFruta[1]:.2f} | Categoria: {laFruta[2]}")

        case "S":
            break

    