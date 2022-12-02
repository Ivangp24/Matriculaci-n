class Curso:#clase
    def __init__ (self, id , nombre,  creditos, añosestudio):
        self.id=id#almacenar en la instancia
        self.nombre=nombre#string
        self.creditos=creditos
        self.añosestudio=añosestudio
    def info(self):#método de instancia
        print(f'La carrera de {self.nombre}, tiene {self.creditos} creditos y dura {self.añosestudio} años')

carrera1=Curso(1,'Química',240,4)
carrera2=Curso(2,'Medicina',360,6)
carrera3=Curso(3,'Física',240,4)
carrera1.info()
carrera2.info()
carrera3.info()