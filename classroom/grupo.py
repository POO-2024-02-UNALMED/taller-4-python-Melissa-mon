from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, estudiantes=None, grupo="grupo ordinado", asignaturas=None):
        if estudiantes is None:
            estudiantes = []  # Si no se pasa estudiantes, usar una lista vacía.
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, kwargs.items()):
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