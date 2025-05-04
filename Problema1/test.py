import requests

url_master = "http://localhost:5000/enviar-tarea"

tareas = [10, 20, 30]

print("Enviando tareas al master...")
for i, tarea in enumerate(tareas, 1):
    response = requests.post(url_master, json={"tarea": tarea})
    resultado = response.json()
    print(f"\nTarea {i}: {tarea}")
    print(f"Enviada a esclavo: {resultado['esclavo']}")
    print(f"Respuesta recibida: {resultado['respuesta']}")