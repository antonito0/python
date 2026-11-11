from alumno import Alumno
from curso import Curso

'''
alumno1 = Alumno("unai")
alumno2 = Alumno("irene")

alumno1.anotar(7)
alumno1.anotar(8)
alumno2.anotar(6)

curso = Curso()

curso.anadir(alumno1)
curso.anadir(alumno2)

for i in curso.alumnos:
    print(i)

curso.guardar("alumnos.txt")
'''

curso = Curso()
curso.cargar("alumnos.txt")
for i in curso.alumnos:
    print(i)
