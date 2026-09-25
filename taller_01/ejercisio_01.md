Parte A — Conceptos
Responder en una o dos líneas.

1 °Un programa atiende dos tareas alternando en un solo núcleo. ¿Es concurrencia, paralelismo o ambas?
es concurrencia ya que las tareas se alternan en un solo nucleo de trabajo el cual hace varias tareas 
sin ejecutarse de forma estrictamente simultanea 

2 °Nombrar dos diferencias entre un proceso y un hilo (memoria, costo, fallo).
en este caso es meomria ya que la memoria toma diferentesespacios de memoria, mientras 
que los hilos comparten esa misma memoria de su proceso principal

ademas de crear procesos es mas costoso que crear hilos ya que este gasta menos recursos del sistemas

3 °¿En qué estado del ciclo de vida está un hilo que ejecuta time.sleep(2)? ¿Qué devuelve is_alive()?
Está en estado bloqueado / dormido (sleeping), y el método is_alive() devuelve True porque el hilo sigue vivo aunque esté en pausa.

4 °¿Qué protege el GIL? ¿Evita las condiciones de carrera en los datos del programa?
protege las estructuras internas del intérprete de CPython, pero no evita las condiciones de carrera en las variables lógicas del usuario.

5 °¿Por qué 4 hilos que duermen 1 s cada uno tardan ~1 s en total y no ~0,25 s?
Porque los hilos operan de forma concurrente, permitiendo que los tiempos de espera de 1 segundo ocurran de manera simultánea en lugar de sumarse de forma secuencial.
(informcion tomada por gemini )

6 °Al crear un hilo por herencia, ¿qué método se sobrescribe y cuál nunca? ¿Por qué?
Se sobrescribe el método run() y nunca se sobrescribe start(), ya que este último se encarga de los procedimientos internos del sistema

7 °¿Qué pasa con un hilo daemon cuando termina el hilo principal? ¿Qué no se ejecuta?
El hilo daemon se detiene de forma abrupta e inmediata, por lo tanto cualquier instrucción restante dentro de su ciclo o bloque de cierre no llega a ejecutarse.

8 °Completar la regla del curso: hilos para , procesos para.
Hilos son para calcular proceos pesados del CPU y esta muy arraigado a los multiprocesos

