CREATE DATABASE  IF NOT EXISTS `projekat_2` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `projekat_2`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: projekat_2
-- ------------------------------------------------------
-- Server version	5.7.40

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
-- Table structure for table `admin_types`
--

DROP TABLE IF EXISTS `admin_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_types` (
  `id` varchar(50) NOT NULL,
  `admin_type` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `seniority` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_type` (`admin_type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_types`
--

LOCK TABLES `admin_types` WRITE;
/*!40000 ALTER TABLE `admin_types` DISABLE KEYS */;
INSERT INTO `admin_types` VALUES ('5d6f8ee3-7193-48df-a2f0-04b49b29ec65','Customer','Karen','Senior citizen'),('8cdb67e5-9b84-41e5-92ed-f6293f5cb690','Owner','Waiter','Intern'),('c547f051-ec51-4a3f-ad9d-a70901dcafaf','employee','Barista','Senior');
/*!40000 ALTER TABLE `admin_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `admin_type_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_type_id` (`admin_type_id`),
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`admin_type_id`) REFERENCES `admin_types` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES ('9b8a7f92-7f56-4313-accf-7294fea30d3a','Bojan','Milosavljevic','8cdb67e5-9b84-41e5-92ed-f6293f5cb690');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` varchar(50) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('bab24107-5040-46f8-addd-a8556672fa83','Art'),('fa5dc771-a535-41cf-b9e2-ecb3a8a85919','ITBC'),('55721293-940e-49aa-898f-4b5a3bcc5125','Maths');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `id` varchar(50) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `played_quizzes` int(11) DEFAULT NULL,
  `questions_taken` int(11) DEFAULT NULL,
  `correct_answers` int(11) DEFAULT NULL,
  `incorrect_answers` int(11) DEFAULT NULL,
  `num_of_achievements` int(11) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES ('01709922-e9a6-45c5-a128-bc1336ac448a','AlekiBolek',2,20,4,16,0,'6db0a022-9ec9-4253-8797-a280d0ef0097'),('4f4e7440-f387-4037-8c09-20541dbff4be','VeljanZmaj',0,0,0,0,0,'ec1b9028-d6ac-4d11-b535-236c085e9dc9'),('7c4a1f81-988b-4188-80e0-0a04b8d67cda','MancheBojanche',2,20,5,15,0,'2ae15f5c-6f95-43aa-b4f6-47e012b11a75');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `q_and_as`
--

DROP TABLE IF EXISTS `q_and_as`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `q_and_as` (
  `id` varchar(50) NOT NULL,
  `quiz_id` varchar(50) NOT NULL,
  `question_id` varchar(50) NOT NULL,
  `player1_answer` varchar(50) DEFAULT NULL,
  `player2_answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `quiz_id` (`quiz_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `q_and_as_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`),
  CONSTRAINT `q_and_as_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `q_and_as`
--

LOCK TABLES `q_and_as` WRITE;
/*!40000 ALTER TABLE `q_and_as` DISABLE KEYS */;
INSERT INTO `q_and_as` VALUES ('15996e50-64df-4b53-b496-2458a731b525','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','e9695fca-9de5-40e6-a21e-58188609290e','a','c'),('3386b9b9-7388-4880-a30c-f5042d0c470d','3dacd7ab-c7da-489c-a644-0dbadca81643','58f16c8e-3447-417e-8c6d-8d0561f780d7','',''),('33ba8ecb-5cc3-41aa-b005-c6ec919716a2','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','d36a070b-28d0-44a7-941f-2299ef4cf9fd','b','a'),('6ac5aaf2-7535-4d98-ab04-ada5b2fa22f2','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','445aa4be-ca22-4438-a909-63e7d86fbf4f','c','c'),('aa79209e-1a0b-4a03-9f39-d0eadb9ce742','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','ce190926-cdec-451e-a192-839ec0662959','d','c'),('b5f9afcf-9bcf-48e6-be49-325fc638d672','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','119012a4-94a3-497e-9be2-d8c50ee8e675','c','c'),('c0adb31a-0c1e-479e-859b-d64869570e07','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','eb3108f7-5135-4134-9e01-ccb85d96133a','c','c'),('cfed28a4-0d66-4699-9ce3-00a2d4ae0294','3dacd7ab-c7da-489c-a644-0dbadca81643','ce190926-cdec-451e-a192-839ec0662959','',''),('e70383db-2e88-46ee-a33e-c7aedd279e1f','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','88e7d9a0-0ee0-422b-834d-db0268a28c85','a','c'),('eeb959fc-b36c-46e7-b136-c8a7ac6b4072','3dacd7ab-c7da-489c-a644-0dbadca81643','01d1ce6e-4517-424e-97d2-d343aea1fe4d','',''),('f3a2ae98-ed80-41d8-9190-29987d84ed37','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','cfd91f8b-b214-4cab-a61b-d7255977e492','a','c'),('f7e38dc9-4099-47b2-816c-64d8568ed66a','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','f9c7129f-b19c-4429-a136-4bd83a4eb7bd','b','a'),('f946f992-1b79-49a4-93a2-55b4712a386c','3dacd7ab-c7da-489c-a644-0dbadca81643','992c0759-cc57-4dfc-af3c-1787a7147fc1','',''),('fe5960c7-3c4e-42e5-af80-e46fb6de8091','4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','37b88227-cf1f-4a56-abd4-a4de04bacda3','c','c');
/*!40000 ALTER TABLE `q_and_as` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` varchar(50) NOT NULL,
  `text` varchar(100) DEFAULT NULL,
  `answer_a` varchar(100) DEFAULT NULL,
  `answer_b` varchar(100) DEFAULT NULL,
  `answer_c` varchar(100) DEFAULT NULL,
  `answer_d` varchar(100) DEFAULT NULL,
  `correct_answer` varchar(100) DEFAULT NULL,
  `category_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES ('01d1ce6e-4517-424e-97d2-d343aea1fe4d','Koliko ce poena Dragan imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('0aef766c-30bd-460d-893c-d7abb7185057','Koliko ce poena Dimi imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('0ed9b5c5-a0d2-431a-aada-2daebdf5ea69','Koliko ce poena Alek imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('119012a4-94a3-497e-9be2-d8c50ee8e675','Koliko ce poena Maja imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('129f1b01-522b-4636-8731-08d7c08785f2','Koliko ce poena Andrija imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('2927fc15-f82b-42f0-a89d-e3c5ade74fbb','Koliko ce poena Ema imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('2d57a956-d185-48d2-a24b-80e0e98746d0','Koliko ce poena Nikolina Cerka imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('2e154d8e-e6d3-4880-adef-59f651b37cc9','Koliko ce poena Milan imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('37b88227-cf1f-4a56-abd4-a4de04bacda3','Koliko ce poena Branko imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('445aa4be-ca22-4438-a909-63e7d86fbf4f','Koliko ce poena Tamara imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('4ea46e81-8296-430d-8b7e-b86f620a5322','Koliko ce poena Borisova Beba imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('58f16c8e-3447-417e-8c6d-8d0561f780d7','Koliko ce poena Veljko imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('76679719-14de-4516-a1c1-05ceeb935695','Koliko ce poena Ivan K imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('88e7d9a0-0ee0-422b-834d-db0268a28c85','Koliko ce poena Toma imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('8c3cf607-30e9-4ec2-9ea4-fd40c21a9fd2','Koliko ce poena Ivan T imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('992c0759-cc57-4dfc-af3c-1787a7147fc1','Koliko ce poena Milena HR imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('ce190926-cdec-451e-a192-839ec0662959','Koliko ce poena Vuk imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('cfd91f8b-b214-4cab-a61b-d7255977e492','Koliko ce poena Mihajlo imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('d36a070b-28d0-44a7-941f-2299ef4cf9fd','Koliko ce poena Danka imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('d3fab9ec-56eb-4713-9be7-e54fe0155384','Koliko ce poena Nikola imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','fa5dc771-a535-41cf-b9e2-ecb3a8a85919'),('e1369930-40a5-46ba-b292-e7f80fb45b86','Koliko ce poena Bojana imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('e9695fca-9de5-40e6-a21e-58188609290e','Koliko ce poena Milos imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('eb3108f7-5135-4134-9e01-ccb85d96133a','Koliko ce poena Boris imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('ee0b5477-2080-4269-9b2a-d3a7fda60922','Koliko ce poena Vladimir imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83'),('f9c7129f-b19c-4429-a136-4bd83a4eb7bd','Koliko ce poena Bojan imati na projektu?','nedovoljno','dovoljno','65','Iskr poprilicno lose al ae','a','bab24107-5040-46f8-addd-a8556672fa83');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quizzes`
--

DROP TABLE IF EXISTS `quizzes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quizzes` (
  `id` varchar(50) NOT NULL,
  `player1` varchar(50) NOT NULL,
  `player2` varchar(50) NOT NULL,
  `player1_time` int(11) DEFAULT NULL,
  `player2_time` int(11) DEFAULT NULL,
  `player1_score` int(11) DEFAULT NULL,
  `player2_score` int(11) DEFAULT NULL,
  `winner` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player1` (`player1`),
  KEY `player2` (`player2`),
  CONSTRAINT `quizzes_ibfk_1` FOREIGN KEY (`player1`) REFERENCES `players` (`username`),
  CONSTRAINT `quizzes_ibfk_2` FOREIGN KEY (`player2`) REFERENCES `players` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quizzes`
--

LOCK TABLES `quizzes` WRITE;
/*!40000 ALTER TABLE `quizzes` DISABLE KEYS */;
INSERT INTO `quizzes` VALUES ('3dacd7ab-c7da-489c-a644-0dbadca81643','MancheBojanche','VeljanZmaj',0,0,NULL,NULL,'','Pending'),('4bbc0960-d973-4f67-b2a7-bf8eeb15ca2d','MancheBojanche','AlekiBolek',0,0,3,2,'MancheBojanche','Pending');
/*!40000 ALTER TABLE `quizzes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2ae15f5c-6f95-43aa-b4f6-47e012b11a75','boki@gmail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0),('6db0a022-9ec9-4253-8797-a280d0ef0097','alek@gmail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0),('b544b234-b078-4d69-9632-5ffffa7f1dbc','tatamate@itbc.org','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,1),('d9e27642-680f-4026-889d-d5be286d3776','miha@gmail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0),('ec1b9028-d6ac-4d11-b535-236c085e9dc9','velja@gmail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-23 13:10:54
