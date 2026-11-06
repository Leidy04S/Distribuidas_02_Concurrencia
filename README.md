# Ejercicio 2: Ejecución con Concurrencia (Atención de Pedidos)

## ¿De qué trata este ejercicio?
Este programa demuestra el concepto de **ejecución concurrente** mediante la simulación de la atención simultánea a tres clientes en una cafetería.

En la ejecución concurrente, **múltiples tareas pueden avanzar en paralelo durante los tiempos de espera**. El sistema no se queda bloqueado esperando a que finalice un pedido para empezar a preparar el siguiente. 

A diferencia del enfoque secuencial (donde tomaría 7 segundos sumar 2s + 3s + 2s), este programa completa todas las órdenes en aproximadamente **3 segundos** (el tiempo que tarda la orden más larga).

---

## Estructura de archivos

```text
Distribuidas_02_Concurrencia/
├── 02_concurrencia.py   # Script en Python con asyncio
├── docker-compose.yml   # Archivo de configuración para Docker
└── README.md            # Documentación del proyecto
```

---

## Requisitos previos

Asegúrate de tener instalados:

- **Git:** [Descargar Git](https://git-scm.com/)
- **Docker Desktop:** [Descargar Docker Desktop](https://www.docker.com/products/docker-desktop/) *(debe estar abierto antes de ejecutar los comandos)*

---

## Comprobar que Docker está listo (Opcional)

Si deseas verificar el funcionamiento de Docker en tu sistema, abre la terminal y ejecuta:

```bash
docker --version
docker compose version
```

---

## Cómo ejecutar el programa paso a paso

### 1. Clonar el repositorio
Abre la terminal y descarga el proyecto desde GitHub:

```bash
git clone [https://github.com/Leidy04S/Distribuidas_02_Concurrencia.git](https://github.com/Leidy04S/Distribuidas_02_Concurrencia.git)
```

### 2. Entrar a la carpeta del proyecto
```bash
cd Distribuidas_02_Concurrencia
```

### 3. Iniciar el programa con Docker Compose
Ejecuta el siguiente comando para iniciar el contenedor y ver el script en acción:

```bash
docker compose up
```

---

## Lo que verás en pantalla

En la consola observarás cómo la preparación de los tres pedidos inicia al mismo tiempo:

```text
============================================================
   EJEMPLO DE EJECUCIÓN CONCURRENTE: ATENCIÓN DE PEDIDOS
============================================================
En la ejecución concurrente, varias tareas avanzan al mismo
tiempo sin tener que esperar a que terminen las demás.

▶ Preparando pedido de Juan: Café expreso...
▶ Preparando pedido de María: Sándwich caliente...
▶ Preparando pedido de Pedro: Jugo natural...

✔ Pedido de Juan (Café expreso) entregado.

✔ Pedido de Pedro (Jugo natural) entregado.

✔ Pedido de María (Sándwich caliente) entregado.

============================================================
Todos los pedidos fueron entregados.
Tiempo total acumulado: 3.00 segundos.
============================================================
```

---

## Cómo detener y cerrar el programa

Para finalizar y eliminar el contenedor creado, ejecuta:

```bash
docker compose down
```