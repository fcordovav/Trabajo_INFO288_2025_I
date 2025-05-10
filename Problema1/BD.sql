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

-- Repetir para la base de datos "video"
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

-- Repetir para la base de datos "articulo"
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

-- Repetir para la base de datos "tesis"
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