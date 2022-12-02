class Alumno:#clase, entidad, modelo
    def __init__ (self, id , nombre,  email):#constructor
        self.id=id#almacenar en la instancia el parámetro
        self.nombre=nombre#string
        self.email=email#string
    def infoAlumno(self):#método de instancia
        print(f'el alumno {self.nombre} con email: {self.email}')

alumno1=Alumno(1, 'Mario Gómez', 'mario_28@gmail.com')
alumno2=Alumno(2, 'Carla Sánchez', 'carlaminor@gmail.com')
alumno3=Alumno(3, 'Carlos Moreno', 'carlos_natacion@hotmail.com')
alumno1.infoAlumno()
alumno2.infoAlumno()
alumno3.infoAlumno()
