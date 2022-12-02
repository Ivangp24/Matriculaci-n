from curso import Curso
from alumno import Alumno

class Matricula:#clase, entidad, modelo
    def __init__(self, idmatricula, fechamatricula, idalumno, idcurso):#constructor
        self.idmatricula=idmatricula
        self.fechamatricula=fechamatricula
        self.idalumno=idalumno
        self.idcurso=idcurso
    def infoMatricula(self):#método de instancia
        print(f'Alumno: {self.idalumno}, matriculado en {self.idcurso}, el día {self.fechamatricula}')

alumno1=Alumno(1, 'Mario Gómez', 'mario_28@gmail.com')
carrera1=Curso(1,'Química',240,4)
alumno2=Alumno(2, 'Carla Sánchez', 'carlaminor@gmail.com')
carrera2=Curso(2,'Medicina',360,6)
alumno3=Alumno(3, 'Carlos Moreno', 'carlos_natacion@hotmail.com')
carrera3=Curso(3,'Física',240,4)
matricula1=Matricula(1, '12-09-2018', alumno1.nombre, carrera1.nombre )
matricula2=Matricula(2, '08/08/2019', alumno2.nombre, carrera2.nombre)
matricula3=Matricula(3, '03/10/2020', alumno2.nombre, carrera3.nombre)
matricula4=Matricula(4, '12/09/2022', alumno3.nombre, carrera3.nombre)
matricula1.infoMatricula()
matricula2.infoMatricula()
matricula3.infoMatricula()
