import threading, time

def sensor(numero, temperatura):
    print(f"{numero} sensor")

    for i in range(5):
        print(f"{numero} - {i + 1}: temperatura {temperatura} centigrados")

        time.sleep(1) 

    print("termino")

if __name__ == "__name__":
    thrreads = [
        threading.thread(target=sensor,args=("sensor 1", 30)),
        threading.thread(target=sensor,args=("sensor 2", 40)),
        threading.thread(target=sensor,args=("sensor 3", 50)),
        threading.thread(target=sensor,args=("sensor 4", 60)),
        threading.thread(target=sensor,args=("sensor 4", 70)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
            thread.join()

    print("finalizo proceso")