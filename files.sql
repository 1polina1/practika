-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: files
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `material_type_import`
--

DROP TABLE IF EXISTS `material_type_import`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_type_import` (
  `material_type` text DEFAULT NULL,
  `material_broke` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_type_import`
--

LOCK TABLES `material_type_import` WRITE;
/*!40000 ALTER TABLE `material_type_import` DISABLE KEYS */;
INSERT INTO `material_type_import` VALUES ('Тип материала 1','0,10%'),('Тип материала 2','0,95%'),('Тип материала 3','0,28%'),('Тип материала 4','0,55%'),('Тип материала 5','0,34%');
/*!40000 ALTER TABLE `material_type_import` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partner_products_import`
--

DROP TABLE IF EXISTS `partner_products_import`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partner_products_import` (
  `product_name` text DEFAULT NULL,
  `partner_name` text DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partner_products_import`
--

LOCK TABLES `partner_products_import` WRITE;
/*!40000 ALTER TABLE `partner_products_import` DISABLE KEYS */;
INSERT INTO `partner_products_import` VALUES ('Паркетная доска Ясень темный однополосная 14 мм','База Строитель',15500,'23.03.2023'),('Ламинат Дуб дымчато-белый 33 класс 12 мм','База Строитель',12350,'18.12.2023'),('Ламинат Дуб серый 32 класс 8 мм с фаской','База Строитель',37400,'07.06.2024'),('Инженерная доска Дуб Французская елка однополосная 12 мм','Паркет 29',35000,'02.12.2022'),('Пробковое напольное клеевое покрытие 32 класс 4 мм','Паркет 29',1250,'17.05.2023'),('Ламинат Дуб дымчато-белый 33 класс 12 мм','Паркет 29',1000,'07.06.2024'),('Паркетная доска Ясень темный однополосная 14 мм','Паркет 29',7550,'01.07.2024'),('Паркетная доска Ясень темный однополосная 14 мм','Стройсервис',7250,'22.01.2023'),('Инженерная доска Дуб Французская елка однополосная 12 мм','Стройсервис',2500,'05.07.2024'),('Ламинат Дуб серый 32 класс 8 мм с фаской','Ремонт и отделка',59050,'20.03.2023'),('Ламинат Дуб дымчато-белый 33 класс 12 мм','Ремонт и отделка',37200,'12.03.2024'),('Пробковое напольное клеевое покрытие 32 класс 4 мм','Ремонт и отделка',4500,'14.05.2024'),('Ламинат Дуб дымчато-белый 33 класс 12 мм','МонтажПро',50000,'19.09.2023'),('Ламинат Дуб серый 32 класс 8 мм с фаской','МонтажПро',670000,'10.11.2023'),('Паркетная доска Ясень темный однополосная 14 мм','МонтажПро',35000,'15.04.2024'),('Инженерная доска Дуб Французская елка однополосная 12 мм','МонтажПро',25000,'12.06.2024');
/*!40000 ALTER TABLE `partner_products_import` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partners_import`
--

DROP TABLE IF EXISTS `partners_import`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partners_import` (
  `type` text DEFAULT NULL,
  `partner_name` text DEFAULT NULL,
  `director` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `phone` text DEFAULT NULL,
  `address` text DEFAULT NULL,
  `INN` bigint(20) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partners_import`
--

LOCK TABLES `partners_import` WRITE;
/*!40000 ALTER TABLE `partners_import` DISABLE KEYS */;
INSERT INTO `partners_import` VALUES ('ЗАО','База Строитель','Иванова Александра Ивановна','aleksandraivanova@ml.ru','493 123 45 67','652050, Кемеровская область, город Юрга, ул. Лесная, 15',2222455179,5),('ООО','Паркет 29','Петров Василий Петрович','vppetrov@vl.ru','987 123 56 78','164500, Архангельская область, город Северодвинск, ул. Строителей, 18',3333888520,4),('ПАО','Стройсервис','Соловьев Андрей Николаевич','ansolovev@st.ru','812 223 32 00','188910, Ленинградская область, город Приморск, ул. Парковая, 21',4440391035,6),('ОАО','Ремонт и отделка','Воробьева Василиса Валерьевна','ekaterina.vorobeva@ml.ru','444 222 33 11','143960, Московская область, город Реутов, ул. Свободы, 51',1111520857,7);
/*!40000 ALTER TABLE `partners_import` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_type_import`
--

DROP TABLE IF EXISTS `product_type_import`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_type_import` (
  `Тип продукции` text DEFAULT NULL,
  `Коэффициент типа продукции` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_type_import`
--

LOCK TABLES `product_type_import` WRITE;
/*!40000 ALTER TABLE `product_type_import` DISABLE KEYS */;
INSERT INTO `product_type_import` VALUES ('Ламинат','2,35'),('Массивная доска','5,15'),('Паркетная доска','4,34'),('Пробковое покрытие','1,5'),('',''),('','');
/*!40000 ALTER TABLE `product_type_import` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_import`
--

DROP TABLE IF EXISTS `products_import`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_import` (
  `product_type` text DEFAULT NULL,
  `product_name` text DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `min_price` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_import`
--

LOCK TABLES `products_import` WRITE;
/*!40000 ALTER TABLE `products_import` DISABLE KEYS */;
INSERT INTO `products_import` VALUES ('Ламинат','Ламинат Дуб дымчато-белый 32 класс 12 мм',7750281,'1799,33'),('Ламинат','Ламинат Дуб серый 32 класс 8 мм с фаской',7028748,'3890,41'),('Пробковое покрытие','Пробковое напольное клеевое покрытие 32 класс 4 мм',5012543,'5450,59'),('Ламинат','ШИКАРНЫЙ БЛЕСК',255698,'1689');
/*!40000 ALTER TABLE `products_import` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-20 18:09:09
