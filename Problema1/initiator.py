import subprocess
import os

env_files = [
    "slaves_envs/.envslave1",
    "slaves_envs/.envslave2",
    "slaves_envs/.envslave3",
    "slaves_envs/.envslave4"
]

processes = []

for env_file in env_files:
    # Cargar variables de entorno 
    env_vars = os.environ.copy()
    with open(env_file) as f:
        for line in f:
            key, value = line.strip().split("=")
            env_vars[key] = value
    # Lanzar esclavo.py con las variables cargadas
    p = subprocess.Popen(["python3", "slave.py"], env=env_vars)
    processes.append(p)

print("Todos los esclavos han sido iniciados.")

# Esperar a que todos terminen (si los cierras manualmente con Ctrl+C)
for p in processes:
    p.wait()