/*Creación de base de datos*/
CREATE DATABASE slsm_db;
USE slsm_db;

/*Creación de tablas*/
CREATE TABLE usuarios (
	id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(80),
    apellidos VARCHAR(80),
    correo VARCHAR(80),
    id_rol INT,
    contrasena VARCHAR(100),
    contrasena_hash VARCHAR(150),
    PRIMARY KEY(id_usuario)
);

CREATE TABLE roles (
	id_rol INT NOT NULL AUTO_INCREMENT,
    nombre_rol VARCHAR(20),
    PRIMARY KEY(id_rol)
);

CREATE TABLE historiales_medicos (
	id_historial INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_nacimiento DATE,
    altura FLOAT,
    numero_telefono VARCHAR(20),
    genero VARCHAR(2),
    peso FLOAT,
    pregunta1_sec2 VARCHAR(2),
    pregunta2_sec2 INT,
    pregunta3_sec2 VARCHAR(2),
    pregunta4_sec2 FLOAT,
    pregunta5_sec2 INT,
    pregunta6_sec2 VARCHAR(2),
    pregunta7_sec2 VARCHAR(200),
    pregunta8_sec2 INT,
    pregunta9_sec2 INT,
    pregunta10_sec2 VARCHAR(200),
    pregunta11_sec2 VARCHAR(200),
    pregunta12_sec2 VARCHAR(200),
    pregunta13_sec2 VARCHAR(200),
    pregunta1_sec3 VARCHAR(2),
    pregunta2_sec3 INT,
    pregunta3_sec3 VARCHAR(2),
    pregunta4_sec3 VARCHAR(200),
    pregunta5_sec3 VARCHAR(2),
    pregunta6_sec3 INT,
    pregunta7_sec3 VARCHAR(2),
    pregunta8_sec3 VARCHAR(200),
    pregunta9_sec3 VARCHAR(2),
    pregunta10_sec3 INT,
    pregunta11_sec3 VARCHAR(2),
    pregunta12_sec3 VARCHAR(200),
    pregunta13_sec3 VARCHAR(2),
    pregunta14_sec3 INT,
    pregunta15_sec3 VARCHAR(2),
    pregunta16_sec3 VARCHAR(200),
    pregunta17_sec3 VARCHAR(200),
    pregunta1_sec4 VARCHAR(2),
    pregunta2_sec4 VARCHAR(2),
    pregunta3_sec4 VARCHAR(2),
    pregunta4_sec4 VARCHAR(2),
    pregunta5_sec4 VARCHAR(200),
    pregunta6_sec4 VARCHAR(2),
    pregunta7_sec4 VARCHAR(2),
    pregunta8_sec4 VARCHAR(2),
    pregunta9_sec4 VARCHAR(2),
    pregunta10_sec4 VARCHAR(2),
    pregunta11_sec4 VARCHAR(2),
    pregunta12_sec4 VARCHAR(2),
    pregunta13_sec4 VARCHAR(2),
    pregunta14_sec4 VARCHAR(200),
    pregunta15_sec4 VARCHAR(2),
    pregunta16_sec4 VARCHAR(2),
    pregunta17_sec4 VARCHAR(2),
    pregunta18_sec4 VARCHAR(2),
    pregunta19_sec4 VARCHAR(2),
    pregunta20_sec4 VARCHAR(2),
    pregunta21_sec4 VARCHAR(2),
    pregunta22_sec4 VARCHAR(200),
    pregunta1_sec5 VARCHAR(2),
    pregunta2_sec5 VARCHAR(200),
    pregunta3_sec5 VARCHAR(2),
    pregunta4_sec5 VARCHAR(40),
    pregunta5_sec5 VARCHAR(2),
    pregunta6_sec5 VARCHAR(2),
    pregunta7_sec5 VARCHAR(30),
    pregunta1_sec6 INT,
    pregunta2_sec6 VARCHAR(15),
    pregunta3_sec6 VARCHAR(2),
    pregunta4_sec6 VARCHAR(2),
    pregunta5_sec6 VARCHAR(2),
    pregunta6_sec6 VARCHAR(2),
    pregunta1_sec7 VARCHAR(2),
    pregunt2_sec7 VARCHAR(2),
    pregunta3_sec7 VARCHAR(200),
    pregunta4_sec7 VARCHAR(2),
    pregunta1_ext VARCHAR(2),
    pregunta2_ext VARCHAR(200),
    pregunta3_ext VARCHAR(2),
    pregunta4_ext VARCHAR(200),
    pregunta5_ext VARCHAR(2),
    pregunta6_ext VARCHAR(22),
    PRIMARY KEY(id_historial) 
);

CREATE TABLE hojas_evolucion_medico (
	id_hojas INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_registro DATE,
    peso FLOAT,
    IMC FLOAT,
    grasa_viseral FLOAT,
    porcentaje_musculo FLOAT,
    abdomen FLOAT,
    ejercicio INT,
    horas_sueno INT,
    talla FLOAT,
    grasa_corporal FLOAT,
    edad_metabolica INT,
    calorias INT,
    glucosa FLOAT,
    comida_chatarra VARCHAR(12),
    calidad_sueno VARCHAR(12),
    notas VARCHAR(200),
    PRIMARY KEY(id_hojas)
);

CREATE TABLE avances_usuarios (
	id_avance INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_registro DATE,
    pregunta1_sec1 INT,
    notas1_sec1 VARCHAR(200),
    notas2_sec1 VARCHAR(200),
    pregunta1_sec2 INT,
    notas1_sec2 VARCHAR(200),
    notas2_sec2 VARCHAR(200),
    pregunta1_sec3 INT,
    notas1_sec3 VARCHAR(200),
    notas2_sec3 VARCHAR(200),
    pregunta1_sec4 INT,
    notas1_sec4 VARCHAR(200),
    notas2_sec4 VARCHAR(200),
    pregunta1_sec5 INT,
    notas1_sec5 VARCHAR(200),
    notas2_sec5 VARCHAR(200),
    pregunta1_sec6 INT,
    notas1_sec6 VARCHAR(200),
    notas2_sec6 VARCHAR(200),
    pregunta1_sec7 VARCHAR(200),
    PRIMARY KEY(id_avance)
);

/*
--- CONSULTAS ---
*/

/*Visualizacion de tablas*/
SHOW TABLES;

/*Cambiar nombre de un campo*/
/*ALTER TABLE usuarios CHANGE rol id_rol INT;*/

/*Agregar datos*/
INSERT INTO roles (nombre_rol)
VALUES ('Especialista'), ('Paciente');

/*Consulta*/
SELECT * FROM usuarios;
SELECT * FROM roles;

SELECT 
	usuarios.id_usuario,
    usuarios.nombre,
    usuarios.apellidos,
    roles.nombre_rol 
FROM 
	usuarios,
    roles
WHERE
	usuarios.id_rol = roles.id_rol;