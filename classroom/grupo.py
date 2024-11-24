from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, estudiantes=None, grupo="grupo ordinado", asignaturas=None):
    if estudiantes is None:
        estudiantes = []
    self._grupo = grupo
    self._Asignatura = Asignatura if Asignatura is not None else []
    self.listadoAlumnos = estudiantes


    def listadoAsignaturas(self, kwargs):
        for nombre, salon in kwargs.items():
            self._asignaturas.append(Asignatura(nombre, salon))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos.extend(lista)

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

if __name__ == "__main__":
    Asignatura1 = Asignatura("Matematicas")
    print(Asignatura1)

    grupo = Grupo(estudiantes=[], grupo="grupo predeterminado")
    print(grupo)

    Grupo.asignarNombre("Grado 12")
    print(Grupo.grado)

    grupo.agregarAlumno("Kelly")
    print(grupo.listadoAlumnos)

    grupo.agregarAlumno("Jaime", ["Pedro", "Santiago"])
    print(grupo.listadoAlumnos)

    grupo.agregarAlumno("Javier")
    print(grupo.listadoAlumnos)

    print(len(grupo.listadoAlumnos))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)

    Grupo.asignarNombre("Grado 6")
    print(Grupo.grado)
