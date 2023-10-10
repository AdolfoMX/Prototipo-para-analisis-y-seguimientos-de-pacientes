CREATE DATABASE  IF NOT EXISTS `slsm_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `slsm_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: slsm_db
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `avances_usuarios`
--

DROP TABLE IF EXISTS `avances_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avances_usuarios` (
  `id_avance` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `pregunta1_sec1` int DEFAULT NULL,
  `notas1_sec1` varchar(200) DEFAULT NULL,
  `notas2_sec1` varchar(200) DEFAULT NULL,
  `pregunta1_sec2` int DEFAULT NULL,
  `notas1_sec2` varchar(200) DEFAULT NULL,
  `notas2_sec2` varchar(200) DEFAULT NULL,
  `pregunta1_sec3` int DEFAULT NULL,
  `notas1_sec3` varchar(200) DEFAULT NULL,
  `notas2_sec3` varchar(200) DEFAULT NULL,
  `pregunta1_sec4` int DEFAULT NULL,
  `notas1_sec4` varchar(200) DEFAULT NULL,
  `notas2_sec4` varchar(200) DEFAULT NULL,
  `pregunta1_sec5` int DEFAULT NULL,
  `notas1_sec5` varchar(200) DEFAULT NULL,
  `notas2_sec5` varchar(200) DEFAULT NULL,
  `pregunta1_sec6` int DEFAULT NULL,
  `notas1_sec6` varchar(200) DEFAULT NULL,
  `notas2_sec6` varchar(200) DEFAULT NULL,
  `pregunta1_sec7` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_avance`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avances_usuarios`
--

LOCK TABLES `avances_usuarios` WRITE;
/*!40000 ALTER TABLE `avances_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `avances_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historiales_medicos`
--

DROP TABLE IF EXISTS `historiales_medicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historiales_medicos` (
  `id_historial` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `numero_telefono` varchar(20) DEFAULT NULL,
  `genero` varchar(15) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `pregunta1_sec2` varchar(2) DEFAULT NULL,
  `pregunta2_sec2` int DEFAULT NULL,
  `pregunta3_sec2` varchar(2) DEFAULT NULL,
  `pregunta4_sec2` float DEFAULT NULL,
  `pregunta5_sec2` int DEFAULT NULL,
  `pregunta6_sec2` varchar(2) DEFAULT NULL,
  `pregunta7_sec2` varchar(200) DEFAULT NULL,
  `pregunta8_sec2` int DEFAULT NULL,
  `pregunta9_sec2` int DEFAULT NULL,
  `pregunta10_sec2` varchar(200) DEFAULT NULL,
  `pregunta11_sec2` varchar(200) DEFAULT NULL,
  `pregunta12_sec2` varchar(200) DEFAULT NULL,
  `pregunta13_sec2` varchar(200) DEFAULT NULL,
  `pregunta1_sec3` varchar(2) DEFAULT NULL,
  `pregunta2_sec3` int DEFAULT NULL,
  `pregunta3_sec3` varchar(2) DEFAULT NULL,
  `pregunta4_sec3` varchar(200) DEFAULT NULL,
  `pregunta5_sec3` varchar(2) DEFAULT NULL,
  `pregunta6_sec3` int DEFAULT NULL,
  `pregunta7_sec3` varchar(2) DEFAULT NULL,
  `pregunta8_sec3` varchar(200) DEFAULT NULL,
  `pregunta9_sec3` varchar(2) DEFAULT NULL,
  `pregunta10_sec3` int DEFAULT NULL,
  `pregunta11_sec3` varchar(2) DEFAULT NULL,
  `pregunta12_sec3` varchar(200) DEFAULT NULL,
  `pregunta13_sec3` varchar(2) DEFAULT NULL,
  `pregunta14_sec3` int DEFAULT NULL,
  `pregunta15_sec3` varchar(2) DEFAULT NULL,
  `pregunta16_sec3` varchar(200) DEFAULT NULL,
  `pregunta17_sec3` varchar(200) DEFAULT NULL,
  `pregunta1_sec4` varchar(2) DEFAULT NULL,
  `pregunta2_sec4` varchar(2) DEFAULT NULL,
  `pregunta3_sec4` varchar(2) DEFAULT NULL,
  `pregunta4_sec4` varchar(2) DEFAULT NULL,
  `pregunta5_sec4` varchar(200) DEFAULT NULL,
  `pregunta6_sec4` varchar(2) DEFAULT NULL,
  `pregunta7_sec4` varchar(2) DEFAULT NULL,
  `pregunta8_sec4` varchar(2) DEFAULT NULL,
  `pregunta9_sec4` varchar(2) DEFAULT NULL,
  `pregunta10_sec4` varchar(2) DEFAULT NULL,
  `pregunta11_sec4` varchar(2) DEFAULT NULL,
  `pregunta12_sec4` varchar(2) DEFAULT NULL,
  `pregunta13_sec4` varchar(2) DEFAULT NULL,
  `pregunta14_sec4` varchar(200) DEFAULT NULL,
  `pregunta15_sec4` varchar(2) DEFAULT NULL,
  `pregunta16_sec4` varchar(2) DEFAULT NULL,
  `pregunta17_sec4` varchar(2) DEFAULT NULL,
  `pregunta18_sec4` varchar(2) DEFAULT NULL,
  `pregunta19_sec4` varchar(2) DEFAULT NULL,
  `pregunta20_sec4` varchar(2) DEFAULT NULL,
  `pregunta21_sec4` varchar(2) DEFAULT NULL,
  `pregunta22_sec4` varchar(200) DEFAULT NULL,
  `pregunta1_sec5` varchar(2) DEFAULT NULL,
  `pregunta2_sec5` varchar(200) DEFAULT NULL,
  `pregunta3_sec5` varchar(2) DEFAULT NULL,
  `pregunta4_sec5` varchar(40) DEFAULT NULL,
  `pregunta5_sec5` varchar(2) DEFAULT NULL,
  `pregunta6_sec5` varchar(2) DEFAULT NULL,
  `pregunta7_sec5` varchar(40) DEFAULT NULL,
  `pregunta1_sec6` int DEFAULT NULL,
  `pregunta2_sec6` varchar(40) DEFAULT NULL,
  `pregunta3_sec6` varchar(2) DEFAULT NULL,
  `pregunta4_sec6` varchar(2) DEFAULT NULL,
  `pregunta5_sec6` varchar(2) DEFAULT NULL,
  `pregunta6_sec6` varchar(2) DEFAULT NULL,
  `pregunta1_sec7` varchar(2) DEFAULT NULL,
  `pregunt2_sec7` varchar(2) DEFAULT NULL,
  `pregunta3_sec7` varchar(200) DEFAULT NULL,
  `pregunta4_sec7` varchar(2) DEFAULT NULL,
  `pregunta1_ext` varchar(2) DEFAULT NULL,
  `pregunta2_ext` varchar(200) DEFAULT NULL,
  `pregunta3_ext` varchar(2) DEFAULT NULL,
  `pregunta4_ext` varchar(200) DEFAULT NULL,
  `pregunta5_ext` varchar(2) DEFAULT NULL,
  `pregunta6_ext` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_historial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiales_medicos`
--

LOCK TABLES `historiales_medicos` WRITE;
/*!40000 ALTER TABLE `historiales_medicos` DISABLE KEYS */;
/*!40000 ALTER TABLE `historiales_medicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hojas_evolucion_medico`
--

DROP TABLE IF EXISTS `hojas_evolucion_medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hojas_evolucion_medico` (
  `id_hojas` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `IMC` float DEFAULT NULL,
  `grasa_viseral` float DEFAULT NULL,
  `porcentaje_musculo` float DEFAULT NULL,
  `abdomen` float DEFAULT NULL,
  `ejercicio` int DEFAULT NULL,
  `horas_sueno` int DEFAULT NULL,
  `talla` float DEFAULT NULL,
  `grasa_corporal` float DEFAULT NULL,
  `edad_metabolica` int DEFAULT NULL,
  `calorias` int DEFAULT NULL,
  `glucosa` float DEFAULT NULL,
  `comida_chatarra` varchar(12) DEFAULT NULL,
  `calidad_sueno` varchar(12) DEFAULT NULL,
  `notas` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_hojas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hojas_evolucion_medico`
--

LOCK TABLES `hojas_evolucion_medico` WRITE;
/*!40000 ALTER TABLE `hojas_evolucion_medico` DISABLE KEYS */;
/*!40000 ALTER TABLE `hojas_evolucion_medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Especialista'),(2,'Paciente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  `apellidos` varchar(80) DEFAULT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `id_rol` int DEFAULT NULL,
  `contrasena` varchar(100) DEFAULT NULL,
  `contrasena_hash` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'GUADALUPE','GUINTO','guadalupe.guinto@gmail.com',2,'12345','$2b$12$NffuYu0ZnORLiM/PObslrugmyRsFz0V8sPArMW2HK7Lu3VYawhb7.'),(2,'AMAYRANI','GOMEZ','170300079@ucaribe.edu.mx',1,'12345','$2b$12$q1ROBA.geON5Ll9PvyD.ROHVtBTqyKXwEfSPzeIFZb.vz2PiKUAEm'),(3,'ADOLFO ','TUN DZUL','170300124@ucaribe.edu.mx',2,'12345','$2b$12$7dYcrIuYsYl8Rg769cLTzeL0WHxbsq5RBuWsq1JuLqd8UmozirYD2'),(4,'KARLA','GUINTO','karla.guinto@gmail.com',2,'12345','$2b$12$M9BpQ4wQCB6pbiLrodDkjuvkCejCoH..F1AN8ZD6aoblpNHxbikqO'),(5,'GUADALUPE','SALINAS','guadalupe.salinas@gmail.com',1,'12345','$2b$12$6QnmWuNG1RQoHh6rwcch5.eCZTvKiHKgJx3WkCR9FZNwEUl7giADy'),(6,'AMAYRANI','GOMEZ','amayraniigomez@gmail.com',2,'12345','$2b$12$o8uAScdMsXi8ZXT8R9ZmyOXzcaVYN5X31MTQts2ktwNVgeiJ0NEfO');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'slsm_db'
--

--
-- Dumping routines for database 'slsm_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-09 22:50:22
