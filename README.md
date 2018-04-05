# codigos-postales-mexico
Script de python para generar archivos sql de la base de datos de códigos postales de SEPOMEX

# Requerimientos

* Python 3
* Python xrld

# Notas

Dentro de la carpeta `source` existe el archivo [CPdescarga.xls](http://www.correosdemexico.gob.mx/lservicios/servicios/Descarga.aspx) oficial de SEPOMEX.
**Nota: archivo actualizado a abril de 2018**

Dentro de la carpeta `sql` existen todos los archivos `.sql` para cada estado y un `codigos_postales_todos_los_estados.sql`.
Se puede descargar el archivo `codigos-postales-mes-año-sql.zip` que contiene los archivos antes mencionados.


# Instrucciones 

Instalar las dependencias

`pip install -r requirements.txt`

## Ejecucion
En la consola

`python generador-codigos.py table=nombre_de_la_tabla_a_usar`

Genera un archivo `sql/codigos_postales_todos_los_estados.sql` que contiene todos los CP para todos los estados

Si usamos:
`python generador-codigos.py table=nombre_de_la_tabla_a_usar --archivos-separados` 

generamos un archivo `sql/nombre_de_estado.sql` por cada estado.
