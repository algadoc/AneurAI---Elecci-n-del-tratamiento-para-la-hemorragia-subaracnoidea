# AneurAI: Proposición del tratamiento para paciente con HSA
![alt text](https://github.com/algadoc/AneurAI-AISaturdays-Madrid/blob/master/LogoAneurisma.PNG)

Somos un grupo de la segunda edición de AISaturdays Madrid y hemos desarrollado este algoritmo que propone el mejor tratamiento a seguir para pacientes con hemorragia subaracnoidea.

## Qué es la HSA

La HSA (hemorragia subaracnoidea) es un volcado de sangre entre la aracnoide y la piamadre, dos de las capas que recubren y protegen el cerebro. Este derramamiento puede producir daño cerebral en cuestión de minutos, y afecta a 1 de cada 1000 personas. Muchos de estos casos ocurren cuando se ruptura un aneurisma, una deformación de la pared arterial dentro del cerebro. Tras numerosos ciclos de presión de la sangre, pequeñas deformaciones en la pared de las arterias empiezan a crecer y forman pompas o globos que debilitan la pared. Al romperse, el torrente sanguineo se expone al ecosistema intracraneal, lo cual resulta en una HSA. La primera imagen es una reconstrucción de un aneurisma, y la segunda es el resultado de la ruptura de uno.
 ![alt text](https://github.com/algadoc/AneurAI-AISaturdays-Madrid/blob/master/Aneurisma.gif) ![alt text](https://github.com/algadoc/AneurAI-AISaturdays-Madrid/blob/master/HSA.png)

## Dataset

Hemos utilizado datos recogidos por la Asociación Española de Neurocirugía entre los años 2004 y 2015. Se grabaron numerosas variables médicas de 4000 pacientes, pero al final las variables incluidas en el modelo son:

- Edad
- Sexo
- Múltiple (si el paciente tiene mas de un aneurisma)
- Glasgow Comma Scale (https://www.glasgowcomascale.org/)
- World Federation of Neurological Surgeons Subarachnoid Hemorrhage Grading (https://emedicine.medscape.com/article/2172497-overview)
- Fisher Scale (https://emedicine.medscape.com/article/2172467-overview)
- Tamaño del aneurisma
- Momento (en que punto del desarrollo de la hemorragia se trató)

## Modelos

Buscamos qué modelo nos daría la mejor capacidad de predicción. Entre los que probamos cabe destacar:

- Random Forest Classifier
- Decision Tree Classifier
- SVM

Al final encontramos que un AdaBoost Classifier con 200 Decision Trees y un Learning Rate de nos daba la mayor precisión.

## AneurAI_Script

Este jupyter notebook muestra cómo puedes importar todos los .joblib y utilizar el algoritmo directamente. El algoritmo se puede usar con la función runPatient(). Los datos médicos e históricos son introducidos por separado para hacer la generación de los gráficos más sencilla, y la función devuelve las predicciones para el tratamiento endovascular, quirúrgico, la posición y grupo del paciente en el PCA/KMean de los datos históricos y los mismos valores para el KPCA/KMean de los datos médicos.

## Página Web

En esta carpeta está todo lo necesario para correr nuestra página web. Está todavía en desarrollo, pero aun así permite el uso del algoritmo de manera dinámica y sencilla. Incluye el código HTML, stylings y el script de Python que le permite usar el algoritmo. Hemos usado Flask para darle esta funcionalidad, y los archivos .joblib contienen los algoritmos ya pre entrenados.

## Próximos pasos

La mayor limitación que hemos encontrado a la hora de mejorar este algoritmo ha sido el bajo número de pacientes incluidos en la muestra. Esto causa que el efecto del tratamiento en muchos pacientes sea difícil de detectar. Queremos buscar otras bases de datos que nos permitan mejorar el algoritmo y así hacer predicciones más precisas. 

## Participates
Alfonso Lagares, Miguel Flores, Pablo T. Campos
