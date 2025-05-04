# TrabajoPractico01_INFO288_202501

## Instalación

### Ubuntu

#### Requisitos de paquetes

Ejecuta los siguientes comandos para instalar las dependencias necesarias:

```bash
sudo apt install python3-mysql.connector
sudo apt install python3-flask
sudo apt install python3-requests
```

#### MariaDB

1. Instala MariaDB utilizando el gestor de paquetes apt:
   ```bash
   sudo apt update
   sudo apt install mariadb-server
2. Inicia el servicio de MariaDB:
   ```bash
   sudo systemctl start mariadb
3. Verifica que el servicio esté corriendo:
   ```bash
   sudo systemctl status mariadb


# Configuración de la Base de Datos en UBUNTU

1. Conéctate al servidor de MariaDB utilizando el cliente de línea de comandos:
    ```bash
   mysql -u root -p
3. Crea una nueva base de datos llamada distribuidos:
   ```bash
   CREATE DATABASE problema1_SD;
5. Crea un nuevo usuario y otórgale todos los permisos sobre la base de datos:
    ```bash
   CREATE USER 'user'@'localhost' IDENTIFIED BY '1234';
   GRANT ALL PRIVILEGES ON problema1_SD.* TO 'user'@'localhost';
   FLUSH PRIVILEGES;
6. Crear las tablas de problema1_SD


# Ejecución
1. Clonar el repositorio
    ```bash
   git clone https://github.com/fcordovav/TrabajoPractico01_INFO288_202501
2. Entrar al directorio del proyecto
    ```bash
   cd TrabajoPractico01_INFO288_202501
4. Ejecuta el archivo master.py
   ```bash
   python3 master.py
5. Ejecuta el archivo initiator.py
   ```bash
   python3 initiator.py

# Variables de entorno

# Consultas a la API

