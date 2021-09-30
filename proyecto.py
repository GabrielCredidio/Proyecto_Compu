#===========================
# em = evalua multiplicación
def em():

    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero:")
    resultado = int(num1) * int(num2)

    return resultado

multiplicacion = em()
print(multiplicacion)
#===========================
# es = evaluación suma
def es ():
 
    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero: ")
    resultado = int(num1) + int(num2)
    return resultado

suma = es()
print(suma)
#===========================
# ed = evaluación división
def ed ():
    
    num1 = input("Informar el primer numero: ")
    num2 = input("Informar el segundo numero: ")
    resultado = int(num1) / int(num2)
    return resultado

division = ed()
print(division)
#===========================
soluciones = ["d", "c", "c", "a"]
R=0
for i in soluciones:
    respuesta = input("Selecione las letras entre a, b, c, d: ")
    if respuesta ==1:
        R = R + 1
        print("La respuesta es correcta.", R, "puntos acumulados de",len(soluciones),"puntos.")
    elif respuesta != i:
        print("Respuesta incorrecta. La respuesta correcta era:", i)
#===========================   
R = int(input("Ingresa una calificación de Matematicas: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))
    
    
R = int(input("Ingresa una calificación de Espanol: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))
    
R = int(input("Ingresa una calificación Computacion: "))

while R < 70:
    R = int(input("Ingresa una calificación: "))
