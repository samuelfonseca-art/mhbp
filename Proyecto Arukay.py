plantas_completas = {
    "rosa": {
        "agua_ml_dia": 500,
        "luz_horas_dia": 7,
        "composta_g_mes": 50,
        "pisos_termicos": "templado (1800-2500.)",
        "clima": "templado, fresco",
        "distancia_plantar_m": 0.3
    },
    "albahaca": {
        "agua_ml_dia": 300,
        "luz_horas_dia": 6,
        "composta_g_mes": 20,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 0.25
    },
    "cactus": {
        "agua_ml_dia": 100,
        "luz_horas_dia": 5,
        "composta_g_mes": 10,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "árido, seco",
        "distancia_plantar_m": 0.4
    },
    "papa": {
        "agua_ml_dia": 800,
        "luz_horas_dia": 6,
        "composta_g_mes": 70,
        "pisos_termicos": "templado (2000-3000.)",
        "clima": "templado, fresco",
        "distancia_plantar_m": 0.4
    },
    "maiz": {
        "agua_ml_dia": 600,
        "luz_horas_dia": 8,
        "composta_g_mes": 60,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 0.5
    },
    "caña de azucar": {
        "agua_ml_dia": 900,
        "luz_horas_dia": 8,
        "composta_g_mes": 80,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 1.0
    },
    "yuca": {
        "agua_ml_dia": 700,
        "luz_horas_dia": 7,
        "composta_g_mes": 50,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 1.0
    },
    "platano": {
        "agua_ml_dia": 850,
        "luz_horas_dia": 7,
        "composta_g_mes": 65,
        "pisos_termicos": "bajo (0-1500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 3.0
    },
    "cafe": {
        "agua_ml_dia": 500,
        "luz_horas_dia": 5,
        "composta_g_mes": 40,
        "pisos_termicos": "templado (1200-1800.)",
        "clima": "templado, húmedo",
        "distancia_plantar_m": 2.0
    },
    "cacao": {
        "agua_ml_dia": 600,
        "luz_horas_dia": 6,
        "composta_g_mes": 45,
        "pisos_termicos": "bajo (0-800.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 3.0
    },
    "aguacate": {
        "agua_ml_dia": 700,
        "luz_horas_dia": 6,
        "composta_g_mes": 55,
        "pisos_termicos": "templado (1500-2500.)",
        "clima": "templado, húmedo",
        "distancia_plantar_m": 5.0
    },
    "clavel": {
        "agua_ml_dia": 400,
        "luz_horas_dia": 7,
        "composta_g_mes": 35,
        "pisos_termicos": "templado (1800-2500.)",
        "clima": "templado, fresco",
        "distancia_plantar_m": 0.3
    },
    "crisantemo": {
        "agua_ml_dia": 450,
        "luz_horas_dia": 6,
        "composta_g_mes": 40,
        "pisos_termicos": "templado (1800-2500.)",
        "clima": "templado, fresco",
        "distancia_plantar_m": 0.4
    },
    "orquidea": {
        "agua_ml_dia": 350,
        "luz_horas_dia": 5,
        "composta_g_mes": 30,
        "pisos_termicos": "templado (1200-2000.)",
        "clima": "templado, húmedo",
        "distancia_plantar_m": 0.3
    },
    "palma de aceite": {
        "agua_ml_dia": 1000,
        "luz_horas_dia": 8,
        "composta_g_mes": 90,
        "pisos_termicos": "bajo (0-500.)",
        "clima": "cálido, húmedo",
        "distancia_plantar_m": 9.0
    },
    "cebada": {
        "agua_ml_dia": 550,
        "luz_horas_dia": 7,
        "composta_g_mes": 45,
        "pisos_termicos": "templado (2000-3000.)",
        "clima": "templado, fresco",
        "distancia_plantar_m": 0.25
    },
}

def buscar_planta(nombre):
    nombre = nombre.lower().strip()
    if nombre in plantas_completas:
        datos = plantas_completas[nombre]
        return (f"Información para '{nombre.title()}':\n"
                f"  Agua necesaria: {datos['agua_ml_dia']} ml por día\n"
                f"  Luz solar: {datos['luz_horas_dia']} horas por día\n"
                f"  Composta necesaria: {datos['composta_g_mes']} gramos por mes\n"
                f"  Pisos térmicos recomendados: {datos['pisos_termicos']}\n"
                f"  Tipo de clima: {datos['clima']}\n"
                f"  Distancia recomendada para plantar: {datos['distancia_plantar_m']} metros\n")
    else:
        return f"No tengo informacion para '{nombre}'. Intenta con otro nombre."

def main():
    print("Calculadora de plantas")
    print("Tenemos: rosa,albahaca,cactus,papa,maiz,caña de azucar,yuca,platano,cafe,caco,aguacate,clavel,crisanteno,orquidea,palma de aceite,cebada")
    while True:
        planta = input("Ingresa el nombre del cultivo(escribe 'salir' para terminar): ")
        if planta.lower() == "salir":
            print("¡Hasta luego!")
            break
        print(buscar_planta(planta))

if __name__ == "__main__":
    main()