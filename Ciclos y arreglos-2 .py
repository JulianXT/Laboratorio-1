NUEN=int(input("Introduzca su numero de entrenamientos:"))
i=1
def maxHR(age):
     return 208-0.7*age
age=int(input('Enter your age: '))

Z1=0
Z2=0
Z3=0
Z4=0
Z5=0
while i <= NUEN:
    FC=int(input('Enter your Frecuencia cardiaca en la zona '+ str(i)+":"))
    FCM = maxHR(age)
    if FC<0.5*FCM:
        Zona = "su frecuencia cardiaca no esta en una zona de trabajo"
    elif FC >=0.5*FCM and FC < 0.6*FCM:
        Zona = "Z1"
        Z1+= 1
    elif FC >=0.6*FCM and FC <0.7*FCM:
        Zona = "Z2"
        Z2+=1
    elif FC >=0.70*FCM and FC <0.8*FCM:
        Zona = "Z3"
        Z3+=1
    elif FC >=0.8*FCM and FC <0.9*FCM:
        Zona = "Z4"
        Z4+=1
    elif FC >=0.9*FCM and FC < FCM:
        Zona = "Z5"
        Z5+=1
    else:
        Zona = "su frecuencia cardiaca no esta en una zona de trabajo"
    print("En el entrenamiento:", i, "tu zona de trabajo es:", Zona)
    i+=1

print("Hay",Z1, "entrenamientos en la zona 1, ",
    Z2, "entrenamientos en la zona 2, ",
    Z3, "entrenamientos en la zona 3, ",
    Z4, "entrenamientos en la zona 4, ",
    Z5, "entrenamientos en la zona 5, ")    

Zonas=[Z1, Z2, Z3, Z4, Z5]
i=0
while i < 5:
    Porcentaje= ((Zonas[i]/NUEN)*100)
    i+=1
    print("El porcentaje de entrenamientos en la zona",i,"es de",Porcentaje,"%")
    

