import asyncio
import time

async def atender_pedido(cliente, producto, duracion):
    print(f"▶ Preparando pedido de {cliente}: {producto}...")
    await asyncio.sleep(duracion)  # Simula el tiempo de preparación sin bloquear el programa
    print(f"✔ Pedido de {cliente} ({producto}) entregado.\n")

async def main():
    inicio = time.perf_counter()

    print("=" * 60)
    print("   EJEMPLO DE EJECUCIÓN CONCURRENTE: ATENCIÓN DE PEDIDOS")
    print("=" * 60)
    print("En la ejecución concurrente, varias tareas avanzan al mismo")
    print("tiempo sin tener que esperar a que terminen las demás.\n")

    # Inicia y atiende los tres pedidos de forma concurrente
    await asyncio.gather(
        atender_pedido("Juan", "Café expreso", 2),
        atender_pedido("María", "Sándwich caliente", 3),
        atender_pedido("Pedro", "Jugo natural", 2)
    )

    fin = time.perf_counter()

    print("=" * 60)
    print(f"Todos los pedidos fueron entregados.")
    print(f"Tiempo total acumulado: {fin - inicio:.2f} segundos.")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())