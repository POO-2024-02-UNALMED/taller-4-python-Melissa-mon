from classroom.asignatura import Asignatura

class Asignatura:

    def __init__(self, nombre, salon):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return f"{self._nombre} {self._salon}"


class Grupo:
    grado = None

    def __init__(self, estudiantes, grupo="grupo ordinado", asignaturas=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
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
    # Crear una asignatura e imprimirla
    Asignatura1 = Asignatura("Matematicas", "remoto")
    print(Asignatura1)  # Matematicas remoto

    # Crear un grupo de estudiantes e imprimirlo
    grupo = Grupo(estudiantes=[], grupo="grupo predeterminado")
    print(grupo)  # Grupo de estudiantes: grupo predeterminado

    # Asignar nombre de grado y mostrarlo
    Grupo.asignarNombre("Grado 12")
    print(Grupo.grado)  # Grado 12

    # Agregar estudiantes al grupo e imprimir el listado
    grupo.agregarAlumno("Kelly")
    print(grupo.listadoAlumnos)  # ['Kelly']

    grupo.agregarAlumno("Jaime", ["Pedro", "Santiago"])
    print(grupo.listadoAlumnos)  # ['Jaime', 'Pedro', 'Santiago']

    grupo.agregarAlumno("Javier")
    print(grupo.listadoAlumnos)  # ['Jaime', 'Pedro', 'Santiago', 'Javier']

    # Imprimir el número de estudiantes
    print(len(grupo.listadoAlumnos))  # 4

    # Asignar un nuevo grado y mostrarlo
    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)  # Grado 1

    Grupo.asignarNombre("Grado 6")
    print(Grupo.grado)  # Grado 6
