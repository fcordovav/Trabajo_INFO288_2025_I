# TrabajoPractico01_INFO288_202501

## Instalación

### Ubuntu

#### Requisitos de paquetes

Ejecuta los siguientes comandos para instalar las dependencias necesarias:

```bash
sudo apt install python3-mysql.connector
sudo apt install python3-flask
sudo apt install python3-requests
sudo apt install python3.12-venv
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
   ```bash
   -- Usar la base de datos correspondiente para la tabla "libro"
   USE libro;

   -- Crear la tabla con solo las columnas "titulo" y "tipo"
   CREATE TABLE IF NOT EXISTS libro (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50)
   );

   -- Insertar datos en la tabla "libro"
   INSERT INTO libro (titulo, tipo) VALUES
   ('Ecuaciones Diferenciales Básicas', 'libro'),
   ('Introducción a la Programación', 'libro'),
   ('Matemática Discreta', 'libro');

   -- Usar la base de datos correspondiente para la tabla "video"
   USE video;

   CREATE TABLE IF NOT EXISTS video (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50)
   );

   INSERT INTO video (titulo, tipo) VALUES
   ('Curso de Python', 'video'),
   ('Teoría de la Relatividad', 'video'),
   ('Introducción a la IA', 'video');

   -- Usar la base de datos correspondiente para la tabla  "articulo"
   USE articulo;

   CREATE TABLE IF NOT EXISTS articulo (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50)
   );

   INSERT INTO articulo (titulo, tipo) VALUES
   ('Artículos sobre Blockchain', 'articulo'),
   ('El futuro de la tecnología', 'articulo'),
   ('Nuevas tendencias en IA', 'articulo');

   -- Usar la base de datos correspondiente para la tabla  "tesis"
   USE tesis;

   CREATE TABLE IF NOT EXISTS tesis (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50)
   );

   INSERT INTO tesis (titulo, tipo) VALUES
   ('Impacto de la energía solar', 'tesis'),
   ('Innovaciones en materiales', 'tesis'),
   ('Desarrollo de software en entornos distribuidos', 'tesis');


## Ejecución Parte 1
1. Clonar el repositorio
    ```bash
   git clone https://github.com/fcordovav/TrabajoPractico01_INFO288_202501
2. Entrar al directorio del proyecto
    ```bash
   cd TrabajoPractico01_INFO288_202501/Problema1
4. Ejecuta el archivo master.py
   ```bash
   python3 master.py
5. Ejecuta los esclavos manualmente en cada carpeta slaves/slave con python3 slave.py o de forma automática con
   ```bash
   python3 initiator.py

## Ejecución Parte 2 (Pyro4)
1. Entrar al directorio Problema1
   ```bash
   python3 -m venv pyro_env
   source pyro_env/bin/activate
   pip install Pyro4
2. Arranca el nameserver de Pyro4
   ```bash
   source pyro_env/bin/activate
   pyro4-ns
3. Ejecutar el server RMI 
   ```bash
   source pyro_env/bin/activate
   python3 serverRMI.py
4. Ejecutar los clientes RMI
   ```bash
   python3 initiatorRMI.py

## Variables de entorno

## Consultas a la API

