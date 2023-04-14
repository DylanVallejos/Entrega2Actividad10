nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
quitar= ";.\n\'"
for caracter in quitar:
    nombres= nombres.replace(caracter,"")
nombres=nombres.split(",")
# Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items#
def generar_Estructura(nombre,nota1,nota2):
    dicc_alumnos={}
    for n,n1,n2 in zip(nombre,nota1,nota2):
         dicc_alumnos[n]=(n1,n2)
    return(dicc_alumnos)
nuevo_dicc=generar_Estructura(nombres,notas_1,notas_2)
print("*" *100)
print(nuevo_dicc)


#Calcular el promedio de notas de cada estudiante
def prom_cada_alumno():
    dicc_alumnos_promedio={}
    for n,n1,n2 in zip(nombres,notas_1,notas_2):
     dicc_alumnos_promedio[n]=(n1+n2)/2
    return dicc_alumnos_promedio
promedios_alumnos=prom_cada_alumno()
print("*" *100)
print(promedios_alumnos)

## Calcular el promedio general del curso
def promedio_general(promedio_alumno):
    suma=0
    for nb,nt in promedios_alumnos.items():
        suma=suma+nt
    prom_gen=suma/len(nombres)
    print('El promedio general del curso es: ',suma/len(nombres))

##Identificar al estudiante con la nota promedio más alta.
def maximo(promedios_alum):
    print ('El estudiante con la nota promedio mas alta es:',max(promedios_alum, key=promedios_alum.get))
#Identificar al estudiante con la nota más baja

def minimo(prome_alum):
    print ('El estudiante con nota mas baja es: ',min(prome_alum, key=prome_alum.get))
promedio_general(promedios_alumnos)
maximo(promedios_alumnos)
minimo(nuevo_dicc)

