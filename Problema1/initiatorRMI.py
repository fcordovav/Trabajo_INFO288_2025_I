import subprocess
import os
import signal

# Ruta al Python del entorno virtual
VENV_PYTHON = os.path.abspath("pyro_env/bin/python3")


# Directorio base donde están los esclavos
base_dir = "slaves"

# Lista de procesos lanzados
processes = []

try:
    for slave_folder in os.listdir(base_dir):
        slave_path = os.path.join(base_dir, slave_folder)
        client_script = os.path.join(slave_path, "clientRMI.py")

        # Saltar si no es una carpeta o si no tiene clientRMI.py
        if not os.path.isdir(slave_path) or not os.path.isfile(client_script):
            continue

        print(f"Iniciando cliente RMI en {client_script}...")
        p = subprocess.Popen([VENV_PYTHON, "clientRMI.py"], cwd=slave_path)
        processes.append(p)

    print("Todos los clientes RMI iniciados.\nPresiona Ctrl+C para detenerlos.")

    for p in processes:
        p.wait()

except KeyboardInterrupt:
    print("\nInterrupción detectada. Cerrando procesos...")

    for p in processes:
        try:
            p.send_signal(signal.SIGINT)
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"Proceso {p.pid} no respondió, terminando forzosamente...")
            p.terminate()

    print("Todos los procesos finalizados.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
