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

SHOW TABLES;

/*
TABLAS PENDIENTES POR CREAR..

CREATE TABLE historiales_medicos (
	id_historial INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    ...
);

CREATE TABLE hojas_evolucion_medico (
	id_hojas INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    ...
);

CREATE TABLE avances_usuarios (
	id_avance INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    ...
);
*/

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
	usuarios.rol = roles.id_rol;