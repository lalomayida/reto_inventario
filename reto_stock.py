from functools import reduce

stock = [{'name': 'tor', 'quantity': 5, 'unit_price': 5.0, 'id': 1}]

def agregarArticuloStock(esReintentar):
    nombre = input("Ingrese el nombre del artículo: ")
    cantidad = int(input("Ingrese la cantidad del artículo: "))
    precio_unitario = float(input("Ingrese el precio unitario del artículo: "))

    nuevoArticulo = {'name': nombre, 'quantity': cantidad, 'unit_price': precio_unitario}
    print('')
    print(nuevoArticulo)
    esCorrecto = input('\n¿Son correctos los detalles del artículo? S/N \n')
    if esCorrecto == 'S':
        nuevoArticulo['id'] = len(stock) + 1
        stock.append(nuevoArticulo)
        print('Nuevo artículo agregado')
    else:
        if esReintentar:
            print('Por favor, inténtelo de nuevo')
        else:
            agregarArticuloStock(True)


def actualizarArticuloStock():
    ordenarArticulos('id', 2)
    imprimirStock = input('¿Desea imprimir el inventario? (S/N) \n')
    if imprimirStock == 'S':
        print(stock)

    idSeleccionado = int(input('\nPor favor, ingrese el id del artículo que desea actualizar: '))

    articulo = buscarArticuloStockPor('id', idSeleccionado)[0]
    if articulo:
        print(articulo)
        print('Seleccione el campo que desea cambiar: ')
        campoActualizar = seleccionarCriterioIndividual()
        nuevoValor = input(f'¿Cuál es el nuevo valor para {campoActualizar}? \n')
        stock[articulo['id'] - 1][campoActualizar] = nuevoValor
        print('Valor actualizado.')
        print(stock[articulo['id'] - 1])
    else:
        print('No se encontró ningún artículo con ese id \n')


def buscarArticuloStock():
    print('\n¿Por qué criterio desea buscar?\n')
    criterioBusqueda = seleccionarCriterioIndividual()
    valorBuscado = input(f'¿Cuál debería ser el valor para {criterioBusqueda}? \n')
    articulo = buscarArticuloStockPor(criterioBusqueda, valorBuscado)
    if articulo:
        print(articulo)
    else:
        print(f'No se encontró ningún artículo con {criterioBusqueda} {valorBuscado} \n')


def verificarTipos(campo, articulo, valor):
    valorActual = articulo[campo]
    if isinstance(valorActual, str):
        return valorActual == valor
    if isinstance(valorActual, int):
        return valorActual == int(valor)
    if isinstance(valorActual, float):
        return valorActual == float(valor)


def buscarArticuloStockPor(campo, valor):
    return list(filter(lambda articulo: verificarTipos(campo, articulo, valor), stock))


def ordenarStockPorNombrePrecioCantidad():
    print('\n¿Por qué criterio desea ordenar?\n')
    criterioOrden = seleccionarCriterioIndividual()
    direccion = int(input('''¿Debería ser el orden
      1. ascendente
      2. descendente? \n'''))
    ordenarArticulos(criterioOrden, direccion)
    print(stock)


def ordenarArticulos(criterioOrden, direccion):
    stock.sort(key=lambda articulo: articulo[criterioOrden], reverse=direccion == 1)


def seleccionarCriterioIndividual():
    claves = []
    contador = 1
    for clave in stock[0].keys():
        print(f"{contador}. {clave}")
        contador += 1
        claves.append(clave)
    campoSeleccionado = int(input("Ingrese su elección: "))
    return claves[campoSeleccionado - 1]


def seleccionarCriterioMultiple():
    claves = []
    contador = 1
    for clave in stock[0].keys():
        print(f"{contador}. {clave}")
        contador += 1
        claves.append(clave)
    seleccion = input("Ingrese sus elecciones separadas por coma (Todos por defecto): ")
    campos = []
    if seleccion:
        seleccion = seleccion.split(',')
        if len(seleccion) > 0:
            campos = list(map(lambda num: claves[int(num)-1], seleccion))
        else:
            print('La selección no es válida \n')
    else:
        campos = list(stock[0].keys())
    return campos


def filtrarCamposArticulo(camposDeseados, articulo):
    articuloFiltrado = {}
    for clave in articulo.keys():
        try:
            if camposDeseados.index(clave) >= 0:
                articuloFiltrado[clave] = articulo[clave]
        except ValueError:
            pass
    return articuloFiltrado


def generarReporteStock():
    print('\n¿Qué campos se deben incluir en el informe? \n')
    campos = seleccionarCriterioMultiple()
    if len(campos) > 0:
        articulosReportados = map(
            lambda articulo: filtrarCamposArticulo(campos, articulo), stock)
        print(list(articulosReportados))


def obtenerValorTotalStock():
    valor = 0
    for articulo in stock:
        valor = valor + (articulo['quantity'] * articulo['unit_price'])
    print(f'El valor total del inventario es: ${valor}')


def menuInventario():
    while True:
        print('')
        print('----- Bienvenido al Administrador de Inventario ------\n')
        print('1. Agregar nuevo artículo')
        print('2. Actualizar artículo')
        print('3. Buscar artículo')
        print('4. Ordenar inventario por nombre, precio o cantidad')
        print('5. Generar informe')
        print('6. Obtener valor total del inventario')
        print('7. Salir \n')

        seleccion = int(input('Por favor, ingrese su elección: '))
        if seleccion == 1:
            agregarArticuloStock(False)
        if seleccion == 2:
            actualizarArticuloStock()
        if seleccion == 3:
            buscarArticuloStock()
        if seleccion == 4:
            ordenarStockPorNombrePrecioCantidad()
        if seleccion == 5:
            generarReporteStock()
        if seleccion == 6:
            obtenerValorTotalStock()
        if seleccion == 7:
            break

    print('¡Gracias, vuelva pronto!')


menuInventario()
