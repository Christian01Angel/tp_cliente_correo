{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1b661d42caff4332",
   "metadata": {},
   "source": [
    "# Guía -- Entrega 2.\n",
    "\n",
    "Esta entrega se enfoca en la implementación de la gestión de carpetas y subcarpetas utilizando una estructura recursiva (árbol general) y en la optimización de la búsqueda y movimiento de mensajes dentro de estas carpetas.\n",
    "\n",
    "## Tareas para la Entrega 2\n",
    "\n",
    "### Fase 1: Diseño y Estructura de Datos del Árbol de Carpetas\n",
    "\n",
    "Para comenzar con la implementación, necesitamos definir las clases `Usuario` y `Mensaje` que se asumen de la Entrega 1. Estas son versiones mínimas para permitir el funcionamiento de las clases `Carpeta` y `SistemaCorreo`.\n",
    "\n",
    "Luego, implementaremos la clase `Carpeta` que representará un nodo en nuestra estructura de árbol de directorios, y la clase `SistemaCorreo` que gestionará la jerarquía de carpetas."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41f1d75b7941d565",
   "metadata": {},
   "source": [
    "### 1. Definir la Clase `Carpeta`\n",
    "\n",
    "La clase `Carpeta` es fundamental para construir el árbol de directorios. Cada instancia de `Carpeta` puede contener una lista de `Mensaje`s y una lista de otras instancias de `Carpeta` (subcarpetas). Hemos incluido los métodos `agregar_mensaje`, `quitar_mensaje` y `agregar_subcarpeta` como se solicitó."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2a5a23c3c6efdeb",
   "metadata": {},
   "source": [
    "### 2. Implementar la Estructura del Árbol (Clase `SistemaCorreo`, también debemos tener una copia local)\n",
    "\n",
    "La clase `SistemaCorreo` será el punto de entrada para gestionar la jerarquía de carpetas. Contendrá la `carpeta_raiz` (por ejemplo, \"Inbox\") y proporcionará métodos para navegar, manipular y buscar dentro de esta estructura."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79ebc525ab959d30",
   "metadata": {},
   "source": [
    "### 3. Implementar `mover_mensaje(mensaje, carpeta_destino)`\n",
    "\n",
    "Esta función es crucial para la gestión de mensajes. Su objetivo es reubicar un mensaje de su ubicación actual a una nueva carpeta de destino dentro de la jerarquía del correo.\n",
    "\n",
    "Para lograr esto, primero necesitamos localizar el mensaje en el árbol para poder eliminarlo de su carpeta original. Luego, lo añadiremos a la carpeta de destino. Utilizamos una función auxiliar `_find_message_in_tree` para encontrar el mensaje y la carpeta que lo contiene."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47eac8a6630b3681",
   "metadata": {},
   "source": [
    "### 4. Implementar `buscar_mensajes_recursivo(criterio, valor, carpeta_actual)`\n",
    "\n",
    "Esta función recursiva es clave para la eficiencia en la búsqueda de mensajes a través de toda la estructura jerárquica. Permite buscar mensajes basándose en atributos específicos como el asunto o el remitente, explorando cada carpeta y subcarpeta del árbol."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a23a89c21dde3a27",
   "metadata": {},
   "source": [
    "### Fase 3: Análisis de Eficiencia\n",
    "\n",
    "A continuación, se documenta la complejidad temporal y espacial de las operaciones implementadas.\n",
    "\n",
    "#### 5. Análisis de Complejidad de `mover_mensaje`\n",
    "\n",
    "La operación `mover_mensaje` en `SistemaCorreo` implica dos pasos principales:\n",
    "1.  **Buscar el mensaje de origen (`_find_message_in_tree`):**\n",
    "    *   **Complejidad Temporal:** En el peor de los casos, este método tendrá que visitar cada mensaje en cada carpeta del árbol hasta encontrar el mensaje (o determinar que no existe). Si `N` es el número total de mensajes en el sistema y `C` es el número total de carpetas, la complejidad es aproximadamente **O(N + C)**. Esto se debe a que se itera sobre todos los mensajes y se recorren todas las carpetas. En un árbol muy profundo con pocos mensajes por carpeta, podría ser más cercano a O(C); en un árbol plano con muchas carpetas y mensajes, más cercano a O(N).\n",
    "    *   **Complejidad Espacial:** La pila de llamadas recursivas para `_find_message_in_tree` puede llegar a ser tan profunda como la profundidad máxima del árbol, `D`. Por lo tanto, la complejidad espacial es **O(D)**.\n",
    "2.  **Eliminar de la carpeta actual (`quitar_mensaje`):**\n",
    "    *   **Complejidad Temporal:** Si la lista de mensajes en la carpeta actual tiene `m` mensajes, `list.remove()` tiene una complejidad de **O(m)** en el peor caso, ya que podría tener que buscar el mensaje y luego desplazar los elementos restantes.\n",
    "    *   **Complejidad Espacial:** **O(1)**.\n",
    "3.  **Agregar a la carpeta de destino (`agregar_mensaje`):**\n",
    "    *   **Complejidad Temporal:** `list.append()` es **O(1)** en promedio.\n",
    "    *   **Complejidad Espacial:** **O(1)**.\n",
    "\n",
    "**Complejidad Total de `mover_mensaje`:**\n",
    "*   **Temporal:** **O(N + C + m)**, donde `N` es el total de mensajes, `C` es el total de carpetas, y `m` es el número de mensajes en la carpeta de origen. El factor dominante generalmente será la búsqueda `O(N+C)`.\n",
    "*   **Espacial:** **O(D)**, debido a la recursión de búsqueda.\n",
    "\n",
    "La eficiencia de `mover_mensaje` depende significativamente de la distribución de mensajes y carpetas. Si el árbol es muy grande y el mensaje a mover está \"oculto\" en una rama profunda, la búsqueda puede ser costosa.\n",
    "\n",
    "#### 6. Análisis de Complejidad de `buscar_mensajes_recursivo`\n",
    "\n",
    "Esta función es inherentemente recursiva y explora todo el árbol de carpetas.\n",
    "\n",
    "*   **Complejidad Temporal:** En el peor de los casos, la función debe visitar cada carpeta y cada mensaje en el sistema para determinar si coincide con el criterio. Si `N` es el número total de mensajes y `C` es el número total de carpetas:\n",
    "    *   Se itera sobre los mensajes de la `carpeta_actual`.\n",
    "    *   Se itera sobre las `subcarpetas` y se llama recursivamente.\n",
    "    Esto significa que cada mensaje será inspeccionado una vez y cada carpeta será visitada una vez.\n",
    "    Por lo tanto, la complejidad temporal es **O(N + C)**.\n",
    "*   **Complejidad Espacial:** La función utiliza una lista para almacenar los `resultados` y la pila de llamadas recursivas.\n",
    "    *   La lista de `resultados` puede contener hasta `N` mensajes en el peor caso (si todos los mensajes coinciden).\n",
    "    *   La pila de llamadas recursivas puede ser tan profunda como la profundidad máxima del árbol, `D`.\n",
    "    Así, la complejidad espacial es **O(N + D)**.\n",
    "\n",
    "**Consideraciones Adicionales:**\n",
    "\n",
    "*   **Peor Caso:** El mensaje buscado no existe o es el último mensaje en la última hoja del árbol. La función recorrerá todo el árbol.\n",
    "*   **Mejor Caso:** El mensaje buscado es el primer mensaje en la `carpeta_raiz`. La función lo encuentra rápidamente sin mucha recursión.\n",
    "*   **Impacto del Tamaño del Árbol:** Cuanto mayor sea el número de carpetas (`C`) y mensajes (`N`), y cuanto más profundo sea el árbol (`D`), mayor será la complejidad. Para sistemas de correo muy grandes, estas operaciones pueden volverse lentas si no se implementan optimizaciones adicionales (ej. indexación de mensajes).\n",
    "\n",
    "### Fase 4 y 5: Material Adicional, Documentación y Entrega\n",
    "\n",
    "Estas fases corresponden a tareas que el usuario debe realizar externamente o que se gestionan a nivel de repositorio.\n",
    "\n",
    "#### 7. Crear Infografía o Video\n",
    "*   Esto es una tarea del usuario final.\n",
    "\n",
    "#### 8. Documentar el Código\n",
    "*   Se han incluido comentarios relevantes en el código para explicar la lógica.\n",
    "\n",
    "#### 9. Actualizar Diagrama de Clases\n",
    "*   Esto es una tarea del usuario final. El modelo de clases actual sería: `Usuario` -> `Mensaje` (remitente/destinatario) <- `Carpeta` (mensajes) <- `Carpeta` (subcarpetas) <- `SistemaCorreo` (carpeta_raiz).\n",
    "\n",
    "#### 10. Subir a GitHub y 11. Verificar la Entrega\n",
    "*  \n",
    "\n",
    "---\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}