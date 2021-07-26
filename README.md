# bocobases
## Sistema de monitoreo de bases para proyecto Bocosur

# Descripción

Este es un sistema muy sencillo de monitoreo de bases de medición 
para el proyecto Bocosur. Consta de dos archivos prinicipales:

*   cliente.py
*   servidor.py

## Servidor

El programa _servidor.py_  levanta un servicio web dedicado 
(WSGI -- Web Service Gateway Interface). Esto no es otra cosa
que un pequeño servidor web dedicado a una cosa particular, en
lugar de un servidor web general de páginas, etc., como Apache.

Puntualmente, _servidor.py_  recibe mensajes periódicamente desde
cada una de las bases. Estos mensajes incluyen información como:

*   status de la base
*   captura de imagen actual desde la cámara

Los mensajes de por sí indican que la base está operativa y conectada.
La ausencia de mensajes de una base puede indicar que hay un corte
en la conexión de internet entre base y servidor, o bien que la base se
cayó por algún motivo desconocido.

Como tarea secundaria, el servidor genera una página web estática
en donde se muestra el último estado e imagen de cada base en la red
de bases de Bocosur.

## Cliente

El programa _cliente.py_  se comunica con _servidor.py_. Para esto
envía un _query_  hacia  el host y puerto en donde se ubica el 
_servidor_, en donde se envía el status y la última captura de
la cámara almacenada en disco por el software de control de la cámara
(que corre aparte). El envío se hace mediante el mecanismo POST.

La respuesta del servidor también es útil en caso de caída de la conexión.
Si la base está activa pero el mensaje no logra llegar al servidor 
(esto se puede verificar mediante el resultado del query HTTP), el evento
en cuestión se registra internamente como mensaje no enviado.

PENDIENTE: si existen eventos no enviados hacia el servidor, deberían
enviarse retroactivamente  por un canal especial (por ej., otra URL)
al servidor para que éste tome nota de lo sucedido.

# Instalación

Tanto el cliente como el servidor requieren Python 3.x para funcionar.
Python es libre y gratuito y puede descargarse para todos los sistemas 
operativos desde la página del proyecto.

El único paquete no estándar de Python que se utiliza es `Bottle`,
que puede instalarse, por ejemplo, usando la herramienta de paquetes `pip`

pip install bottle

# Autor

Por dudas o consultas dirigirse a Ignacio Ramírez <nacho@fing.edu.uy>

