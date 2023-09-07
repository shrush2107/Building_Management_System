-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: buildingmanagement1
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `buildngmanager`
--

DROP TABLE IF EXISTS `buildngmanager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buildngmanager` (
  `bmanager_id` varchar(6) NOT NULL,
  `start_date` date NOT NULL,
  `salary` int NOT NULL,
  UNIQUE KEY `bmanager_id` (`bmanager_id`),
  CONSTRAINT `buildngmanager_ibfk_1` FOREIGN KEY (`bmanager_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildngmanager`
--

LOCK TABLES `buildngmanager` WRITE;
/*!40000 ALTER TABLE `buildngmanager` DISABLE KEYS */;
INSERT INTO `buildngmanager` VALUES ('BM1','2012-01-01',120000);
/*!40000 ALTER TABLE `buildngmanager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `helpprovider`
--

DROP TABLE IF EXISTS `helpprovider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `helpprovider` (
  `helpprovider_id` varchar(6) NOT NULL,
  `address` varchar(255) NOT NULL,
  `role` enum('plumber','pest control worker','handyman') NOT NULL,
  UNIQUE KEY `helpprovider_id` (`helpprovider_id`),
  CONSTRAINT `helpprovider_ibfk_1` FOREIGN KEY (`helpprovider_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `helpprovider`
--

LOCK TABLES `helpprovider` WRITE;
/*!40000 ALTER TABLE `helpprovider` DISABLE KEYS */;
INSERT INTO `helpprovider` VALUES ('Hp1','57 Hudson Pass','plumber'),('hp2','5384 Weeping Birch Point','handyman'),('hp3','616 Steensland Pass','handyman'),('hp4','1 West Crossing','plumber'),('hp5','5 Harbort Alley','handyman'),('hp6','0074 Arizona Hill','pest control worker'),('hp7','0215 Butterfield Drive','pest control worker');
/*!40000 ALTER TABLE `helpprovider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insurance`
--

DROP TABLE IF EXISTS `insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insurance` (
  `insurance_id` int NOT NULL AUTO_INCREMENT,
  `lease_id` int NOT NULL,
  `tenant_id` varchar(6) NOT NULL,
  `start_date` date NOT NULL,
  `tenure` int NOT NULL,
  `insurance_provider` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`insurance_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `lease_id` (`lease_id`),
  CONSTRAINT `insurance_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenant` (`tenant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `insurance_ibfk_2` FOREIGN KEY (`lease_id`) REFERENCES `lease` (`lease_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurance`
--

LOCK TABLES `insurance` WRITE;
/*!40000 ALTER TABLE `insurance` DISABLE KEYS */;
INSERT INTO `insurance` VALUES (1,9,'T13','2021-08-25',12,'Nader, Champlin and Huel'),(2,1,'T2','2021-07-13',12,'Daniel LLC'),(3,13,'T18','2021-12-10',12,'Nader, Champlin and Huel'),(4,17,'T3','2021-08-29',12,'Daniel LLC'),(5,18,'T20','2021-09-19',12,'Nader, Champlin and Huel'),(6,10,'T15','2021-12-22',12,'Daniel LLC'),(7,11,'T9','2021-09-06',12,'Cormier LLC'),(8,19,'T17','2021-07-31',12,'Daniel LLC'),(9,14,'T11','2021-12-04',12,'Nader, Champlin and Huel'),(10,2,'T14','2021-11-11',12,'Daniel LLC'),(11,3,'T7','2021-07-29',12,'Cormier LLC'),(12,6,'T6','2021-11-28',12,'Nader, Champlin and Huel'),(13,20,'T19','2021-09-16',12,'Daniel LLC'),(14,15,'T4','2021-11-12',12,'Cormier LLC'),(15,7,'T5','2021-11-22',12,'Nader, Champlin and Huel'),(16,4,'T1','2021-08-22',12,'Cormier LLC'),(17,16,'T8','2021-12-19',12,'Daniel LLC'),(18,5,'T12','2021-10-25',12,'Cormier LLC'),(19,12,'T16','2021-10-13',12,'Cormier LLC'),(20,8,'T10','2021-07-15',12,'Daniel LLC');
/*!40000 ALTER TABLE `insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lease`
--

DROP TABLE IF EXISTS `lease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lease` (
  `lease_id` int NOT NULL AUTO_INCREMENT,
  `lmanager_id` varchar(6) NOT NULL,
  `tenant_id` varchar(6) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `appartment_number` varchar(10) NOT NULL,
  `rent_amount` int NOT NULL,
  PRIMARY KEY (`lease_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `lmanager_id` (`lmanager_id`),
  CONSTRAINT `lease_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenant` (`tenant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `lease_ibfk_2` FOREIGN KEY (`lmanager_id`) REFERENCES `leasingmanager` (`lmanager_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lease`
--

LOCK TABLES `lease` WRITE;
/*!40000 ALTER TABLE `lease` DISABLE KEYS */;
INSERT INTO `lease` VALUES (1,'LM3','T2','2021-07-13','2024-11-20','17',2600),(2,'LM2','T14','2021-11-11','2023-02-26','10',2900),(3,'LM1','T7','2021-07-29','2023-05-31','13',2500),(4,'LM5','T1','2021-08-22','2023-11-01','20',2700),(5,'LM2','T12','2021-10-25','2023-01-31','2',2500),(6,'LM4','T6','2021-11-28','2024-08-08','14',2500),(7,'LM2','T5','2021-11-22','2023-09-20','9',3000),(8,'LM1','T10','2021-07-15','2023-07-17','15',3500),(9,'LM4','T13','2021-08-25','2024-07-15','18',2700),(10,'LM3','T15','2021-12-22','2024-12-27','3',2900),(11,'LM5','T9','2021-09-06','2024-05-16','4',3200),(12,'LM4','T16','2021-10-13','2024-05-10','7',2600),(13,'LM3','T18','2021-12-10','2024-01-28','5',2600),(14,'LM1','T11','2021-12-04','2023-07-03','6',2600),(15,'LM3','T4','2021-11-12','2025-09-06','1',2700),(16,'LM4','T8','2021-12-19','2024-01-21','11',2900),(17,'LM2','T3','2021-08-29','2023-12-07','12',3000),(18,'LM1','T20','2021-09-19','2025-09-11','8',2900),(19,'LM1','T17','2021-07-31','2023-07-22','19',3000),(20,'LM2','T19','2021-09-16','2023-05-29','16',3000);
/*!40000 ALTER TABLE `lease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leasingmanager`
--

DROP TABLE IF EXISTS `leasingmanager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leasingmanager` (
  `lmanager_id` varchar(6) NOT NULL,
  UNIQUE KEY `lmanager_id` (`lmanager_id`),
  CONSTRAINT `leasingmanager_ibfk_1` FOREIGN KEY (`lmanager_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leasingmanager`
--

LOCK TABLES `leasingmanager` WRITE;
/*!40000 ALTER TABLE `leasingmanager` DISABLE KEYS */;
INSERT INTO `leasingmanager` VALUES ('LM1'),('LM2'),('LM3'),('LM4'),('LM5');
/*!40000 ALTER TABLE `leasingmanager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rentbill`
--

DROP TABLE IF EXISTS `rentbill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rentbill` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `lmanager_id` varchar(6) NOT NULL,
  `tenant_id` varchar(6) NOT NULL,
  `due_date` varchar(255) NOT NULL,
  `status` enum('paid','not paid') NOT NULL,
  PRIMARY KEY (`bill_id`),
  KEY `tenant_id` (`tenant_id`),
  KEY `lmanager_id` (`lmanager_id`),
  CONSTRAINT `rentbill_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenant` (`tenant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rentbill_ibfk_2` FOREIGN KEY (`lmanager_id`) REFERENCES `leasingmanager` (`lmanager_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rentbill`
--

LOCK TABLES `rentbill` WRITE;
/*!40000 ALTER TABLE `rentbill` DISABLE KEYS */;
INSERT INTO `rentbill` VALUES (1,'LM5','T1','2023-01-01','not paid'),(2,'LM4','T13','2023-01-04','not paid'),(3,'LM3','T2','2023-01-01','not paid'),(4,'LM2','T3','2023-01-02','not paid'),(5,'LM3','T4','2023-01-02','not paid'),(6,'LM2','T5','2023-01-02','not paid'),(7,'LM3','T18','2023-01-06','not paid'),(8,'LM4','T6','2023-01-02','not paid'),(9,'LM1','T7','2023-01-02','not paid'),(10,'LM1','T11','2023-01-03','not paid'),(11,'LM2','T14','2023-01-04','not paid'),(12,'LM4','T8','2023-01-02','not paid'),(13,'LM5','T9','2023-01-02','not paid'),(14,'LM2','T19','2023-01-06','not paid'),(15,'LM1','T10','2023-01-02','not paid'),(16,'LM4','T16','2023-01-05','not paid'),(17,'LM2','T12','2023-01-03','not paid'),(18,'LM1','T17','2023-01-05','not paid'),(19,'LM3','T15','2023-01-04','not paid'),(20,'LM1','T20','2023-01-06','not paid'),(21,'LM5','T1','2022-12-01','paid'),(22,'LM4','T13','2022-12-04','paid'),(23,'LM3','T2','2022-12-01','paid'),(24,'LM2','T3','2022-12-02','paid'),(25,'LM3','T4','2022-12-02','paid'),(26,'LM2','T5','2022-12-02','paid'),(27,'LM3','T18','2022-12-06','paid'),(28,'LM4','T6','2022-12-02','paid'),(29,'LM1','T7','2022-12-02','paid'),(30,'LM1','T11','2022-12-03','paid'),(31,'LM2','T14','2022-12-04','paid'),(32,'LM4','T8','2022-12-02','paid'),(33,'LM5','T9','2022-12-02','paid'),(34,'LM2','T19','2022-12-06','paid'),(35,'LM1','T10','2022-12-02','paid'),(36,'LM4','T16','2022-12-05','paid'),(37,'LM2','T12','2022-12-03','paid'),(38,'LM1','T17','2022-12-05','paid'),(39,'LM3','T15','2022-12-04','paid'),(40,'LM1','T20','2022-12-06','paid'),(41,'LM5','T1','2022-11-01','paid'),(42,'LM4','T13','2022-11-04','paid'),(43,'LM3','T2','2022-11-01','paid'),(44,'LM2','T3','2022-11-02','paid'),(45,'LM3','T4','2022-11-02','paid'),(46,'LM2','T5','2022-11-02','paid'),(47,'LM3','T18','2022-11-06','paid'),(48,'LM4','T6','2022-11-02','paid'),(49,'LM1','T7','2022-11-02','paid'),(50,'LM1','T11','2022-11-03','paid'),(51,'LM2','T14','2022-11-04','paid'),(52,'LM4','T8','2022-11-02','paid'),(53,'LM5','T9','2022-11-02','paid'),(54,'LM2','T19','2022-11-06','paid'),(55,'LM1','T10','2022-11-02','paid'),(56,'LM4','T16','2022-11-05','paid'),(57,'LM2','T12','2022-11-03','paid'),(58,'LM1','T17','2022-11-05','paid'),(59,'LM3','T15','2022-11-04','paid'),(60,'LM1','T20','2022-11-06','paid');
/*!40000 ALTER TABLE `rentbill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service` (
  `service_id` int NOT NULL AUTO_INCREMENT,
  `tenant_id` varchar(6) NOT NULL,
  `date_request` date NOT NULL,
  `problem` enum('plumbing issue','pest control','household repair') NOT NULL,
  `service_description` varchar(500) NOT NULL,
  `service_status` enum('complete','incomplete') NOT NULL,
  `appartment_number` int NOT NULL,
  PRIMARY KEY (`service_id`),
  KEY `tenant_id` (`tenant_id`),
  CONSTRAINT `service_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenant` (`tenant_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES (1,'T16','2022-12-09','plumbing issue','water leaking from faucet','incomplete',7),(2,'T7','2022-12-08','household repair','light issue','incomplete',13),(3,'T2','2022-12-01','plumbing issue','shower issue','complete',17),(4,'T12','2022-12-08','plumbing issue','water leaking from faucet','incomplete',2),(5,'T20','2022-12-07','household repair','cabinate issue','complete',8),(6,'T16','2022-12-01','household repair','heater issue','complete',7),(7,'T10','2022-12-02','plumbing issue','shower issue','complete',15),(8,'T3','2022-12-01','household repair','light issue','complete',12),(9,'T7','2022-12-06','household repair','cabinate issue','complete',13),(10,'T12','2022-12-06','household repair','flooring issue','complete',2),(11,'T1','2022-12-07','household repair','NA','complete',20),(12,'T20','2022-12-08','plumbing issue','NA','incomplete',8),(13,'T19','2022-12-04','household repair','NA','complete',16),(14,'T13','2022-12-04','household repair','heater not working','complete',18),(15,'T12','2022-12-07','plumbing issue','water leaking from faucet','complete',2),(16,'T7','2022-12-09','household repair','window pannel broken','incomplete',13),(17,'T6','2022-12-09','household repair','heater issue','incomplete',14),(18,'T12','2022-12-04','household repair','cabinate door creaking','complete',2),(19,'T1','2022-12-08','pest control','cockroach problem','incomplete',20),(20,'T17','2022-12-02','pest control','cockroach problem','complete',19),(21,'T6','2022-12-08','pest control','NA','incomplete',14),(22,'T20','2022-12-08','household repair','floor creaking','incomplete',8),(23,'T3','2022-12-05','plumbing issue','water clogging','complete',12),(24,'T5','2022-12-09','pest control','cockroach problem','incomplete',9),(25,'T13','2022-12-09','household repair','NA','incomplete',18),(26,'T5','2022-12-09','household repair','NA','incomplete',9),(27,'T4','2022-12-06','plumbing issue','water leaking from faucet','complete',1),(28,'T10','2022-12-09','pest control','NA','incomplete',15),(29,'T10','2022-12-04','pest control','bed bug problem','complete',15),(30,'T9','2022-12-09','pest control','bed bug problem','incomplete',4),(31,'T8','2022-12-07','household repair','door not locking properly','complete',11),(32,'T11','2022-12-05','pest control','bed bug problem','complete',6),(33,'T18','2022-12-04','household repair','light not working','complete',5),(34,'T11','2022-12-07','household repair','light not working','complete',6),(35,'T1','2022-12-06','household repair','NA','complete',20);
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serviceandhelper`
--

DROP TABLE IF EXISTS `serviceandhelper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serviceandhelper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `service_id` int DEFAULT NULL,
  `helpprovider_id` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `service_id` (`service_id`),
  KEY `helpprovider_id` (`helpprovider_id`),
  CONSTRAINT `serviceandhelper_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `serviceandhelper_ibfk_2` FOREIGN KEY (`helpprovider_id`) REFERENCES `helpprovider` (`helpprovider_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serviceandhelper`
--

LOCK TABLES `serviceandhelper` WRITE;
/*!40000 ALTER TABLE `serviceandhelper` DISABLE KEYS */;
INSERT INTO `serviceandhelper` VALUES (1,1,'HP1'),(2,2,'HP3'),(3,3,'HP1'),(4,4,'HP4'),(5,5,'HP5'),(6,6,'HP2'),(7,7,'HP4'),(8,8,'HP3'),(9,9,'HP2'),(10,10,'HP5'),(11,11,'HP5'),(12,12,'HP4'),(13,13,'HP3'),(14,14,'HP2'),(15,15,'HP4'),(16,16,'HP3'),(17,17,'HP5'),(18,18,'HP5'),(19,19,'HP6'),(20,20,'HP7'),(21,21,'HP7'),(22,22,'HP3'),(23,23,'HP4'),(24,24,'HP6'),(25,25,'HP3'),(26,26,'HP5'),(27,27,'HP4'),(28,28,'HP7'),(29,29,'HP6'),(30,30,'HP7'),(31,31,'HP3'),(32,32,'HP7'),(33,33,'HP2'),(34,34,'HP5'),(35,35,'HP2');
/*!40000 ALTER TABLE `serviceandhelper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenant`
--

DROP TABLE IF EXISTS `tenant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenant` (
  `tenant_id` varchar(6) NOT NULL,
  UNIQUE KEY `tenant_id` (`tenant_id`),
  CONSTRAINT `tenant_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenant`
--

LOCK TABLES `tenant` WRITE;
/*!40000 ALTER TABLE `tenant` DISABLE KEYS */;
INSERT INTO `tenant` VALUES ('T1'),('T10'),('T11'),('T12'),('T13'),('T14'),('T15'),('T16'),('T17'),('T18'),('T19'),('T2'),('T20'),('T3'),('T4'),('T5'),('T6'),('T7'),('T8'),('T9');
/*!40000 ALTER TABLE `tenant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenantcarddetails`
--

DROP TABLE IF EXISTS `tenantcarddetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenantcarddetails` (
  `tenantcarddetails_id` int NOT NULL AUTO_INCREMENT,
  `tenant_id` varchar(6) NOT NULL,
  `card_number` bigint NOT NULL,
  `exp_date` varchar(10) NOT NULL,
  `security_code` int NOT NULL,
  PRIMARY KEY (`tenantcarddetails_id`),
  KEY `tenant_id` (`tenant_id`),
  CONSTRAINT `tenantcarddetails_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenant` (`tenant_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenantcarddetails`
--

LOCK TABLES `tenantcarddetails` WRITE;
/*!40000 ALTER TABLE `tenantcarddetails` DISABLE KEYS */;
INSERT INTO `tenantcarddetails` VALUES (1,'T1',5108758051269150,'2027-10',858),(2,'T2',5108755045591921,'2027-06',649),(3,'T3',5108751171959453,'2024-05',413),(4,'T4',5048375337966526,'2026-10',509),(5,'T5',5108751320414509,'2026-04',954),(6,'T6',5108759425441285,'2024-02',635),(7,'T7',5108752645289279,'2024-06',675),(8,'T8',5048375709607252,'2025-08',559),(9,'T9',5048376357337663,'2024-07',552),(10,'T10',5108756782571621,'2024-08',235),(11,'T11',5048376278542862,'2025-11',605),(12,'T12',5048374940525951,'2024-11',174),(13,'T13',5048378106113155,'2027-01',738),(14,'T14',5108751296136326,'2023-12',629),(15,'T15',5048375253433758,'2026-12',753),(16,'T16',5048374240447120,'2023-05',937),(17,'T17',5108750692127384,'2027-11',116),(18,'T18',5048374825067400,'2027-04',182),(19,'T19',5108758028037912,'2023-10',496),(20,'T20',5108752645444734,'2025-11',207),(21,'T17',5108753296905981,'2027-08',179),(22,'T2',5108752642465559,'2025-04',439),(23,'T5',5048372896732308,'2025-10',267),(24,'T14',5048378328539088,'2023-07',399),(25,'T20',5048374342341569,'2023-09',314);
/*!40000 ALTER TABLE `tenantcarddetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` varchar(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `usercred` varchar(255) NOT NULL,
  `userpassword` varchar(255) NOT NULL,
  `date_of_birth` date NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `nationality` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('BM1','Bo Peng','Male','bopeng123','Peng!567','1989-06-14','546-679-098','China'),('HP1','Alfreda McGrey','Female','amcgrey0','8joi88IJ9X8','1990-03-16','952-113-6581','Italy'),('HP2','Lorrie Olford','Male','lolford1','vNGVE8dJX','1957-04-16','484-124-9480','Mexico'),('HP3','Lorrie Pinxton','Male','lpinxton2','Hq98tNEA6Ast','1959-04-21','987-767-4547','Mexico'),('HP4','Amalee MacRedmond','Female','amacredmond3','7i2SHgqZ','1967-08-19','409-112-9554','Spain'),('HP5','Beverley Boylund','Female','bboylund4','NBkR2A2a','1989-03-26','445-166-0973','Italy'),('HP6','Elsinore Blamey','Female','eblamey5','RMWK1626','1998-01-01','738-950-8353','Pakistan'),('HP7','Horatia Bonwick','Female','hbonwick6','kLHN9hmaa','1957-02-17','511-397-5911','Mexico'),('LM1','Fernando Oherlihy','Male','foherlihy0','zqMknZ8dN7','1958-05-16','760-991-0228','Brazil'),('LM2','Freddi Kytley','Female','fkytley1','xfNwpD','1987-11-23','209-710-2561','American'),('LM3','Stanwood Stickland','Male','sstickland2','N2TTMgiq','1997-06-06','371-334-7513','Armenia'),('LM4','Rickert Arnowicz','Male','rarnowicz3','UczlacAk2','1968-05-26','316-188-2864','Japan'),('LM5','Travus Vertey','Male','tvertey4','hYdgpbg','1999-05-10','889-135-6079','Italy'),('T1','Torrance Matteacci','Male','tmatteacci0','bn19xNEjx','1957-04-16','465-705-5616','Brazil'),('T10','Jerrold Tilburn','Male','jtilburn9','2k2Zxub','2007-05-28','307-560-8712','American'),('T11','Chrysa Peplay','Female','cpeplaya','DriftrU','1994-06-30','896-253-0361','Indonesia'),('T12','Licha Sheering','Female','lsheeringb','J2cgpv3','1997-07-31','455-912-5199','Russia'),('T13','Conway Petegree','Male','cpetegreec','CUQrqn','1985-10-20','704-357-6501','Mali'),('T14','Burton Killock','Male','bkillockd','XdbRLx2dDU','2000-07-16','124-923-2805','Albania'),('T15','Garry Duckitt','Male','gduckitte','8ukAKM4bmt','1952-10-14','777-519-0078','South Africa'),('T16','Harry Napier','Male','hnapierf','UnRMFu9nE0n','1993-12-09','102-326-3906','France'),('T17','Luce Livett','Male','llivettg','HFrN2fG','1968-06-11','327-862-1900','China'),('T18','Pascale Exelby','Male','pexelbyh','EBxtu9hT','1996-10-27','769-418-7384','Poland'),('T19','Niel Nolin','Male','nnolini','KsOE3IJVnE','1970-04-08','369-159-5898','American'),('T2','Welbie Yanson','Male','wyanson1','IGZ8Mg','1994-06-17','564-126-4785','China'),('T20','Carmelita Sheara','Female','cshearaj','FwkA2wuF','1961-10-30','236-346-3061','Philippines'),('T3','Kyle Trorey','Male','ktrorey2','jRl2lda','1999-12-30','601-277-4619','France'),('T4','Elladine Van Oort','Female','evan3','YZNXkD1GGC','1990-07-07','406-736-7677','American'),('T5','Annadiana Fragino','Female','afragino4','t7vGh0pemj','2004-07-27','721-741-5332','Uzbekistan'),('T6','Yardley Badgers','Male','ybadgers5','zr6UWq','2006-12-26','775-522-7030','Russia'),('T7','Serene Ollerton','Female','sollerton6','6jAHD6BzK','2009-06-14','577-208-7291','Lithuania'),('T8','Ailee Yellep','Female','ayellep7','Spwyo66h','1965-04-30','806-363-8492','American'),('T9','Cati Fearby','Female','cfearby8','M5IpciyzSJK','1986-02-06','689-254-7448','Finland');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


-- Dumping routines for database 'buildingmanagement1'
--
/*!50003 DROP PROCEDURE IF EXISTS `generatebill` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `generatebill`(in lmanager_id varchar(6), in tenant_id varchar(6), in due_date varchar(255))
begin
insert into rentbill(lmanager_id, tenant_id, due_date, status) values(lmanager_id, tenant_id, due_date,'not paid');
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-09 21:36:53
