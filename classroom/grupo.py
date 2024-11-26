from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def _init_(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        listaI = []
        listaI.append(alumno)
        self.listadoAlumnos += lista + listaI

    def _str_(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre