import json


def obtener_alumnos():
    estudiantes = []
    try:
        archivo = open("Estudiantes.prn", mode="r")
        if archivo.readable():
            for est in archivo.read().split("\n"):
                if len(est) > 0:
                    estudiantes.append((est[0:8], est[8:]))
        archivo.close()
    except FileNotFoundError as ex:
        print("El archivo alumnos no existe: ", ex)
    return estudiantes


def obtener_materias():
    kardex = []
    try:
        archivo = open("Kardex.txt", mode="r")
        if archivo.readable():
            for kar in archivo.read().split("\n"):
                if len(kar) > 0:
                    datos = kar.split("|")
                    kardex.append((datos[0], datos[1], datos[2]))
        archivo.close()
    except FileNotFoundError as ex:
        print("El archivo kardex no existe: ", ex)
    except IOError as ioex:
        print("El archivo kardex tuvo un error: ", ioex)
    return kardex


def obtener_alumnos_por_nocontrol(*args):
    datos = []
    estudiantes = obtener_alumnos()
    materias = obtener_materias()
    archivo = open("Resultado.txt", mode="w")

    if len(args) > 0:
        for no_control in args:
            materias_alumno = []
            datos_alumno = {}
            for i in range(0, len(estudiantes)):
                if estudiantes[i][0] == no_control:
                    for j in range(0, len(materias)):
                        if materias[j][0] == no_control:
                            materias_alumno.append(materias[j][1])
                    datos_alumno = {"Nombre": estudiantes[i][1], "Materias": materias_alumno}
                    break
            datos.append(datos_alumno)
    else:
        for i in range(0, len(estudiantes)):
            materias_alumno = []
            for j in range(0, len(materias)):
                if materias[j][0] == estudiantes[i][0]:
                    materias_alumno.append(materias[j][1])
            datos.append({"Nombre": estudiantes[i][1], "Materias": materias_alumno})

    print("El archivo json es el siguiente:\n", json.dumps(datos))
    archivo.write(json.dumps(datos))


obtener_alumnos_por_nocontrol()
