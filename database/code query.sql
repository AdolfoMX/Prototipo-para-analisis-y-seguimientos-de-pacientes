/*Creación de base de datos*/
CREATE DATABASE slsm_db;
USE slsm_db;

/*Creación de tablas*/
CREATE TABLE usuarios (
	id_usuario INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(25),
	apellidos VARCHAR(25),
    correo VARCHAR(25),
    fecha_nacimiento DATE,
    rol VARCHAR (13),
    contrasena VARCHAR(90),
    contrasena_hash VARCHAR(100),
    PRIMARY KEY(id_usuario)
);

/*Consulta*/
SELECT * FROM usuarios;
