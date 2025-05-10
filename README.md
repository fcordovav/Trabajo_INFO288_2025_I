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

1. Usar script para base de datos:
    ```bash
    sudo mysql -u root -p < BD.sql
 

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

