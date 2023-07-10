# Tercera-pre-entrega-Coronel

Para ver esta entrega dirigirse a la rama "master".
Se realizaron 4 clases: Clientes, Vendedores, Productos, RecursosHumanos siguiendo la idea de entregas anteriores.
Se trabajo en una web para una pequeña empresa (pyme) dedicada a la venta de materiales de construcción.
Se agregaron (con los minimos minimos conocimientos de html y mucho google, algunas imagenes para darle personalidad a la pagina).

Las URL disponibles son las siguientes:

    path('inicio/', inicio),
    path('Clientes/', clientes, name="Cursos"),
    path('Vendedores/', vendedores, name="Vendedores"),
    path('Productos/', productos, name="Productos"),
    path('Empty/', Empty, name="Empty"),
    path('RecursosHumanos/', recursosHumanos, name="RecursosHumanos"),
    path('RegistrarCliente/', RegistrarCliente, name="RegistrarCliente"),
    path('RegistrarVendedor/', RegistrarVendedor, name="RegistrarVendedor"),
    path('BuscarVendedor/', BuscarVendedor, name="BuscarVendedor"),
    path('aux_BuscarVendedor/', aux_BuscarVendedor, name="aux_BuscarVendedor"),
    path('RegistrarProducto/', RegistrarProducto, name="RegistrarProducto"),
    path('BuscarProducto/', BuscarProducto, name="BuscarProducto"),
    path('aux_BuscarProducto/', aux_BuscarProducto, name="aux_BuscarProducto"),
    path('RegistrarCandidato/', RegistrarCandidato, name="RegistrarCandidato"),

Se recomienda empezar probando el inicio, Clientes, Vendedores, Productos y RecursosHUmanos que son las planillas meramente esteticas.
Luego probar las dedicadas al registro y finalmente a las de busqueda.

Se han dejado pre-cargados los siguientes objetos si se quisiera probar la busqueda sin cargar nada nuevo:
Productos = arena, Cal.
Vendedores = NombrePrueba, ApellidoPrueba, Chaco,123456,prueba@prueba.com,10
Vendedores = Martin, Ramirez, Buenos Aires, 456789, martira@gmail.com,10


Si quisieran ver algo desde el admin deje creado un superusuario para los tutores del curso que se los dejo en la entrega en CODER.
