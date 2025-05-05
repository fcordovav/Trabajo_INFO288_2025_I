import subprocess
import os
import signal

# Directorio base donde están las carpetas de los esclavos
base_dir = "slaves"

# Lista de carpetas de los esclavos
slaves = ["slave1", "slave2", "slave3", "slave4"]

processes = []

try:
    for slave_folder in slaves:
        script_path = os.path.join(base_dir, slave_folder, "slave.py")
        
        if not os.path.isfile(script_path):
            print(f"No se encontró el archivo: {script_path}")
            continue
        
        print(f"Iniciando {script_path}...")
        p = subprocess.Popen(["python3", script_path])
        processes.append(p)

    print("Todos los esclavos iniciados.")
    
    for p in processes:
        p.wait()

except KeyboardInterrupt:
    print("\n Interrupción detectada. Cerrando esclavos...")

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

