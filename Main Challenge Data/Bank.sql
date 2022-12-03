CREATE DATABASE  IF NOT EXISTS `Bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Bank`;
-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: Bank
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `BankAccount`
--

DROP TABLE IF EXISTS `BankAccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BankAccount` (
  `AccountID` int NOT NULL,
  `UserID` int NOT NULL,
  `AccountType` varchar(255) DEFAULT NULL,
  `AccountBalance` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`AccountID`,`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BankAccount`
--

LOCK TABLES `BankAccount` WRITE;
/*!40000 ALTER TABLE `BankAccount` DISABLE KEYS */;
INSERT INTO `BankAccount` VALUES (259555772,4,'Saving',14020.58),(322798030,3,'Multiplier',39740.17),(339657462,4,'Current',47380.33),(353677039,3,'Saving',76660.21),(621156213,1,'Saving',70200.71),(785703027,5,'Current',42460.32),(828120424,2,'Multiplier',50640.12),(958945214,1,'Current',99720.46);
/*!40000 ALTER TABLE `BankAccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ScheduledTransactions`
--

DROP TABLE IF EXISTS `ScheduledTransactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ScheduledTransactions` (
  `TransactionID` int NOT NULL,
  `AccountID` int NOT NULL,
  `ReceivingAccountID` int DEFAULT NULL,
  `Date` varchar(255) DEFAULT NULL,
  `TransactionAmount` decimal(10,2) DEFAULT NULL,
  `Comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`TransactionID`,`AccountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ScheduledTransactions`
--

LOCK TABLES `ScheduledTransactions` WRITE;
/*!40000 ALTER TABLE `ScheduledTransactions` DISABLE KEYS */;
INSERT INTO `ScheduledTransactions` VALUES (1,621156213,339657462,'2022-11-08T04:00:00.000Z',500.00,'Monthly Pocket Money'),(2,958945214,621156213,'2022-11-08T04:00:00.000Z',8996.00,'School Fees'),(3,828120424,322798030,'2022-11-25T04:00:00.000Z',3000.00,'Driving Centre Top-up'),(4,353677039,785703027,'2022-11-17T06:21:00.000Z',255.00,'Tuition Fee Payment'),(5,259555772,828120424,'2022-11-08T04:00:00.000Z',32.00,'Books Payment');
/*!40000 ALTER TABLE `ScheduledTransactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL,
  `Username` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `Firstname` varchar(255) DEFAULT NULL,
  `Lastname` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `OptIntoPhyStatements` bit(1) DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'ExecutiveDBS','DBSBestBank2022','Tom','Lim','TomLim@easymail.com','Block 123 Serangoon Garden #10-129',_binary '\0'),(2,'SeederDBS','iWant2JoinDBS','Mary','Tan','MaryTan@simplemail.com','Block 234 Changi Business Park #50-123',_binary ''),(3,'AcerDBS','Top5Seeder','Gary','Ong','GaryOng@easymail.com','Block 345 Jurong Business Park #25-214',_binary '\0'),(4,'AssociateDBS','Whatis2Years','Harry','Goh','HarryGoh@bestbank.com','Block 456 One North Fusionopolis #34-743',_binary '\0'),(5,'PresidentDBS','Multiplier3.5%','Cheryl','Chia','CherylChia@bestbank.com','Block 567 Marina Bay Sands #63-743',_binary '');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-20 22:55:07
