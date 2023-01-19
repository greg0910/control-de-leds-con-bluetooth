# Control de LEDs con Bluetooth
Este código es un ejemplo de cómo controlar un conjunto de LEDs con un dispositivo Bluetooth utilizando el módulo de Python de bluedot. Se utilizan las librerías siguientes:

- bluedot.btcomm: para establecer la conexión Bluetooth
- signal: para pausar el programa
gpiozero: para controlar los LEDs
- time: para controlar el tiempo de espera en el código
## Uso
El código establece una conexión Bluetooth y espera la recepción de datos enviados desde un dispositivo externo. Los datos deben ser enviados en un formato específico (explicado en el código) para que sean interpretados y utilizados para controlar los LEDs.

## Configuración
Asegúrese de tener instaladas las librerías necesarias para ejecutar el código y de tener un dispositivo Bluetooth conectado a la Raspberry Pi. También debe configurar los pines de la Raspberry Pi según su configuración.

## Ejecución
Para ejecutar el código, abra una terminal en la Raspberry Pi y navegue hasta la carpeta donde se encuentra el archivo. Ejecute el código con el comando `python nombre_archivo.py`. Utilice un dispositivo externo conectado vía Bluetooth para enviar los datos necesarios para controlar los LEDs.

## Problemas conocidos
- El código está diseñado para funcionar con una Raspberry Pi específica, por lo que es posible que deba modificar algunas líneas de código para adaptarlo a su configuración.
- El código espera recibir datos en un formato específico, por lo que si no se envían los datos en el formato correcto, el código no funcionará correctamente.
## Licencia
Este código está disponible bajo la licencia MIT. Puede ser utilizado, modificado y distribuido libremente siempre y cuando se incluya este aviso de licencia.