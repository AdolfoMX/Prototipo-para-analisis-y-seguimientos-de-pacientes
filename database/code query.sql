/*Creación de base de datos*/
CREATE DATABASE slsm_db;
USE slsm_db;

/*Creación de tablas*/
CREATE TABLE usuarios (
	id_usuario INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(25),
	apellidos VARCHAR(25),
    correo VARCHAR(25),
    rol int,
    contrasena VARCHAR(90),
    contrasena_hash VARCHAR(100),
    PRIMARY KEY(id_usuario)
);

CREATE TABLE roles (
	id_rol INT NOT NULL AUTO_INCREMENT,
    nombre_rol VARCHAR(20),
    PRIMARY KEY(id_rol)
);

/*Agregar datos*/
INSERT INTO roles (nombre_rol)
VALUES ('Especialista'), ('Paciente');

/*Consulta*/
SELECT * FROM usuarios;
SELECT * FROM roles;
SELECT * FROM usuarios, roles
