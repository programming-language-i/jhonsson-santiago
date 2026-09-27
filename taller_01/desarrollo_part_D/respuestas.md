1 °Consultar el precio de 30 productos en 30 APIs distintas: Hilos, porque el programa pasa la mayor parte del tiempo en espera de las respuestas de red (I/O-bound).

2 °Contar las palabras palíndromas de 10 libros ya cargados en memoria: Procesos, porque requiere un uso intensivo del procesador para analizar texto (calcula / CPU-bound).

3 °Un servidor de chat que atiende 15 clientes conectados: Hilos, porque el servidor gestiona múltiples conexiones concurrentes de red basadas en espera de mensajes (I/O-bound).

4 °Aplicar un filtro de desenfoque a 200 fotos, píxel por píxel, en Python puro: Procesos, porque exige cálculos matemáticos pesados en los núcleos del procesador (calcula / CPU-bound).

5 °Leer 50 archivos de log del disco y copiarlos a otra carpeta: Hilos, porque la limitante principal es la espera de las operaciones de lectura y escritura en disco (I/O-bound).

6 °Simular 1.000.000 de lanzamientos de dados en 8 lotes y promediar: Procesos, porque demanda un esfuerzo numérico y lógico constante del procesador (calcula / CPU-bound).