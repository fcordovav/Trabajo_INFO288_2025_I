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

## Configuración de la Base de Datos en UBUNTU

1. Conéctate al servidor de MariaDB utilizando el cliente de línea de comandos:
    ```bash
   sudo mysql -u root -p
3. Crear las bases de datos:
   ```bash
   CREATE DATABASE libro;
   CREATE DATABASE video;
   CREATE DATABASE articulo;
   CREATE DATABASE tesis;

5. Crea un nuevo usuario y otórgale todos los permisos sobre la base de datos:
    ```bash
   CREATE USER 'user'@'localhost' IDENTIFIED BY '1234';
   GRANT ALL PRIVILEGES ON libro.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON video.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON articulo.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON tesis.* TO 'user'@'localhost';
   FLUSH PRIVILEGES;


6. Crear las tablas de bases de datos


## Ejecución
1. Clonar el repositorio
    ```bash
   git clone https://github.com/fcordovav/TrabajoPractico01_INFO288_202501
2. Entrar al directorio del proyecto
    ```bash
   cd TrabajoPractico01_INFO288_202501
4. Ejecuta el archivo master.py
   ```bash
   python3 master.py
5. Ejecuta los esclavos manualmente en cada carpeta slaves/slave con python3 slave.py o de forma automática con
   ```bash
   python3 initiator.py

## Variables de entorno

## Consultas a la API

