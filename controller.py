
from model import *
from entity import *
from util import *

class TrabajadorController:
    #constructor
    def __init__(self):
        #crear objeto de la clase alumnofile
        self.__obj=TrabajadorArchivo()

    #metodos de negocio
    def listaTrabajador(self):
        return self.__obj.listar()

    def buscarTrabajador(self,id):
        return self.__obj.buscar(id)

    def procesarTrabajador(self,tr,opcion):
        self.__msg=None
        if opcion==ADD:
            ok=self.__obj.adicionar(tr)
            if ok==False:
                self.__msg="Trabajador registrado con exito!"
            else:
                self.__msg="Codigo de Trabajador ya existe!"
        if opcion==UPD:
            self.__obj.actualizar(tr)
            self.__msg="Trabajador actualizado con exito!"
        if opcion==DEL:
            self.__obj.eliminar(tr)
            self.__msg="Trabajador eliminado con exito!"
        return self.__msg

#end class