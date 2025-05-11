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