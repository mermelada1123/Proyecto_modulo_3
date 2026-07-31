# Sistema de Gestión de Inventario de Herramientas

## Descripción

Este proyecto fue desarrollado como trabajo final del Módulo 3 del Bootcamp de Python Full Stack Trainee SENCE.

El sistema permite administrar el inventario de herramientas mediante un menú interactivo en consola. Implementa el método FIFO (First In, First Out) para el control de existencias y registra el historial de compras realizadas.
## Gestión de inventario

Cada compra genera un nuevo lote que almacena la cantidad y el costo de adquisición. Al registrar una venta, el sistema recorre los lotes en orden de ingreso y descuenta las unidades comenzando por el lote más antiguo, siguiendo la metodología **FIFO (First In, First Out)**.

### Ejemplo

Compras registradas:

| Lote | Cantidad |
|------|---------:|
| 1 | 5 |
| 2 | 3 |

Si se realiza una venta de **6 unidades**, el sistema:

- Descarga las 5 unidades del lote 1.
- Descarga 1 unidad del lote 2.

Resultado:

| Lote | Cantidad restante |
|------|------------------:|
| 1 | 0 |
| 2 | 2 |
## Funcionalidades

- Inicio de sesión de usuario.
- Registro de compras.
- Registro de ventas.
- Control de stock.
- Gestión de lotes.
- Descuento automático utilizando el método FIFO.
- Historial de compras.
- Visualización del inventario.

## Autora

Fernanda Campos Araneda

Proyecto realizado para el Bootcamp Python FullStack Trainee SENCE.
