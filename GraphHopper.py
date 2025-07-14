import requests

API_KEY = "9f226800-0133-413f-ab60-410e63e1e468"


ciudades = {
    "santiago": (-33.4489, -70.6693),
    "valparaiso": (-33.0472, -71.6127),
    "puerto montt": (-41.4696, -72.9423),
    "buenos aires": (-34.6037, -58.3816),
    "mendoza": (-32.8908, -68.8272),
    "cordoba": (-31.4201, -64.1888)
}


transportes = {
    "auto": "car",
    "bicicleta": "bike",
    "peatonal": "foot"
}

def calcular_ruta(origen, destino, medio):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{ciudades[origen][0]},{ciudades[origen][1]}", f"{ciudades[destino][0]},{ciudades[destino][1]}"],
        "vehicle": transportes[medio],
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "paths" not in data:
        print("Error al obtener la ruta. Verifica tu API key o las ciudades.")
        return

    path = data["paths"][0]
    distancia_km = path["distance"] / 1000
    distancia_mi = path["distance"] / 1609.34
    tiempo_min = path["time"] / (1000 * 60)

    print(f"\nDistancia entre {origen.title()} y {destino.title()}: {distancia_km:.2f} km ({distancia_mi:.2f} millas)")
    print(f"Duración estimada en {medio}: {tiempo_min:.1f} minutos")

    print("\nInstrucciones del viaje:")
    for i, instruccion in enumerate(path["instructions"], 1):
        print(f"{i}. {instruccion['text']} ({instruccion['distance']:.1f} m)")

# Programa principal
while True:
    print("\nPlanificador de viaje entre ciudades de Chile y Argentina")
    origen = input("Ingrese ciudad de origen (o 's' para salir): ").strip().lower()
    if origen == "s":
        break

    destino = input("Ingrese ciudad de destino: ").strip().lower()
    if destino == "s":
        break

    if origen not in ciudades or destino not in ciudades:
        print("Ciudad no válida. Intente nuevamente.")
        continue

    print("Medios de transporte disponibles: auto, bicicleta, peatonal")
    medio = input("Ingrese medio de transporte: ").strip().lower()
    if medio not in transportes:
        print("Medio de transporte no válido. Intente nuevamente.")
        continue

    calcular_ruta(origen, destino, medio)

