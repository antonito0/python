from alumno import Alumno

class Curso:
    def __init__ (self):
        self.alumnos = []

    def anadir (self, alumno):
        self.alumnos.append(alumno)

    def mejor (self):
        if not self.alumnos:
            return None
        mejor = None
        for i in self.alumnos:
            if mejor is None or mejor.media() < i.media():
                mejor = i
        return mejor

    def aprobados (self):
        aprobados = []
        for a in self.alumnos:
            if a.media() >= 5:
                aprobados.append(a)
        return aprobados

    def guardar(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            for a in self.alumnos:
                notas = ",".join(str(n) for n in a.notas)
                f.write(f"{a.nombre};{notas}\n")

    def cargar(self, ruta):
        self.alumnos = []
        with open(ruta, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                nombre, _, notas = linea.partition(";")
                alumno = Alumno(nombre)
                for n in notas.split(","):
                    if n:
                        alumno.anotar(float(n))
                self.alumnos.append(alumno)

    def __str__ (self):
        return f"{self.alumnos}"