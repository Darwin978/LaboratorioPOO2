import Estudiante

def buscarMatricula(estudiante, matricula):
    try:
        dic = Estudiante.devolverMaterias(estudiante)
        if matricula in dic:
            print('True')
            return True
        else:
            print('False')
            return False
    except KeyError as e:
        print("NO SE HA ENCONTRADO CORRELACIÓN ENTRE EL ESTUDIANTE Y LA MATERIA", e)
    
buscarMatricula('Darwin', 'POO')