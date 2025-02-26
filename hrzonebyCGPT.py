def calcular_zonas_fc(edad, fc_entrenamiento):
    # Cálculo de la FC máxima según la fórmula clásica
    fc_max = 220 - edad
    
    # Definición de los rangos de zonas
    zonas = {
        "Z1 (Recuperación)": (0.5 * fc_max, 0.6 * fc_max),
        "Z2 (Resistencia)": (0.6 * fc_max, 0.7 * fc_max),
        "Z3 (Aeróbica)": (0.7 * fc_max, 0.8 * fc_max),
        "Z4 (Anaeróbica)": (0.8 * fc_max, 0.9 * fc_max),
        "Z5 (Máxima)": (0.9 * fc_max, fc_max)
    }
    
    # Determinar la zona correspondiente
    for zona, (lim_inf, lim_sup) in zonas.items():
        if lim_inf <= fc_entrenamiento <= lim_sup:
            return zona
    
    return "Fuera de rango"

# Solicitar entrada al usuario
try:
    edad = int(input("Ingrese su edad: "))
    fc_entrenamiento = int(input("Ingrese su frecuencia cardíaca durante el entrenamiento: "))
    
    zona = calcular_zonas_fc(edad, fc_entrenamiento)
    print(f"Su zona de entrenamiento es: {zona}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
    
#Julian Trujillo
#Nicol Garcia
#Vivian Montoya
#Carlos Sanchez
