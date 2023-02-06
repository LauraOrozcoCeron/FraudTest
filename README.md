# PRUEBA DATA SCIENTIST R5 #

Los principales proyectos de R5 vienen encaminados al sector vehículos. Usted deberá apoyarse de sus conocimientos para cumplir el siguiente objetivo:

## Fraude en las reclamaciones de siniestro

* **Objetivo:** Un modelo de machine learning que prediga la probabilidad de que una reclamación sea o no un fraude. *Modelo funcional*
**Contexto:** La base de datos corresponde a data de 1994 a 1996 y cada registro corresponde a un individuo que realizo una reclamacion del seguro del vehiculo por un accidente. De acuerdo al planteamiento del problema, es posible que se presenten casos de fraude en el seguro lo que se traduce en reclamos con informacion falsa o sobre exagerada para el cobro del mismo. 

## DICCIONARIO DE DATOS:

Columnas (Columns):

* 00) Month: mes en el que ocurrió el accidente. (Month in which the accident occured)

* 01) WeekOfMonth: semana en la que ocurrió el accidente. (Week in the month of accident)

* 02) DayOfWeek: Día de la semana en que ocurrió el accidente. (Day of the week of the accident)

* 03) Make: Marca del vehículo. (Car maker)

* 04) AccidentArea: Si el accidente fue en un área rural o urbana. (Accident occured in rural or urban area)

* 05) DayOfWeekClaimed: Día de la semana en la que se hizo la denuncia, "controlar ceros". (Day of the week the accident was claimed, "control zeros")

* 06) MonthClaimed: Mes en el que se hizo la denuncia, "controlar ceros". (Month the accident was claimed, "control zeros")

* 07) WeekOfMonthClaimed: Número de semana del mes en la que se hizo la denuncia. (Week in the month of accident)


* 08) Sex: Género de la persona que realiza la denuncia. (Gender of the person involved in the accident)

* 09) MaritalStatus: Estado cívil de la persona que hace la denuncia. (Marital status of the person involved in the accident)

* 10) Age: Edad de la persona que hace la denuncia. (Age of the person involved in the accident)

* 11) Fault: Si el culpable fue el dueño del seguro u otro involucrado. (If the insurance owner was responsable of the accident)

* 12) PolicyType: Combinación de tipo de auto y de tipo de póliza: Liability (contra terceros), Collision (Incluye daños al vehículo del propietario), All Perils (contra todo riesgo). (Combination between Vehicle Category and Base Policy)

* 13) VehicleCatergory: Clasificación de tipo de auto. (Vehicle categorization)

* 14) VehiclePrice: Precio del vehículo. (Price of the vehicle)

* 15) FraudFound_P: Si el incidente fue fraudulento o no)

* 16) PolicyNumber: Número único de accidente, coincide con el número de filas del dataset. (Unique number of each entry)

* 17) RepNumber: Numeración entre 1 y 16. (Enumeration between 1 and 16)

* 18) Deductible: Costo del seguro. (Ensurance cost)

* 19) DriverRating: Calificación del piloto, puede ser data ordinal. (This driver rating might be ordinal)

* 20) Days_Policy_Accident: Rango adquisición del seguro y suceso del accidente. (Days between ensurance is acquired and the accident occured)

* 21) Days_Policy_Claim: Rango entre adquisición del seguro y denuncia del accidente. (Days between ensurance is acquired and the accident was claimed)

* 22) PastNumberOfClaims: Cantidad de denuncias anteriores realizadas por el dueño del vehículo. (Number of past claims of the ensurance owner)

* 23) AgeOfVehicle: Edad del vehículo.

* 24) AgeOfPolicyHolder: Edad del dueño del seguro.

* 25) PoliceReportFiled: Si fue denunciado a la policía. (If the accident was reported to the police)

* 26) WitnessPresent: Si hay testigos.

* 27) AgentType: Internos son cuando el fraude es realizado por personas trabajando en la empresa de seguros. Externos son los fraudes en los que el seguro es engañado por personas independientes 

* 28) NumberOfSuppliments: Son daños al vehículo no registrados a la hora de la denuncia, daños extras que no se ven por el exterior, normalmente roturas en componentes internos como suspensión, chasis, etc.

* 30) NumberOfCars: Número de autos involucrados en el accidente. 

* 31) Year: Año en el que ocurrió el accidente.

* 32) BasePolicy: Tipo de seguro, igual a PolicyType. (Tipe of ensurance)

# Modelo de clasificacion:

De acuerdo a la data suministrada, tenemos un caso que se puede resolver a traves de aprendizaje supervisado, para este problema seleccione el modelo XGBoost que puede resolver esta problematica, es un modelo minimo viable el cual se le realizo optimizacion de hiperparametros para mejorar su rendimiento. Para el modelo se utiilizaron las siguientes variables: 'monthh', 'weekofmonth', 'dayofweek', 'make', 'accidentarea', 'dayofweekclaimed', 'monthclaimed',
'weekofmonthclaimed', 'sex', 'maritalstatus', 'fault', 'vehiclecategory', 'vehicleprice',
'driverrating', 'days_policy_accident', 'days_policy_claim', 'pastnumberofclaims', 'ageofvehicle',
'ageofpolicyholder', 'policereportfiled', 'witnesspresent', 'agenttype', 'numberofsuppliments',
'addresschange_claim', 'numberofcars', 'yearr', 'basepolicy', 'policytype'.


* **Metricas de negocio**

El modelo al aportar las predicciones de posibles fraudes de acuerdo a las caracteristicas evaluadas permitiria crear estrategias de revision exhaustiva de documentos que permitan determinar la veracidad de la informacion suministrada por el siniestrado. En cuanto a metricas del negocio evaluaria la proporcion de polizas aprobadas por la entidad, si al realizar la evaluacion exahustiva se logra reducir el cobro de seguros.

* **Despliegue**

Crear un dockerfile basada en una imagen de python que instale los paquetes usados en el proyecto copie el modelo y el codigo fuente del predict al contenedor y como entry point del contenedor definir levantar la api utilizando un servidor web como uvicorn. Posterior a eso publicar la imagen a un repositorio de imagenes ECR de AWS para luego utilizarlo en el servicio ECS de AWS. Posteriormente, conectar el cluster de contenedores al servicio de api gateway de AWS que controlaria el trafico de nuestra api.


* **Instrucciones de uso**

Para correr el proyecto es necesario instalar las librerias en requierements.txt y posterior a eso ejecutar los archivos .py preprocessing, train y predict (este esta adecuado para un caso particular). El archivo app.py contiene un servidor web local que permite visualizar las predicciones a partir de un request body. 
Dentro de la carpeta model se encuetra el modelo entrenado el cual es output del archivo train.py.

