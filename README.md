# Restaurante App

## Nombre del estudiante
EUNICE BELEN MALLA CORO

---

# Descripción del sistema

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos. Su finalidad es administrar el registro y listado de productos, bebidas y clientes mediante un menú interactivo ejecutado desde la consola.

El proyecto está organizado de forma modular para facilitar el mantenimiento del código y demostrar la aplicación de los principios SOLID, especialmente Responsabilidad Única (SRP), Abierto/Cerrado (OCP) y Sustitución de Liskov (LSP).

---

# Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── bebida.py
│   ├── cliente.py
│   └── producto.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

README.md
```

---

# Responsabilidad de cada clase

## Producto

Representa un producto general del restaurante.

Contiene los siguientes atributos:

- Código
- Nombre
- Categoría
- Precio

También implementa el método:

- `mostrar_informacion()`

---

## Bebida

Es una clase que hereda de Producto.

Además de los atributos heredados, incorpora información propia como:

- Tamaño
- Tipo de envase

Sobrescribe el método `mostrar_informacion()` para mostrar la información específica de una bebida.

---

## Cliente

Representa un cliente registrado en el restaurante.

Contiene:

- Identificación
- Nombre
- Correo electrónico

Implementa el método `mostrar_informacion()`.

---

## Restaurante

Es la clase de servicio encargada de administrar el sistema.

Sus funciones principales son:

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Validar códigos repetidos.
- Validar identificaciones repetidas.
- Listar productos.
- Listar clientes.

---

## main.py

Es el punto de inicio del programa.

Se encarga de:

- Mostrar el menú.
- Solicitar datos mediante `input()`.
- Crear los objetos.
- Llamar a los métodos de la clase Restaurante.

No administra directamente las listas internas.

---

# Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, ya que una bebida representa un tipo específico de producto.

Gracias a la herencia, una bebida puede utilizar todas las características de un producto y agregar información adicional sin modificar la clase base.

Esto permite almacenar objetos Producto y Bebida dentro de la misma colección y utilizar el método `mostrar_informacion()` mediante polimorfismo.

---

# Principios SOLID aplicados

## SRP (Responsabilidad Única)

Cada clase tiene una única responsabilidad.

- Producto representa productos.
- Bebida representa bebidas.
- Cliente representa clientes.
- Restaurante administra el sistema.
- main.py controla la interacción con el usuario.

---

## OCP (Abierto/Cerrado)

El sistema puede ampliarse agregando nuevas clases derivadas de Producto sin modificar la lógica principal del servicio Restaurante.

---

## LSP (Sustitución de Liskov)

Los objetos de la clase Bebida pueden utilizarse como objetos Producto sin alterar el funcionamiento del programa.

Durante el listado de productos, el sistema ejecuta el método `mostrar_informacion()` sin necesidad de comprobar el tipo del objeto.

---

# Instrucciones de ejecución

1. Descargar o clonar el repositorio.

2. Abrir el proyecto en Visual Studio Code o cualquier IDE compatible con Python.

3. Verificar que la estructura del proyecto sea correcta.

4. Ejecutar el archivo:

```
main.py
```

5. Utilizar el menú para:

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Listar productos.
- Listar clientes.

6. Salir del sistema.

---

# Reflexión

El desarrollo de este proyecto permitió comprender la importancia de organizar el código mediante clases con responsabilidades bien definidas. La aplicación de los principios SOLID facilita la creación de programas más claros, reutilizables y fáciles de mantener. Además, el uso de la herencia y el polimorfismo permite extender las funcionalidades del sistema sin modificar el código existente, mejorando la calidad y escalabilidad del software.
