class Alumno:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.notas = []

    def anotar (self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.notas.append(nota)

    def media (self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Nombre: {self.nombre} \nNotas: {self.notas}"