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
   CREATE DATABASE users;

5. Crea un nuevo usuario y otórgale todos los permisos sobre la base de datos:
   ```bash
   CREATE USER 'user'@'localhost' IDENTIFIED BY '1234';
   GRANT ALL PRIVILEGES ON libro.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON video.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON articulo.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON tesis.* TO 'user'@'localhost';
   GRANT ALL PRIVILEGES ON users.* TO 'user'@'localhost';
   FLUSH PRIVILEGES;


6. Crear las tablas de bases de datos
   ```bash
   -- Usar la base de datos correspondiente para la tabla "libro"
   USE libro;

   -- Crear la tabla con solo las columnas "titulo" y "tipo"
   CREATE TABLE IF NOT EXISTS libro (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50),
      category_id INT
   );

   -- Insertar datos en la tabla "libro"
   INSERT INTO libro (titulo, tipo, category_id) VALUES
   ('Ecuaciones Diferenciales Básicas', 'libro', 1),
   ('Introducción a la Programación', 'libro', 2),
   ('Matemática Discreta', 'libro', 1),
   ('La posada errante', 'libro', 11),
   ('El arte de la guerra', 'libro', 12),
   ('Cien años de soledad', 'libro', 11),
   ('El principito', 'libro', 13),
   ('Crónica de una muerte anunciada', 'libro', 11),
   ('Rayuela', 'libro', 11),
   ('El túnel', 'libro', 11),
   ('Álgebra Lineal Aplicada', 'libro', 1),
   ('Python para Ciencia de Datos', 'libro', 2),
   ('Fundamentos de Computación', 'libro', 3),
   ('Física Cuántica Moderna', 'libro', 4),
   ('Redes Neuronales y Deep Learning', 'libro', 5),
   ('Tecnología Espacial', 'libro', 6),
   ('Criptografía Moderna', 'libro', 3),
   ('Fundamentos de Blockchain', 'libro', 7),
   ('Energía eólica en zonas rurales', 'libro', 8),
   ('Materiales inteligentes', 'libro', 9),
   ('Diseño de Software Seguro', 'libro', 10);


   -- Usar la base de datos correspondiente para la tabla "video"
   USE video;

   CREATE TABLE IF NOT EXISTS video (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50),
      category_id INT
   );

   INSERT INTO video (titulo, tipo, category_id) VALUES
   ('Curso de Python', 'video', 2),
   ('Teoría de la Relatividad', 'video', 4),
   ('Introducción a la IA', 'video', 5),
   ('Álgebra para principiantes', 'video', 1),
   ('Programación en JavaScript', 'video', 2),
   ('Lógica Computacional', 'video', 3),
   ('Experimentos de física con Arduino', 'video', 4),
   ('IA Generativa y Chatbots', 'video', 5),
   ('Tecnología 5G explicada', 'video', 6),
   ('Blockchain aplicado a logística', 'video', 7),
   ('Proyectos solares caseros', 'video', 8),
   ('Propiedades de nuevos materiales', 'video', 9),
   ('Testing automatizado de software', 'video', 10);

   -- Usar la base de datos correspondiente para la tabla  "articulo"
   USE articulo;

   CREATE TABLE IF NOT EXISTS articulo (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50),
      category_id INT
   );

   INSERT INTO articulo (titulo, tipo, category_id) VALUES
   ('Artículos sobre Blockchain', 'articulo', 7),
   ('El futuro de la tecnología', 'articulo', 6),
   ('Nuevas tendencias en IA', 'articulo', 5),
   ('El impacto de las matemáticas en la IA', 'articulo', 1),
   ('Nuevas metodologías de programación ágil', 'articulo', 2),
   ('Tendencias en arquitecturas computacionales', 'articulo', 3),
   ('Física de partículas y colisionadores', 'articulo', 4),
   ('Avances recientes en visión computacional', 'articulo', 5),
   ('La evolución tecnológica post-pandemia', 'articulo', 6),
   ('Blockchain en sistemas financieros', 'articulo', 7),
   ('Energía solar vs energía eólica', 'articulo', 8),
   ('Nanotecnología en materiales', 'articulo', 9),
   ('Microservicios en desarrollo de software', 'articulo', 10);

   -- Usar la base de datos correspondiente para la tabla  "tesis"
   USE tesis;

   CREATE TABLE IF NOT EXISTS tesis (
      id INT AUTO_INCREMENT PRIMARY KEY,
      titulo VARCHAR(255),
      tipo VARCHAR(50),
      category_id INT
   );

   INSERT INTO tesis (titulo, tipo, category_id) VALUES
   ('Impacto de la energía solar', 'tesis', 8),
   ('Innovaciones en materiales', 'tesis', 9),
   ('Desarrollo de software en entornos distribuidos', 'tesis', 10),
   ('Modelado matemático de epidemias', 'tesis', 1),
   ('Lenguajes de programación funcionales', 'tesis', 2),
   ('Simulación computacional de fluidos', 'tesis', 3),
   ('Ondas gravitacionales: detección y análisis', 'tesis', 4),
   ('Redes neuronales aplicadas a medicina', 'tesis', 5),
   ('Impacto tecnológico en la educación rural', 'tesis', 6),
   ('Criptografía poscuántica', 'tesis', 3),
   ('Blockchain en administración pública', 'tesis', 7),
   ('Aplicaciones solares en comunidades indígenas', 'tesis', 8),
   ('Materiales biodegradables para empaques', 'tesis', 9),
   ('Arquitectura de microservicios en la nube', 'tesis', 10);



   USE users;

   -- Tabla users simplificada (infante, joven, adulto)
   CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nombre VARCHAR(50) NOT NULL,
      edad_min INT,
      edad_max INT
   );

   -- Insertar solo las 3 categorías de usuarios
   INSERT INTO users (nombre, edad_min, edad_max) VALUES
   ('infante', 0, 12),
   ('joven', 13, 25),
   ('adulto', 26, 120);

   -- Tabla categories (corregida con comas)
   CREATE TABLE IF NOT EXISTS categories (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50) NOT NULL
   );

   -- Insertar categorías (corregido)
   INSERT INTO categories (name) VALUES
   ('Matemáticas'),       -- 1
   ('Programación'),       -- 2
   ('Computación'),        -- 3
   ('Física'),             -- 4
   ('Inteligencia Artificial'), -- 5
   ('Tecnología'),         -- 6
   ('Blockchain'),         -- 7
   ('Energías renovables'), -- 8
   ('Ingeniería de materiales'), -- 9
   ('Desarrollo de software'), -- 10
   ('Literatura'),         -- 11
   ('Filosofía'),          -- 12
   ('Cuento');             -- 13

   -- Tabla user_categories (relación muchos a muchos)
   CREATE TABLE IF NOT EXISTS user_categories (
      user_id INT,
      category_id INT,
      PRIMARY KEY (user_id, category_id),
      FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
      FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
   );

   -- Asignar categorías solo a infante, joven y adulto (simplificado)
   -- INFANTE (id=1)
   INSERT INTO user_categories (user_id, category_id) VALUES
   (1, 11), -- Literatura
   (1, 13); -- Cuento

   -- JOVEN (id=2)
   INSERT INTO user_categories (user_id, category_id) VALUES
   (2, 1),  -- Matemáticas
   (2, 2),  -- Programación
   (2, 4);  -- Física

   -- ADULTO (id=3)
   INSERT INTO user_categories (user_id, category_id) VALUES
   (3, 6),  -- Tecnología
   (3, 7),  -- Blockchain
   (3, 10); -- Desarrollo de software


## Ejecución Parte 1
1. Clonar el repositorio
    ```bash
   git clone https://github.com/fcordovav/TrabajoPractico01_INFO288_202501
2. Entrar al directorio del proyecto
    ```bash
   cd TrabajoPractico01_INFO288_202501/Problema1

3. Variables de entorno

Se debe construir un .env en:

/Problema1:

   ```
   URL1=http://localhost:5001/query
   TIPO_DOCUMENTO1=libro
   URL2=http://localhost:5002/query
   TIPO_DOCUMENTO2=tesis
   URL3=http://localhost:5003/query
   TIPO_DOCUMENTO3=video
   URL4=http://localhost:5004/query
   TIPO_DOCUMENTO4=articulo
   ```
En cada uno de los slave debe estar esto:

   ```
   DB_HOST=localhost
   DB_USER=user
   DB_PASSWORD=1234
   ```

y ahora agregarle esto individualmente 

/slave1:

   ```
   ID=1
   IP=127.0.0.1
   PORT=5001
   TIPO_DOCUMENTO=libro
   DB_NAME=libro
   ```

/slave2:

   ```
   ID=2
   IP=127.0.0.1
   PORT=5002
   TIPO_DOCUMENTO=tesis
   DB_NAME=tesis
   ```

/slave3:

   ```
   ID=3
   IP=127.0.0.1
   PORT=5003
   TIPO_DOCUMENTO=video
   DB_NAME=video
   ```

/slave4:

   ```
   ID=4
   IP=127.0.0.1
   PORT=5004
   TIPO_DOCUMENTO=articulo
   DB_NAME=articulo
   ```


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
(Ejrcutar pasos 2, 3 y 4 en distintas terminales)

## Consultas a la API

