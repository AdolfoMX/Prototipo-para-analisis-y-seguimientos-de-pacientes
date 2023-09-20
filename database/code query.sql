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
    PRIMARY KEY(id_usuario)
);

/*Inserción*/
INSERT INTO usuarios (usuariosnombre, apellidos, correo, rol, contrasena) 
VALUES ("ADOLFO", "TUN DZUL", "170300124@ucaribe.edu.mx", "Paciente", "12345");

/*Consulta*/
SELECT * FROM usuarios;
SELECT * FROM usuarios WHERE correo LIKE '170300124@ucaribe.edu.mx';
