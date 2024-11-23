<h1 align="center">Práctica 2: Alineamientos con Biopython</h1>

**Participantes:**
- Ricardo Juan Cárdenes Pérez
- Susana Suárez Mendoza

<div align="justify">
    
Esta práctica consta de dos ejercicios que ponen en práctica la función `PairWiseAligner` de Biopython para alinear secuencias y obtener la puntuación y el alineamiento óptimo.

## Ejercicio 1: 

Usa la clase PairWiseAligner de Biopython para alinear secuencias  de ADN y obtener la puntuación y el alineamiento óptimo en estos dos escenarios. Prueba a cambiar los parámetros del alineador como el esquema de puntuación, las penalizaciones de alineamiento y la modalidad de alineamiento (global o local). Compara los resultados obtenidos con diferentes configuraciones y explica las diferencias

### Apartado a) Obtener las secuencias aleatoriamente

#### 1. Generación de secuencias aleatorias de longitud fija o variable

Para generar las secuencias aleatorias, se ha implementado la función `generate_random_dna_sequence`, que utiliza la función `random.choice` del módulo estándar de Python. Esta función realiza un bucle que itera tantas veces como se indique en la longitud deseada de la secuencia y selecciona aleatoriamente un nucleótido de entre las opciones disponibles ('A', 'C', 'G', 'T').

El código de la función es el siguiente:

```python
def generate_random_dna_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))
```

Además, en el *notebook* presentado, la longitud de la cadena también se ha generado de manera aleatoria utilizando la función `random.randint`, lo que permite obtener secuencias de longitud variable en función de los parámetros especificados. Esto garantiza la variabilidad tanto en los nucleótidos como en la longitud de las secuencias generadas.

#### 2. Alineamiento de Secuencias Mediante Búsqueda en Rejilla

La **búsqueda en rejilla** es una técnica ampliamente utilizada para optimizar hiperparámetros en modelos de aprendizaje automático mediante la evaluación exhaustiva de todas las combinaciones posibles dentro de un espacio discretizado. Consiste en definir un conjunto de valores para cada hiperparámetro y construir una rejilla que abarque todas las combinaciones posibles. Cada configuración se emplea para entrenar o validar el modelo, evaluando su desempeño con una métrica específica, como la precisión o el error. En este contexto, se evalúan las puntuaciones obtenidas para identificar la variabilidad de los hiperparámetros y su impacto en el alineamiento.

Los parámetros probados para el alineamiento son los siguientes:

```python
param_grid = {
    "mode": ["global", "local"],
    "match_score": [1, 2, 3],
    "mismatch_score": [-1, -2, -3],
    "open_gap_score": [-2, -3, -4],
    "extend_gap_score": [-0.5, -1, -1.5],
}
```

El parámetro `open_gap_score` se asocia con la penalización aplicada a la apertura de un hueco en el alineamiento, mientras que `extend_gap_score` se refiere a la penalización por extender un hueco ya existente, independientemente de su posición. Para implementar la búsqueda en rejilla, se desarrolló una función que permite configurar los hiperparámetros del alineamiento y devuelve tanto la puntuación como el resultado del alineamiento:

```python
def align_with_parameters(seq1, seq2, **kwargs):
    aligner = PairwiseAligner()
    for key, value in kwargs.items():
        setattr(aligner, key, value)

    alignment = aligner.align(seq1, seq2)
    return alignment.score, alignment
```

Finalmente, las configuraciones de los parámetros, junto con las puntuaciones y los resultados del alineamiento, se almacenaron en un `DataFrame` para facilitar su análisis posterior. Esto permite comparar y seleccionar la combinación de parámetros más adecuada para el alineamiento óptimo de secuencias.

#### 3. Análisis de resultados

##### 3.1. Visualización de la puntuación en función del valor de los parámetros y el modo

Se propone generar gráficos de caja (*boxplots*) para analizar la relación entre cada hiperparámetro y la puntuación ("score") del alineamiento. La Figura 1 muestra el resultado para una secuencia aleatoria donde se observa que el modo local destaca en puntajes gracias a su enfoque en regiones similares y parámetros permisivos, mientras que el modo global es más sensible a penalizaciones debido a su alineamiento completo; entre los parámetros, *match_score* y *mismatch_score* tienen el mayor impacto directo en los puntajes finales. 

<div align="center">
    <img src="images/boxplot.png" alt="Boxplot" />
      <p><strong>Figura 1.</strong> <i>Boxplots</i> .</p> 
</div>

##### 3.2. Visualización de cómo afectan las puntuaciones obtenidas bajo ciertas condiciones

Se propone agrupar las puntuaciones en un número de rango, generando etiquetas en formato `[min - max]` y asignando cada puntuación a uno de estos grupos (`score_group`). Luego, se visualiza cómo los parámetros ajustables (`match_score`, `mismatch_score`, `open_gap_score`, `extend_gap_score`) se distribuyen según los rangos de puntuación, creando subgráficos individuales con curvas de densidad. 

###### 3.2.1. Visualización de la distribución de parámetros por rangos de puntuación - Modo local

En el modo local, las configuraciones que generan puntuaciones más altas en el alineamiento de secuencias se asocian con valores altos de `match_score` y penalizaciones menos severas (valores menos negativos) en `mismatch_score`, `open_gap_score` y `extend_gap_score`. En particular, un `match_score` elevado recompensa mejor las coincidencias, mientras que penalizaciones ligeras para desajustes y brechas favorecen puntuaciones más altas, destacando la importancia de ajustar estas configuraciones para maximizar el rendimiento del alineamiento.

<div align="center">
    <img src="images/dens_local.png" alt="Densidad local" />
      <p><strong>Figura 2.</strong>Curvas de densidad del modo local.</p> 
</div>

###### 3.2.2. Visualización de la distribución de parámetros por rangos de puntuación - Modo global

En el modo global, las puntuaciones más altas se logran con un `match_score` elevado, penalizaciones ligeras para desajustes (`mismatch_score` cercano a 0), y valores menos negativos en `open_gap_score` y `extend_gap_score`. Configuraciones que favorecen coincidencias y minimizan las penalizaciones por desajustes y brechas son clave para optimizar el alineamiento global, ya que estas reducen el impacto negativo de las restricciones en la puntuación final.

<div align="center">
    <img src="images/dens_global.png" alt="Densidad global" />
      <p><strong>Figura 3.</strong>Curvas de densidad del modo global.</p> 
</div>

#### 4. Conclusiones Generales

Los resultados muestran que el desempeño de los alineamientos depende tanto de los parámetros configurados como del tipo de alineamiento (local o global). Los alineamientos locales, al enfocarse en regiones similares, ofrecen mejores puntajes con configuraciones más permisivas, siendo ideales para secuencias parcialmente conservadas. Por otro lado, los alineamientos globales, más sensibles a penalizaciones, requieren ajustes precisos para equilibrar recompensas como el `match_score` y penalizaciones (`mismatch_score`, `gap scores`) y son útiles para comparaciones a lo largo de toda la longitud de las secuencias. Ajustar los parámetros según el objetivo permite maximizar la utilidad en el análisis de similitudes y diferencias estructurales.

### Apartado b) Obtener las secuencias a partir de ficheros obtenidos de bases de datos biológicas

En este apartado se propone utilizar las herramientas de NCBI Entrez (una interfaz para buscar y recuperar información biológica). Para ello, se definen las siguientes funciones:
1. Función `get_sequences_ncbi`: esta función realiza una búsqueda en una base de datos de NCBI (como "nucleotide" o "protein") utilizando un término de búsqueda (`search_term`) y obtiene un número limitado de resultados (`max_results`). Posteriormente, llama a otra función para descargar las secuencias encontradas.
2. Función `get_sequences_by_id`: esta función descarga las secuencias de NCBI utilizando los identificadores de secuencia proporcionados. Las secuencias se guardan en archivos FASTA individuales en una carpeta local.

#### 1. Obtención del Fichero FASTA de las Secuencias

Se han planteado dos casos de estudio centrados en el análisis de secuencias genéticas: uno relacionado con las isoformas de un gen humano y otro enfocado en la comparación de un mismo gen entre dos especies diferentes.

**Caso 1: Gen BRCA1 (Breast Cancer 1).**  
El gen BRCA1 es un gen humano localizado en el cromosoma 17 (17q21) que codifica una proteína supresora de tumores, fundamental para el mantenimiento de la estabilidad del ADN y la regulación del ciclo celular. Su principal función es reparar el ADN dañado y prevenir mutaciones genéticas que podrían derivar en cáncer. En este caso, se propone analizar las diferencias entre las isoformas (variantes de transcripción) del gen BRCA1 en humanos.

**Caso 2: Gen FOXP2 (Forkhead Box P2).**  
El gen FOXP2 está asociado con el desarrollo del lenguaje y el habla en humanos, siendo crucial para la comunicación vocal en humanos y otros animales. En este caso, se propone comparar la secuencia del gen FOXP2 en humanos con la secuencia homóloga en ratones, con el objetivo de identificar similitudes y diferencias evolutivas entre ambas especies.

#### 2. Alineamiento de las secuencias de manera global

Para realizar el alineamiento global de las secuencias, se han desarrollado funciones específicas que permiten reconstruir y evaluar el alineamiento de manera detallada. Estas funciones se describen a continuación:
1. **`final_sequence`**  
   Esta función toma como entrada un objeto de alineamiento, junto con las secuencias objetivo (*target*) y consulta (*query*), y genera tres representaciones alineadas:
   - **Secuencia objetivo alineada**: refleja cómo la secuencia objetivo se ajusta en el alineamiento.
   - **Secuencia consulta alineada**: muestra la consulta alineada con la secuencia objetivo.
   - **Línea de alineamiento**: indica coincidencias (representadas por las bases alineadas), desajustes (`*`), y brechas (`-`) en las posiciones correspondientes.  
   Esto se logra recorriendo las coordenadas del alineamiento y manejando tanto los segmentos alineados como las brechas que puedan surgir.

2. **`count_alignment_details`**  
   Esta función analiza la línea de alineamiento generada por `final_sequence` y calcula:
   - **Coincidencias (`matches`)**: número de bases que coinciden entre las secuencias alineadas.
   - **Desajustes (`mismatches`)**: número de posiciones donde las bases no coinciden (`*`).
   - **Brechas (`gaps`)**: número de guiones (`-`) insertados en el alineamiento para manejar inserciones o deleciones.  
   Estos valores permiten evaluar la calidad del alineamiento y obtener métricas cuantitativas clave.

#### 3. Visualización de los resultados

##### **Caso 1.** Gen BRCA1.

La Figura 4 muestra las coincidencias (regiones en blanco), los huecos añadidos para el alineamiento (regiones en rojo) y los desajustes (regiones en azul) de las dos isoformas del gen. Aunque las isoformas tienen un grado significativo de similitud (como se ve en las regiones alineadas), las diferencias observadas en los desajustes y brechas indican variaciones significativas que podrían explorarse más para comprender su relevancia biológica. Esto es especialmente importante para el papel de BRCA1 como supresor de tumores y en el mantenimiento de la estabilidad del ADN.

<div align="center">
    <img src="images/brca_mapa.png" alt="BRCA" />
      <p><strong>Figura 4.</strong>Mapa de alineamiento de las isoformas del gen BRCA1.</p> 
</div>

##### **Caso 2.** Gen FOXP2.

La Figura 5 muestra información similar a la Figura 4 salvo que esta presenta el gen FOXP2. El análisis sugiere que el gen FOXP2 presenta una conservación significativa entre humanos y ratones, lo que resalta su importancia funcional. Sin embargo, las variaciones observadas (gaps y desajustes) apuntan a diferencias evolutivas que pueden estar relacionadas con las especializaciones funcionales en cada especie. 

<div align="center">
    <img src="images/foxp2_mapa.png" alt="FOXP2" />
      <p><strong>Figura 5.</strong>Mapa de alineamiento del gen FOXP2.</p> 
</div>

</div>

<br>

## Ejercicio 2: Implementación del alineamiento con matrices de puntuación

En este ejercicio se desarrolla una solución modular que utiliza clases específicas para implementar y configurar el proceso de alineamiento, permitiendo no sólo modificar manualmente las puntuaciones como se quiera, sino dando la oportunidad al usuario de proporcionar su propia matriz de puntuación para llevar a cabo el alineamiento, además de las matrices ya ofrecidas por BioPython.

### Clases principales

#### Aligner
- Contiene la lógica principal para realizar el alineamiento.
- Permite la configuración de los parámetros de alineamiento, como el modo (global o local), las puntuaciones de coincidencia y desajuste, y las penalizaciones de huecos.
- Proporciona métodos para calcular el alineamiento y obtener la puntuación final.
  
#### AlignerArgs
- Diseñada para manejar los argumentos necesarios para personalizar el comportamiento del alineamiento.
- Facilita la configuración flexible de los parámetros de entrada.

#### AlignerBuilder
- Actúa como una fábrica para instanciar y configurar objetos Aligner según las necesidades del usuario.
- Centraliza la lógica de inicialización para evitar errores al instanciar manualmente los componentes del alineamiento.

#### DataLoader
- Maneja la carga de datos de secuencias desde diferentes fuentes, como archivos locales en formato FASTA o bases de datos externas.
- Garantiza que las secuencias estén listas para ser procesadas por las demás clases.

#### Optimizer
- Proporciona herramientas para ajustar automáticamente los parámetros del alineador utilizando técnicas como búsqueda en rejilla.
- Permite encontrar configuraciones óptimas para maximizar la precisión del alineamiento.

### Apartado a.

Este apartado consiste en la generación de alineamientos de secuencias de aminoácidos obtenidas aleatoriamente a partir de un alfabéto de aminoácidos.

#### Generación aleatoria de secuencias

Un objeto de la clase `RandomSequenceLoader`, el cual puede instanciarse haciendo uso del Factory Method con la clase `DataLoaderFactory`, permite la generación automática de cadenas aleatorias de aminoácidos, dado un alfabeto. Así, generar dos cadenas es tan fácil como ejecutar el código dado a continuación:

```python
sequenceLoader = DataLoaderFactory.get_loader("random")

sequence1 = sequenceLoader.load(50)
sequence2 = sequenceLoader.load(50)
```

el cual generará dos secuencias de 50 aminoácidos cada una. Una vez generadas, se puede realizar el alineamiento construyendo un objeto alineador, lo cual se puede hacer mediante la clase `AlignerBuilder`:

```python
aligner = AlignerBuilder().build(
                                AlignerArgs(
                                    match_score=3,
                                    mismatch_score=-1,
                                    target_internal_extend_gap_score=-3,
                                    target_internal_open_gap_score=-5
                                )
                            )
```
Lo que creará un alineador con los siguientes atributos:

```bash
AlignerArgs(match_score=3.0, 
                    mismatch_score=-1.0, 
                    target_internal_open_gap_score=-5.0, 
                    target_internal_extend_gap_score=-3.0, 
                    target_left_open_gap_score=0.0, 
                    target_left_extend_gap_score=0.0, 
                    target_right_open_gap_score=0.0, 
                    target_right_extend_gap_score=0.0, 
                    query_internal_open_gap_score=0.0, 
                    query_internal_extend_gap_score=0.0, 
                    query_left_open_gap_score=0.0, 
                    query_left_extend_gap_score=0.0, 
                    query_right_open_gap_score=0.0, 
                    query_right_extend_gap_score=0.0)
```

En caso de no pasarle unos argumentos al método `AlignerBuilder.build()`, se tomarán unos por defecto. Ahora sí, podemos alinear las dos secuencias de aminoácidos ejecutando el método `align` del objeto instanciado:

```python
alignments = aligner.align(sequence1, sequence2)
```

Para ver dichos alineamientos, podemos recorrerlos en un bucle for e ir imprimiendolos poco a poco.

```python
matches = []
scores = []

for i, alignment in enumerate(alignments):
    matches.append(get_matches(alignment))
    scores.append(alignment.score)
    print(f"Alignment {i}: Matches: {matches[-1]} - Score: {scores[-1]}")
    print(f"Alignment {i}: {alignment[0]}\nAlignment {i}: {alignment[1]}\n\n")
    
    if i >= 10:
        break
```

Para las secuencias

- CEVGESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
- QTCEYWSVIDFSSETCHFNMDWARHKDGWYSVNKEGWQRWYHSYMIQHLA

Se obtuvieron, por ejemplo, los siguientes alineamientos

```bash
Alignment 0: Matches: 11 - Score: 30.0
Alignment 0: GESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
Alignment 0: G-WYS-V-------NK-------------E----G---WQ---RW-Y


Alignment 1: Matches: 11 - Score: 30.0
Alignment 1: GESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
Alignment 1: GW-YS-V-------NK-------------E----G---WQ---RW-Y


Alignment 2: Matches: 11 - Score: 30.0
Alignment 2: GESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
Alignment 2: GWY-S-V-------NK-------------E----G---WQ---RW-Y
```

Los cuales se pueden mejorar bastante si se modifican los valores de penalización y recompensa del alineador.


#### Algoritmos genéticos

Con el objetivo de encontrar los valores de penalización y recompensa en el alineamiento que se le pasan al alineador mediante un objeto `AlignerArgs`, implementamos algoritmos genéticos. La idea es la siguiente:
1. Se dispone de una población incial, generalemente con unos 1200 alineadores.
2. A menuda que avanza el algoritmo, se produces cruces entre los elementos de la población generada en el instante anterior y, con una probabilidad de 0.1, se produce una mutación en la descendencia.
3. Al llegar a una iteración máxima, escogemos aquel individuo que presente un mayor número de coincidencias, con la esperanza de que este sea el individuo óptimo.

Este algoritmo puede implementarse fácilmente para dos secuencias haciendo uso de la clase `GeneticAlgorithm`

```python
geneticAlgorithm = GeneticAlgorithm(1200, 5, sequence1, sequence2, fitness_function)
aligners, best_aligner = geneticAlgorithm.run()
```

Donde `fitness_function` es una función que devuelve el número de coincidencias de las secuencias tras el alineamiento. Para las secuencias

- CEVGESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
- QTCEYWSVIDFSSETCHFNMDWARHKDGWYSVNKEGWQRWYHSYMIQHLA

Obtuvimos el siguiente alineamiento 

```bash
Matches: 40 - Score: 122.50782387273354
E--EK-----S-A--V-T--A-LWG--KV-N--V---D---E--VGG-E--A------LGRL---LVVYPWTQRFFESFGDLSTPDAVMGNPKV-KA-H-GKKV-L-GA-FSD-G-L---AH-LDNL-K-----GT-F---ATLSELH-----C--D-KLHVDPENF
EGVEKLMDIF-YAKI-RTHE-QL-GPI--FNGAVGIDDASWERH---KEKIAKFWKTML--LNENL--Y-------------------MGNP-VQ--PHI----NLL--PF-DI-KLFDV--WLD-LFKECLDQ--VFEEKA--SE-HFYEVACNI-AK------NF
```

Y el alineador que obtuvo dicho resultado tenía los siguiente valores de puntuación

```bash
Best aligner: AlignerArgs(match_score=9.948647681109431, 
                    mismatch_score=-9.533337651215863, 
                    target_internal_open_gap_score=-0.5626935077836481, 
                    target_internal_extend_gap_score=-1.3224425395624184, 
                    target_left_open_gap_score=-6.51439919407234, 
                    target_left_extend_gap_score=-6.198810320244487, 
                    target_right_open_gap_score=-8.45221923577287, 
                    target_right_extend_gap_score=-1.9226450171121012, 
                    query_internal_open_gap_score=-7.728482601267625, 
                    query_internal_extend_gap_score=-1.1109554998452031, 
                    query_left_open_gap_score=-3.790308498217315, 
                    query_left_extend_gap_score=-0.10826586286379447, 
                    query_right_open_gap_score=-7.031120693617138, 
                    query_right_extend_gap_score=-3.4951787092206086)
```

En cuanto a la población obtenida en la última iteración del algoritmo, cada uno de los alineadores presentaba un número un número de score diferente. Si graficamos los scores obtenidos, obtenemos una distribución como la que se muestra en la Figura 6.

<div align="center">
    <img src="images/dens_ej_2.png" alt="Scores" />
      <p><strong>Figura 6.</strong>Distribución de los scores obtenidos.</p>
</div>

Además, podemos representar cómo fueron los valores de match_score y mismatch_score, entre otros, que dieron lugar a los distintos scores. Para ello, representamos para cada cuartil de los scores los valores de match_score, mismatch_score, target_internal_open_gap_score y target_internal_extend_gap_score que dieron lugar a dichos scores. La Figura 7 muestra cómo se distribuyen estos valores.

<div align="center">
    <img src="images/dens_vals_ej2.png" alt="Boxplot" />
      <p><strong>Figura 7.</strong>Boxplot de los valores de los parámetros en función de los scores.</p>
</div>

En cuando al número de coincidencias, la Figura 8 muestra cómo se distribuyen los valores de coincidencias en función de los scores obtenidos.

<div align="center">
    <img src="images/dens_matches_ej2.png" alt="Boxplot" />
      <p><strong>Figura 8.</strong>Boxplot de las coincidencias en función de los scores.</p>
</div>

#### Alineamineto con matrices de puntuación

En este apartado, se han usado una serie de matrices de puntuación para alinear las secuencias de aminoácidos. Para ello, basta con pasarle la matriz de puntuación deseada al método `align` del objeto `Aligner`. Por ejemplo, para alinear las secuencias

- CEVGESTSHVHSIIESWNKNAMMGVMLQCQVAETYHFGTQSWQCFLEWPY
- QTCEYWSVIDFSSETCHFNMDWARHKDGWYSVNKEGWQRWYHSYMIQHLA

usando la matriz de puntuación `blosum62`, basta con ejecutar el siguiente código

```python
aligner = AlignerBuilder().build()
alignments = aligner.align(sequence1, sequence2, matrix="blosum62")
```

Además, podemos crear una matriz propia desde cero, guardando esta en un archivo y pasándole la ruta de dicho archivo al método `substitution_matrices.read`. En nuestro caso, dado que la matriz se encuentra en `data/MATRIX`, el código sería el siguiente

```python
matrix = substitution_matrices.read("data/MATRIX")
``` 

Ahora, podemos pasarle esta matriz al alineador de la forma

```python
aligner = AlignerBuilder().build()
alignments = aligner.align(sequence1, sequence2, matrix=matrix)
```

Igual que ocurría cuando usabamos las matrices que venían por defecto.

Las matrices ofrecias por BioPython utilizadas son las mostradas en la Figura 9.

<div align="center">
    <img src="images/matrices.png" alt="Matrices" />
      <p><strong>Figura 9.</strong>Matrices de puntuación utilizadas.</p>
</div>

Y la matriz personalizada no es más que una variación que hemos hecho de la matriz `dayhoff`, en la cual hemos activada la diagonal invertida, poniendo la mayoría de sus valores mayores que 1. La figura 10 muestra cómo es esta matriz con respecto a la matriz `dayhoff`.

<div align="center">
    <img src="images/pers_matrix.png" alt="Dayhoff" />
      <p><strong>Figura 10.</strong>Matriz de puntuación `dayhoff`.</p>
</div>

### Apartado b.

En lugar de generar secuencias aleatorias, ¿qué pasaría si usasemos secuencias de aminoácidos correspondientes a proteínas reales? Pues eso comprobamos en este apartado. Primeramente, probamos para las proteínas con identificadores ABG47031 y AUJ50941, correspondientes con la hemoglobina en diferentes organismos.

Con algoritmos genéticos, se obtiene algo bastante similar al ejercicio anterior. Claramente, por tratarse de proteínas reales, formadas por secuencias de aminoácidos más amplias, el número de coincidencias es mayor. Sin embargo, se sigue apreciando la relación entre las coincidencias y los scores obtenidos. Además, a mayor score, mayor puntuación se le da a los valores de match_score, como se puede ver en la Figura 11.

<div align="center">
    <img src="images/dens_vals_b_ej2.png" alt="Scores" />
      <p><strong>Figura 11.</strong>Distribución de los valores de puntuación en función del score.</p>
</div>

