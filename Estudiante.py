diccionario = {'Darwin':['POO', 'Base de datos'],
               'Edwin': ['IA', 'Proyectos Tecnologicos']}

def devolverMaterias(estudiante):
    return diccionario.get(estudiante, "No se encontro el usuario")