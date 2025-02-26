FC=int(input('ingresa tu Frecuencia cardiaca:'))

age=int(input('Enter your age: '))

def maxHR(age):
    return 208-0.7*age
FCM = maxHR(age)

if FC<0.5*FCM:
    print("su frecuencia cardiaca no esta en una zona de trabajo")
elif FC >=0.5*FCM and FC < 0.6*FCM:
    print("Tu zona de trabajo es Z1")
elif FC >=0.6*FCM and FC <0.7*FCM:
    print("Tu zona de trabajo es Z2")
elif FC >=0.70*FCM and FC <0.8*FCM:
    print("Tu zona de trabajo es Z3")
elif FC >=0.8*FCM and FC <0.9*FCM:
    print("Tu zona de trabajo es Z4")
elif FC >=0.9*FCM and FC <FCM:
    print("Tu zona de trabajo es Z5")

