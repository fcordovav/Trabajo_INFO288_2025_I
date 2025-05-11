-- Usar la base de datos correspondiente para la tabla "users"
USE users;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad1 INT, -- Rango de edad inicial
    edad2 INT  -- Rango de edad final
);

INSERT INTO users (name, edad1, edad2) VALUES
('infante', 0, 12),
('adolescente', 13, 17),
('adulto joven', 18, 25),
('adulto', 26, 64),
('adulto mayor', 65, 120);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT
);

INSERT INTO categories (name) VALUES
('Matemáticas'), -- 1
('Programación'), -- 2
('Computación'), --3
('Física'), -- 4
('Inteligencia Artificial'), -- 5
('Tecnología'), -- 6
('Blockchain'), -- 7
('Energías renovables'), -- 8
('Ingeniería de materiales'), -- 9
('Desarrollo de software'); -- 10
('Literatura') -- 11
('Filosofía') -- 12
('Cuento'); -- 13

CREATE TABLE IF NOT EXISTS user_categories (
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, category_id)
);

-- INFANTE
INSERT INTO user_categories (user_id, category_id) VALUES
(1, 13), -- Cuento
(1, 11), -- Literatura
(1, 1);  -- Matemáticas

-- ADOLESCENTE
INSERT INTO user_categories (user_id, category_id) VALUES
(2, 1), -- Matemáticas
(2, 2), -- Programación
(2, 3), -- Computación
(2, 4), -- Física
(2, 5), -- Inteligencia Artificial
(2, 6); -- Tecnología
(2, 11), -- Literatura
(2, 12), -- Filosofía

-- ADULTO JOVEN
INSERT INTO user_categories (user_id, category_id) VALUES
(3, 2),  -- Programación
(3, 3),  -- Computación
(3, 5),  -- Inteligencia Artificial
(3, 10), -- Desarrollo de software
(3, 6),  -- Tecnología
(3, 4),  -- Física
(3, 12); -- Filosofía

-- ADULTO
INSERT INTO user_categories (user_id, category_id) VALUES
(4, 6),  -- Tecnología
(4, 7),  -- Blockchain
(4, 8),  -- Energías renovables
(4, 9),  -- Ingeniería de materiales
(4, 10), -- Desarrollo de software
(4, 1);  -- Matemáticas

-- ADULTO MAYOR
INSERT INTO user_categories (user_id, category_id) VALUES
(5, 11), -- Literatura
(5, 12), -- Filosofía
(5, 6);  -- Tecnología

-- Usar la base de datos correspondiente para la tabla "libro"
USE libro;

-- Crear la tabla con solo las columnas "titulo" y "tipo"
CREATE TABLE IF NOT EXISTS libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    tipo VARCHAR(50)
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Insertar datos en la tabla "libro"
INSERT INTO libro (titulo, tipo, category_id) VALUES
('Ecuaciones Diferenciales Básicas', 'libro', 1),
('Introducción a la Programación', 'libro', 2),
('Matemática Discreta', 'libro', 1);
('La posada errante', 'libro', 11),
('El arte de la guerra', 'libro', 12),
('Cien años de soledad', 'libro', 11),
('El principito', 'libro', 13),
('Crónica de una muerte anunciada', 'libro', 11),
('Rayuela', 'libro', 11),
('El túnel', 'libro', 11);
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
    tipo VARCHAR(50)
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO video (titulo, tipo, category_id) VALUES
('Curso de Python', 'video', 2),
('Teoría de la Relatividad', 'video', 4),
('Introducción a la IA', 'video', 5);
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
    tipo VARCHAR(50)
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO articulo (titulo, tipo, category_id) VALUES
('Artículos sobre Blockchain', 'articulo', 7),
('El futuro de la tecnología', 'articulo', 6),
('Nuevas tendencias en IA', 'articulo', 5);
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
    tipo VARCHAR(50)
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO tesis (titulo, tipo, category_id) VALUES
('Impacto de la energía solar', 'tesis', 8),
('Innovaciones en materiales', 'tesis', 9),
('Desarrollo de software en entornos distribuidos', 'tesis', 10);
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