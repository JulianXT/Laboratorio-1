def maxHR(age):
    return 208 - 0.7 * age

def calcular_zona(FC, FCM):
    zonas = [(0.5, "Z1"), (0.6, "Z2"), (0.7, "Z3"), (0.8, "Z4"), (0.9, "Z5")]
    for limite, zona in zonas:
        if FC < limite * FCM:
            return zona
    return "Z5" if FC < FCM else "Fuera de zona"

def main():
    NUEN = int(input("Introduzca su número de entrenamientos: "))
    age = int(input("Ingrese su edad: "))
    
    zonas_contador = {"Z1": 0, "Z2": 0, "Z3": 0, "Z4": 0, "Z5": 0}
    
    for i in range(1, NUEN + 1):
        FC = int(input(f"Ingrese la frecuencia cardíaca promedio del entrenamiento {i}: "))
        FCM = maxHR(age)
        zona = calcular_zona(FC, FCM)
        
        if zona in zonas_contador:
            zonas_contador[zona] += 1
        
        print(f"En el entrenamiento {i}, tu zona de trabajo es: {zona}")
    
    print("\nPorcentaje de entrenamientos en cada zona:")
    for zona, cantidad in zonas_contador.items():
        porcentaje = (cantidad / NUEN) * 100
        print(f"{zona}: {porcentaje:.2f}%")

if __name__ == "__main__":
    main()
