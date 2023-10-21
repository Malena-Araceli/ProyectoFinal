# Proyecto Final en Python y Django - Basoalto Malena

Este proyecto es una aplicación web desarrollada en Python con el uso del framework Django y se enfoca en la gestión de registros para casamientos. La aplicación almacena y muestra información sobre regalos, parejas de casados, comentarios, lista de invitados y usuarios. A continuación, encontrarás una descripción detallada de los componentes clave de la aplicación.

## Componentes del Proyecto

### Modelos

- `models.py`: En este archivo, se definen los modelos de datos utilizados por la aplicación. Los modelos incluyen:
  - `Regalo`: Este modelo almacena información sobre los regalos, como nombre, descripción, precio y el usuario que lo creó.
  - `Pareja`: Contiene detalles sobre las parejas de casados, como nombres de los cónyuges y la fecha de casamiento.
  - `Avatar`: Registra avatares para los usuarios de la aplicación.
  - `Invitado`: Contiene detalles sobre los invitados, solicitando nombre,apellido y un email.
  - `Comentario`: Registra el autor, mensaje, fecha de publicacion y selecciona a la pareja que desea enviarle el comentario.



### Formularios

- `forms.py`: Aquí encontrarás los formularios utilizados para ingresar y editar la información de los regalos, parejas, avatares, invitados y comentarios.Asi como tambien el inicio de sesion, registro de usuario y la edicion del mismo.

### URLs

- `urls.py`: Este archivo contiene las rutas URL que dirigen las solicitudes a las vistas correspondientes de la aplicación.

### Vistas

- `views.py`: En este archivo se definen todas las vistas utilizadas en la aplicación. Cada modelo sigue el concepto de CRUD (Crear, Leer, Actualizar, Eliminar). Además, encontrarás vistas para el inicio de sesión, registro y edición de perfiles de usuario.

### Plantillas

La carpeta `templates` contiene archivos HTML que se utilizan para renderizar las páginas web de la aplicación. Se emplea una plantilla de Bootstrap y se aplica el concepto de herencia a cada archivo.

## Procesador de contexto

Se ha agregado un contexto de usuario personalizado que muestra el avatar del usuario en la barra de navegación.

## Caso prueba

Se ha agregado un archivo txt detallado donde se pueden ver los errores y soluciones, tambien una hoja de calculos que se puede visualizar aqui https://docs.google.com/spreadsheets/d/1u1D6OBS1Wrd-4xAIYNA8T2FR16vXDVpA8VKXx6R6Psc/edit?usp=sharing

## Autor

Este proyecto fue desarrollado por Basoalto Malena
.

## Demostración

Puedes ver una demostración de la aplicación en funcionamiento en https://www.youtube.com/watch?v=9eFRTjIbZZo
