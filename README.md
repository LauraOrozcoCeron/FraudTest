# PRUEBA DATA SCIENTIST R5 #

Los principales proyectos de R5 vienen encaminados al sector vehiculos. Usted deberá apoyarse de sus conocimientos para cumplir el siguiente objetivo:

* **Reducir perdidas por fraude en las reclamaciones de siniestro**

¿Que debe incluir tu solución?

1) Cree una base de datos en PostgreSql (puede ser local) que debe contener una tabla llamada "fraudes" con la información contenida en ./data/fraude.csv. (el archivo ./data/create_table.txt te ayudará)

2) Con su base de datos cargada, replique la siguente salida sin usar subconsultas.

![Salidaesperada](./data/salida_esperada.png)

3) conectese desde python a la tabla fraudes (la de la base de datos creada, no directamente del .csv) y leala con un query que la traiga lo mas limpia posible.

4) en la carpeta *./notebooks* desarrolle la solución que debe contener un analisis descriptivo de los datos y un modelo de machine learning que ayude a cumplir los objetivos (no se enrede mucho con hacer el mejor modelo, enfoquese en que sea algo funcional).

5) automatice su pipeline de entrenamiento en el archivo *train.py*, imprimiendo por consola o exportando los principales hallazgos. Exporte el modelo y lo guarda en la carpeta *./models*. En el archivo *predict.py* escriba el pipeline de prediccion, pruebelo con el caso particular que usted desee e imprima por consola este caso y su valor predicho (en proabilidades puede ser).

6) Comenta como utilizaría el negocio este modelo para reducir las predidas por fraude, como lo evaluarias frente a las necesidades del negocio (diferente a las métricas ya usadas) y comenta brevemente como llevarias a producción este proyecto.

* Nota1: Crea un repositorio que contenga en el readme.md las instrucciones necesarias para instalar y correr tu proyecto.


* Nota2: Muchos exitos!, cualquier duda puedes escribirme por wp: 3113716605, en serio, cualquier duda.
