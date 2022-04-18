
from controller import *
from entity import *

class Prueba:
    #crear objeto de la clase alumno
    tr=Trabajador("E002","Antony","27/10/1999","Ingeniero","asd","2000")
    #crear objeto de la clase alumnocontroller
    obj=TrabajadorController()
    # registrar alumno
    msg=obj.procesarTrabajador(tr,1)
    print(msg)
    
#end class


# prueba de la clase prueba
p=Prueba()