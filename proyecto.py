EO(preguntas de 1-180, num1, num2)
 var = num1 + num2 + num3
 imprimir pregunta num1
 respuesta usuario pregunta 1 = a
 respuesta correcta pregunta 1 = d
 print(correcto respuesta d)
 print(incorrecto a,b,c)
EF(print var) promedio del examen

#===========================
# em = evalua multiplicación
def em():

    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero:")
    resultado = int(num1) * int(num2)

    return resultado

multiplicacion = em()
print(multiplicacion)
#==========================
# es = evaluación suma
def es ():
 
    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero: ")
    resultado = int(num1) + int(num2)
    return resultado

suma = es()
print(suma)
#==========================
# ed = evaluación división
def ed ():
    
    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero: ")
    resultado = int(num1) / int(num2)
    return resultado

division = ed()
print(suma)
#==========================

respuesta = input("Seleccione las letras entre a, b, c ó d: ")
R=0

R = int(input("Ingresa una calificación: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))

if respuesta == "a":
    R = R + 1
    print("respuesta 1 valor %i, es %r debe ser %r" % (a ,respuesta(a), True))

if respuesta == "b":
    respuesta = respuesta + 0
    print("respuesta 2 valor %i, es %r debe ser %r" % (c ,respuesta(c), False))

if respuesta == "c":
    respuesta = respuesta + 1
    print("respuesta 3 valor %i, es %r debe ser %r" % (b ,respuesta(b), True))

if respuesta == "d":
    respuesta = respuesta + 0
    print("respuesta 4 valor %i, es %r debe ser %r" % (d ,respuesta(d), False))

def evalua(respuesta_correcta, respuesta_usuario, evaluacion, muestra = 1):
    if respuesta == respuesta_usuario:
        evaluacion = evaluacion +1
    if muestra == 1:
        respuesta(respuesta_correcta, respuesta_usuario, evaluacion)
    return evaluacion 
  
def respuesta(respuesta_correcta, respuesta_usuario,evaluacion):
 
    print("Respuesta correcta.", respuesta)
    print("Respuesta:", respuesta_usuario)
    print("Evaluacion_en_linea:", evaluacion)
    
R = int(input("Ingresa una calificación de Matematicas: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))
    
    
R = int(input("Ingresa una calificación de Espanol: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))
    
R = int(input("Ingresa una calificación Computacion: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))

