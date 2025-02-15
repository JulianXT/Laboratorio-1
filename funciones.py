def FCM(age):                 #calcula la frecuencia cardíaca máxima
    return 207-0.7*age

def RZ2(age):                  #calcula el rango de Z2
    return (0.6 * FCM(age), 0.7 * FCM(age))

def calcular_promedio(lista):    #calcula el promedio de las frecuencias cardiacas ingresadas
    return sum(lista) / len(lista) if lista else 0  # Evita división por cero


entrenamientos=[]

i=1
age= int(input("ingrese su edad: "))
NENT= int(input("ingrese el numero de entrenamientos: "))

while i<=NENT:
    FC=int(input("ingrese su frecuencia cardiaca: "))
    entrenamientos.append(FC)
    FCMX=FCM(age)
    RangoZ2bajo,Rangoz2alto= RZ2(age)
    if FC < 0.5 * FCMX:
        Zona = "su frecuencia cardiaca no está en una zona de trabajo"
    elif FC < 0.6 * FCMX:
        Zona = "Z1"
    elif FC < 0.7 * FCMX:
        Zona = "Z2"
    elif FC < 0.8 * FCMX:
        Zona = "Z3"
    elif FC < 0.9 * FCMX:
        Zona = "Z4"
    elif FC < FCMX:
        Zona = "Z5"
    else:
        Zona = "su frecuencia cardiaca no está en una zona de trabajo"
    print(f"En el entrenamiento {i}, tu zona de trabajo es: {Zona}") 
    i+=1
    
PMDUS=calcular_promedio(entrenamientos)
print(f"su promedio de ritmos cardiacos es de {PMDUS:.2f} bpm")

if RangoZ2bajo <= PMDUS <= Rangoz2alto:
    print("Tu promedio está dentro de la zona Z2")
else:
    print("Tu promedio no está en Z2, Ajusta la intensidad del entrenamiento.")