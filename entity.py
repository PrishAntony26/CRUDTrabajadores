#Creacion de clase

class Trabajador:
    
    def __init__(self,codigo,nombre,fecha,cargo,area,sueldo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha = fecha
        self.__cargo = cargo
        self.__area = area
        self.__sueldo = sueldo 
        
    #getter
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def cargo(self):
        return self.__cargo
    
    @property
    def area(self):
        return self.__area
    
    @property
    def sueldo(self):
        return self.__sueldo
    
    #setter
    @codigo.setter 
    def codigo(self,codigo):
        self.__codigo=codigo
        
    @nombre.setter 
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @fecha.setter 
    def fecha(self,fecha):
        self.__fecha=fecha

    @cargo.setter 
    def cargo(self,cargo):
        self.__cargo=cargo
        
    @area.setter 
    def area(self,area):
        self.__area=area
        
    @sueldo.setter 
    def sueldo(self,sueldo):
        self.__sueldo=sueldo