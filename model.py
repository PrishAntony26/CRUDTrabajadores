from entity import *
from io import open
from os.path import exists
from os import remove, rename
 
class TrabajadorArchivo:
    #constructor
    def __init__(self):
        self.__archivo = "Trabajador.txt"
        self.__temporal = "TemporalTrabajador.txt"
        # validar si el archivo existe
        if not exists(self.__archivo):
            fichero = open(self.__archivo, "w")
            fichero.close()
            print("Archivo creado con exito!")
    # end def

    def adicionar(self, trabajo):
        fichero = None
        ok = False
        try:
            # abrir archivo para adicionar
            fichero = open(self.__archivo, "a")
            # preparar dato a escribir
            datos = trabajo.codigo+";"+trabajo.nombre+";" + \
                trabajo.fecha+";"+trabajo.cargo+";"+trabajo.area+";"+str(trabajo.sueldo)+"\n"
            # validar codigo de trabajador
            tr = self.buscar(trabajo.codigo)
            if tr == None:
                # Si no existe el trabajador
                fichero.write(datos)
            else:
                ok = True
        except IOError as e:
            print("Error : ", e)
        finally:
            fichero.close()
        return ok
    

    def actualizar(self, trabajo):
        fuente = None
        destino = None
        try:
            # abrir archivo alumos.txt para lectura
            fuente = open(self.__archivo, "r", encoding="utf8")
            # abre archivo temporal.txt para escritura
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = ";"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == trabajo.codigo:
                    datos = trabajo.codigo+";"+trabajo.nombre+";" + \
                    trabajo.fecha+";"+trabajo.cargo+";"+trabajo.area+";"+str(trabajo.sueldo)+"\n"
                    # escribir datos en el achivo tempotal.txt
                    destino.write(datos)  # aqui actualiza
                else:
                    destino.write(linea) # no se actualiza nada 
        except IOError as e:
            print("Error : ", e)
        finally:
            fuente.close()
            destino.close()
        # borrar archivo alumnos.txt y renombrar archivo temporal.txt
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)

    # end def

    def eliminar(self, trabajo):
        fuente = None
        destino = None
        try:
            # abrir archivo Trabajador.txt para lectura
            fuente = open(self.__archivo, "r", encoding="utf8")
            # abre archivo Trabajador.txt para escritura
            destino = open(self.__temporal, "w", encoding="utf8")
            lineas = fuente.readlines()
            separador = ";"
            for linea in lineas:
                dato = linea.split(separador)
                if dato[0] == trabajo.codigo:
                    pass
                else:
                    destino.write(linea)
        except IOError as e:
            print("Error : ", e)
        finally:
            fuente.close()
            destino.close()
        # borrar archivo Trabajador.txt y renombrar archivo TemporalTrabajador.txt
        remove(self.__archivo)
        rename(self.__temporal, self.__archivo)
    
    #end def
        

    def listar(self):
        fichero = None
        trabajadores = []
        try:
            fichero = open(self.__archivo, "r", encoding="utf8")
            lineas = fichero.readlines()
            for linea in lineas:
                campos = linea.replace("\n", "").split(";")
                trabajador = {
                    "codigo": campos[0], "nombre": campos[1], "fecha": campos[2], "cargo": campos[3], "area": campos[4], "sueldo": campos[5]}
                # agregar alumno a la lista alumnos
                trabajadores.append(trabajador)
        except IOError as e:
            print("Error : ", e)
        finally:
            fichero.close()
        return trabajadores
    

    def buscar(self, trabajo):
        fichero = None
        tr = None
        try:
            fichero = open(self.__archivo, "r", encoding="utf8")
            lineas = fichero.readlines()
            for linea in lineas:
                campos = linea.split(";")
                cod = campos[0]
                if cod == trabajo:
                    tr = campos
                    break
        except IOError as e:
            print("Error : ", e)
        finally:
            fichero.close()
        return tr