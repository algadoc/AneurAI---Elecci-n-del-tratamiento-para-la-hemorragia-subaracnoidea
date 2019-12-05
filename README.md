# AneurAI-AISaturdays-Madrid
Somos un grupo de la segunda edición de AISaturdays Madrid y hemos desarroyado este algoritmo que propone el mejor tratamiento a seguir para pacientes con hemorragia subaracnoidea.

#AneurAI_Script:
Este jupyter notebook muestra como puedes importar todos los .joblib y utilizar el algoritmo directamente. El algoritmo enter se puede usar con la función runPatient(). Los datos médicos e históricos son introducidos por separado para hacer la generación de los gráficos mas sencilla, y la función devuelve las predicciones para el tratamiento endovascular, quirúrgico, la posición y grupo del paciente en el PCA/KMean de los datos históricos y los mismos valores para el KPCA/KMean de los datos médicos.

#Página Web:
En esta carpeta está todo lo necesario para correr nuestra página web. Esta todavía en desarroyo, pero aun así permite el uso del algoritmo de manera dinámica y sencilla. Incluye el código HTML, stylings y el script de python que le permite usar el algoritmo. Hemos usado Flask para darle esta funcionalidad, y los archivos .joblib contienen los algoritmos ya preentrenados.
