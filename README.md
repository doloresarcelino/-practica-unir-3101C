# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

Para ejecutar el script `main.py`, sigue estos pasos:

1. Abre una terminal.
2. Navega al directorio donde se encuentra el script `main.py`.
3. Ejecuta el siguiente comando:

   ```bash
   python3 main.py <filename> <dup> [order]
   ```

Donde:

*  __filename__: ruta al fichero que contiene la lista de palabras, una por línea.
*  __dup__: yes para eliminar palabras duplicadas, no para mantener la lista.
*  __order (opcional)__: asc para ordenar las palabras de forma ascendente, desc para ordenarlas de forma descendente. Si no se proporciona, el orden predeterminado será ascendente.

Por ejemplo:

   ```bash
   python3 main.py words.txt yes asc
   ```

Este comando leerá las palabras del archivo **words.txt**, eliminará los duplicados y ordenará las palabras de forma ascendente. Ajusta los argumentos según sea necesario.

## Ejecución del Makefile

Si prefieres utilizar el Makefile para ejecutar el script `main.py` puedes hacerlo de la siguiente manera:

1. Abre una terminal
2. Navega al directorio dónde se encuetra este repositorio
3. Ejecuta el siguiente comando

   ```bash
   make
   ```

Este comando ejecuta el Makefile predeterminado que incluye instrucciones para ejecutar el script utilizando Docker.

## Ejecución del Makefile Local

Si prefieres utilizar el script `main.py` sin Docker utilizando el Makefile local puedes hacerlo de la siguiente manera:

1. Abre una terminal
2. Navega al directorio dónde se encuetra este repositorio
3. Ejecuta el siguiente comando

   ```bash
   makei -f Makefile_local
   ```

Este comando ejecutará el Makefile local, que está configurado para ejecutar el script sin utilizar Docker. Asegúrate de haber renombrado tu Makefile local como Makefile_local para utilizar este comando.
