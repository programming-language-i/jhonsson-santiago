import multiprocessing

def calcular(n, lista_compartida):
    # Añadimos el resultado a la lista compartida kis para procesos
    #ya que en las lienas originales se confuncia una lista vacia con una appen en lugar de un hilo el cual 
    #confuncia los procesos 
    lista_compartida.append(n * n)

if __name__ == "__main__":
    # en este caso se utiliza un Manager para crear una lista compartida entre procesos
    with multiprocessing.Manager() as manager:
        resultados = manager.list()
        
        procesos = [
            multiprocessing.Process(target=calcular, args=(n, resultados)) 
            for n in range(4)
        ]
        
        for p in procesos:
            p.start()
        for p in procesos:
            p.join()
            
        # Ahora sí se imprimen los datos recolectados ya que este es un proceso de concurrencia
        print(list(resultados))