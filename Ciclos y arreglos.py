NUEN=int(input("Introduzca su numero de entrenamientos:"))
i=1
def maxHR(age):
     return 208-0.7*age
age=int(input('Enter your age: '))
while i <= NUEN:
    FC=int(input('Enter your Frecuencia cardiaca:'))
    FCM = maxHR(age)
    if FC<0.5*FCM:
        Zona = "su frecuencia cardiaca no esta en una zona de trabajo"
    elif FC >=0.5*FCM and FC < 0.6*FCM:
        Zona = "Z1"
    elif FC >=0.6*FCM and FC <0.7*FCM:
        Zona = "Z2"
    elif FC >=0.70*FCM and FC <0.8*FCM:
        Zona = "Z3"
    elif FC >=0.8*FCM and FC <0.9*FCM:
        Zona = "Z4"
    elif FC >=0.9*FCM and FC < FCM:
        Zona = "Z5"
    else:
        Zona = "su frecuencia cardiaca no esta en una zona de trabajo"

    print("En el entrenamiento:", i, "tu zona de trabajo es:", Zona)

    i+=1
#Julian Trujillo
#Nicol Garcia
#Vivian Montoya
#Carlos Sanchez