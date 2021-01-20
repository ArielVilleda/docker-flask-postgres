# Flask, Postgres, Docker app
Mini sistema que expone servicios para manejo de inventario, Las entidades principales son: **Store** que funje el papel de Tienda o almacén, una entidad **Product** que es la que almacena de manera genérica, los tipos de productos que puede poseer una Tienda, y una entidad **Stock** que guarda las relaciones y/o almacenaje de los productos, al asignar un sku, se crea un registro en esta entidad, indicando que se ha añadido un producto a la tienda.

Se utiliza la biblioteca de **Flask** _**flask-restplus**_ para documentae todos estos servicios, es posible consultar está documentación acceciendo a **url_base** una vez levantado y en ejecución el proyecto _(se recomienda usar el ejemplo de docker proporcionado para fácil inicialización del proyecto)_


### Requisitos
- python >= 3.9
- postgres == 12.4
- librerías de python _**(ver project/requirements.txt)**_


### Instrucciones
- Crear el archivo **.env** dentro de la carpeta `/project` con los valores neesarios. Se proporciona un ejemplo en `project/example.env` para ser copiado integramente
- De ser neceario, crear usuario, base de datos, etc. con lo especificado en el **.env** _(si se utiliza el docker-compose.yaml proporcionado, estos valores se configuran automáticamente una vez creado el archivo **.env** ya que los datos para la BD son leídos de ahí)_
- Exportar variables de entorno al entorno de desarrollo _**(no se leen las varibles directamente del archivo .env. Es IMPORTANTE que estás variables existan en el enviroment, ya que se leen con la biblioteca defualt de python `os.environ.get()`. Sí se utiliza docker, estás varibales se cargan automáticamente del archivo al enviroment del container por lo que, una vez más, se recomienda levantar el proyecto con el ejemplo de docker proporcionadoS)**_
- Se configuró un archivo `project/manage.py` que proporciona los siguientes comandos útiles
    - `python manage.py db upgrade` Para realizar la migración de tablas a la BD de postgres
    - `python manage.py postal_codes` Para migrar los códigos postales de México a la tabla de postal_codes
    - `python manage.py run` Para levantar el servicio en el host 0.0.0.0:5000
- Es importante asegurar se de que los comandos `python manage.py db upgrade` y `python manage.py postal_codes` se hayan ejecutado para el correcto funcionamiento de la aplicación
- Visitar en el navegador `0.0.0.0:5000` o _la dirección en la que se este mapeando el servicio_, para ver la dcocumentación y poder acceder a la herramienta para probar estos servicios


### Docker
- Dentro de la carpeta `/docker`, configurar el archivo **docker-compose.yaml**. Se proporciona un ejemplo en `docker/docker-compose.example.yaml` para ser copiado integramente
- Se levantan dos containers:
    - El proyecto Flask con la imagen base de docker `python:3.9.1-slim-buster`
    - Un container que expone el servicio de postgres con la imagen base de docker `postgres:12.4`
- Para levantar los servicios utilizando **docker** se requiere lo siguiente:
    - Una vez dentro de la carpeta `/docker` y con nuestro archivo _yaml_ creado. Con solo ejecutar el comando `docker-compose up` se levantarán los containers necesarios
    - Automáticamente se ejecuta un _shell script_ en el container con python el cual migra las tablas de la base y los datos de los postal_codes _(ver archivo `porject/init_app.sh`)_
    - Si nuestro variable de entorno **FLASK_ENV** es para _development_, será necesario acceder al container de python _(ej. `docker-compose exec project bash`)_ y dentro, ejecutar el comando `python manage.py run` el cual levantará el servicio en la dirección `0.0.0.0:5000` del container y la ligará a `localhost:80`de nuestra máquina _(ver archivo `docker/docker-compose.example.yaml`)_ 
