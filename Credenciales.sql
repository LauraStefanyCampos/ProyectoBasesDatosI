/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `proyectobd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proyectobd`;

CREATE TABLE IF NOT EXISTS `agentes` (
  `AG_NoID` int unsigned NOT NULL AUTO_INCREMENT,
  `AG_Nombre` varchar(50) DEFAULT NULL,
  `AG_Direccion` tinytext,
  `AG_Celular` bigint unsigned DEFAULT NULL,
  `AG_TelefonoOficina` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`AG_NoID`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `agentes_bitacora` (
  `AG_BIT_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `AG_BIT_FECHA` date DEFAULT NULL,
  `AG_BIT_ExecutedSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `AG_BIT_ReverseSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`AG_BIT_ID`),
  KEY `AG_BIT_FECHA` (`AG_BIT_FECHA`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `compradores` (
  `CP_NoID` int unsigned NOT NULL,
  `CP_Nombre` varchar(50) DEFAULT NULL,
  `CP_Direccion` tinytext,
  `CP_Celular` int unsigned DEFAULT NULL,
  PRIMARY KEY (`CP_NoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `compradores_bitacora` (
  `CP_BIT_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `CP_BIT_FECHA` date DEFAULT NULL,
  `CP_BIT_ExecutedSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `CP_BIT_ReverseSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`CP_BIT_ID`),
  KEY `CP_BIT_FECHA` (`CP_BIT_FECHA`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `credenciales` (
  `Nombre_Usuario_Agentes` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Id_Nombre_Usuarios` int NOT NULL AUTO_INCREMENT,
  `Nombre_Usuario_Vendedores` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Nombre_Usuario_Compradores` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Nivel_Acceso` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`Id_Nombre_Usuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `propiedades_en_mercado` (
  `PEM_IDPropiedad` smallint unsigned DEFAULT NULL,
  `PEM_Nombre` varchar(50) DEFAULT NULL,
  `PEM_Ciudad` varchar(50) DEFAULT NULL,
  `PEM_Direccion` tinytext,
  `PEM_CantidadDormitorios` tinyint unsigned DEFAULT NULL,
  `PEM_Caracteristicas` text,
  `PEM_Precio` mediumint unsigned DEFAULT NULL,
  `PEM_FechaPublicacion` date DEFAULT NULL,
  `PEM_AG_NoID` int unsigned DEFAULT NULL,
  `PEM__VD_NoID` int unsigned DEFAULT NULL,
  KEY `FK_propiedades_en_mercado_vendedores` (`PEM__VD_NoID`),
  KEY `FK_propiedades_en_mercado_agentes` (`PEM_AG_NoID`),
  CONSTRAINT `FK_propiedades_en_mercado_agentes` FOREIGN KEY (`PEM_AG_NoID`) REFERENCES `agentes` (`AG_NoID`),
  CONSTRAINT `FK_propiedades_en_mercado_vendedores` FOREIGN KEY (`PEM__VD_NoID`) REFERENCES `vendedores` (`VD_NoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `propiedades_en_mercado_bitacora` (
  `PEM_BIT_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `PEM_BIT_FECHA` date DEFAULT NULL,
  `PEM_BIT_ExecutedSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `PEM_BIT_ReverseSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`PEM_BIT_ID`),
  KEY `PEM_BIT_FECHA` (`PEM_BIT_FECHA`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `propiedades_vendidas` (
  `PV_IDPropiedad` int unsigned NOT NULL,
  `PV_Nombre` varchar(50) DEFAULT NULL,
  `PV_Ciudad` varchar(50) DEFAULT NULL,
  `PV_Direccion` tinytext,
  `PV_CantidadDormitorios` tinyint unsigned DEFAULT NULL,
  `PV_Caracteristicas` tinytext,
  `PV_Precio` mediumint unsigned DEFAULT NULL,
  `PV_FechaPublicacion` date DEFAULT NULL,
  `PV_FechaVenta` date DEFAULT NULL,
  `PV_AG_NoID` int unsigned DEFAULT NULL,
  `PV_VD_NoID` int unsigned DEFAULT NULL,
  `PV_ComisionVenta` int unsigned DEFAULT NULL,
  `PV_CP_NoID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`PV_IDPropiedad`),
  KEY `FK_propiedades_vendidas_compradores` (`PV_CP_NoID`),
  KEY `FK_propiedades_vendidas_vendedores` (`PV_VD_NoID`),
  KEY `FK_propiedades_vendidas_agentes` (`PV_AG_NoID`),
  KEY `PV_Ciudad` (`PV_Ciudad`),
  KEY `PV_CantidadDormitorios` (`PV_CantidadDormitorios`),
  KEY `PV_Precio` (`PV_Precio`),
  CONSTRAINT `FK_propiedades_vendidas_agentes` FOREIGN KEY (`PV_AG_NoID`) REFERENCES `agentes` (`AG_NoID`),
  CONSTRAINT `FK_propiedades_vendidas_compradores` FOREIGN KEY (`PV_CP_NoID`) REFERENCES `compradores` (`CP_NoID`),
  CONSTRAINT `FK_propiedades_vendidas_vendedores` FOREIGN KEY (`PV_VD_NoID`) REFERENCES `vendedores` (`VD_NoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `propiedades_vendidas_bitacora` (
  `PV_BIT_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `PV_BIT_FECHA` date DEFAULT NULL,
  `PV_BIT_ExecutedSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `PV_BIT_ReverseSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`PV_BIT_ID`),
  KEY `PV_BIT_FECHA` (`PV_BIT_FECHA`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `vendedores` (
  `VD_NoID` int unsigned NOT NULL,
  `VD_Nombre` varchar(50) NOT NULL,
  `VD_Direccion` tinytext NOT NULL,
  `VD_Celular` int unsigned DEFAULT NULL,
  PRIMARY KEY (`VD_NoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `vendedores_bitacora` (
  `VD_BIT_ID` int unsigned NOT NULL AUTO_INCREMENT,
  `VD_BIT_FECHA` date DEFAULT NULL,
  `VD_BIT_ExecutedSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `VD_BIT_ReverseSQL` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`VD_BIT_ID`),
  KEY `VD_BIT_FECHA` (`VD_BIT_FECHA`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `compras_por_comprador` (
	`CP_NoID` INT(10) UNSIGNED NOT NULL,
	`CP_Nombre` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Total_Compras` BIGINT(19) NOT NULL
) ENGINE=MyISAM;

CREATE TABLE `total_ventas_agentes_año` (
	`Año` INT(10) NULL,
	`ID_Agente` INT(10) UNSIGNED NOT NULL,
	`Nombre_Agente` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Cantidad_Propiedades_Vendidas` BIGINT(19) NOT NULL
) ENGINE=MyISAM;

CREATE TABLE `ventas_por_agente` (
	`AG_NoID` INT(10) UNSIGNED NOT NULL,
	`AG_Nombre` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Total_Ventas` BIGINT(19) NOT NULL
) ENGINE=MyISAM;

CREATE TABLE `ventas_por_cantidad_de_habitaciones` (
	`PV_IDPropiedad` INT(10) UNSIGNED NOT NULL,
	`PV_Nombre` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Ciudad` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Direccion` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_CantidadDormitorios` TINYINT(3) UNSIGNED NULL,
	`PV_Caracteristicas` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Precio` MEDIUMINT(7) UNSIGNED NULL,
	`PV_FechaPublicacion` DATE NULL,
	`PV_FechaVenta` DATE NULL,
	`PV_AG_NoID` INT(10) UNSIGNED NULL,
	`PV_VD_NoID` INT(10) UNSIGNED NULL,
	`PV_ComisionVenta` INT(10) UNSIGNED NULL,
	`PV_CP_NoID` INT(10) UNSIGNED NULL
) ENGINE=MyISAM;

CREATE TABLE `ventas_por_precio_propiedad` (
	`PV_IDPropiedad` INT(10) UNSIGNED NOT NULL,
	`PV_Nombre` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Ciudad` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Direccion` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_CantidadDormitorios` TINYINT(3) UNSIGNED NULL,
	`PV_Caracteristicas` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Precio` MEDIUMINT(7) UNSIGNED NULL,
	`PV_FechaPublicacion` DATE NULL,
	`PV_FechaVenta` DATE NULL,
	`PV_AG_NoID` INT(10) UNSIGNED NULL,
	`PV_VD_NoID` INT(10) UNSIGNED NULL,
	`PV_ComisionVenta` INT(10) UNSIGNED NULL,
	`PV_CP_NoID` INT(10) UNSIGNED NULL
) ENGINE=MyISAM;

CREATE TABLE `ventas_por_ubicacion` (
	`PV_IDPropiedad` INT(10) UNSIGNED NOT NULL,
	`PV_Nombre` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Ciudad` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Direccion` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_CantidadDormitorios` TINYINT(3) UNSIGNED NULL,
	`PV_Caracteristicas` TINYTEXT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PV_Precio` MEDIUMINT(7) UNSIGNED NULL,
	`PV_FechaPublicacion` DATE NULL,
	`PV_FechaVenta` DATE NULL,
	`PV_AG_NoID` INT(10) UNSIGNED NULL,
	`PV_VD_NoID` INT(10) UNSIGNED NULL,
	`PV_ComisionVenta` INT(10) UNSIGNED NULL,
	`PV_CP_NoID` INT(10) UNSIGNED NULL
) ENGINE=MyISAM;

CREATE TABLE `ventas_por_vendedor` (
	`VD_NoID` INT(10) UNSIGNED NOT NULL,
	`VD_Nombre` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Total_ventas` BIGINT(19) NOT NULL
) ENGINE=MyISAM;

DELIMITER //
CREATE PROCEDURE `CrearComprador`(
    IN p_nombre VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_celular INT
)
BEGIN
    INSERT INTO compradores (CP_Nombre, CP_Direccion, CP_Celular)
    VALUES (p_nombre, p_direccion, p_celular);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `CrearPropiedadEnMercado`(
    IN p_nombre VARCHAR(50),
    IN p_ciudad VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_cantidad_dormitorios TINYINT,
    IN p_caracteristicas TEXT,
    IN p_precio MEDIUMINT,
    IN p_fecha_publicacion DATE,
    IN p_agente_id INT,
    IN p_vendedor_id INT
)
BEGIN
    INSERT INTO propiedades_en_mercado (PEM_Nombre, PEM_Ciudad, PEM_Direccion, PEM_CantidadDormitorios, PEM_Caracteristicas, PEM_Precio, PEM_FechaPublicacion, PEM_AG_NoID, PEM__VD_NoID)
    VALUES (p_nombre, p_ciudad, p_direccion, p_cantidad_dormitorios, p_caracteristicas, p_precio, p_fecha_publicacion, p_agente_id, p_vendedor_id);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `CrearPropiedadVendida`(
    IN p_nombre VARCHAR(50),
    IN p_ciudad VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_cantidad_dormitorios TINYINT,
    IN p_caracteristicas TINYTEXT,
    IN p_precio MEDIUMINT,
    IN p_fecha_publicacion DATE,
    IN p_fecha_venta DATE,
    IN p_agente_id INT,
    IN p_vendedor_id INT,
    IN p_comision_venta INT,
    IN p_comprador_id INT
)
BEGIN
    INSERT INTO propiedades_vendidas (PV_Nombre, PV_Ciudad, PV_Direccion, PV_CantidadDormitorios, PV_Caracteristicas, PV_Precio, PV_FechaPublicacion, PV_FechaVenta, PV_AG_NoID, PV_VD_NoID, PV_ComisionVenta, PV_CP_NoID)
    VALUES (p_nombre, p_ciudad, p_direccion, p_cantidad_dormitorios, p_caracteristicas, p_precio, p_fecha_publicacion, p_fecha_venta, p_agente_id, p_vendedor_id, p_comision_venta, p_comprador_id);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `crear_agente`(
    IN p_nombre VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_celular BIGINT UNSIGNED,
    IN p_telefono_oficina BIGINT UNSIGNED
)
BEGIN
    INSERT INTO agentes (AG_Nombre, AG_Direccion, AG_Celular, AG_TelefonoOficina)
    VALUES (p_nombre, p_direccion, p_celular, p_telefono_oficina);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `EliminarComprador`(
    IN p_id_comprador INT
)
BEGIN
    DELETE FROM compradores WHERE CP_NoID = p_id_comprador;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `EliminarPropiedadEnMercado`(
    IN p_id_propiedad INT
)
BEGIN
    DELETE FROM propiedades_en_mercado WHERE PEM_IDPropiedad = p_id_propiedad;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `EliminarPropiedadVendida`(
    IN p_id_propiedad INT
)
BEGIN
    DELETE FROM propiedades_vendidas WHERE PV_IDPropiedad = p_id_propiedad;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `eliminar_agente`(
    IN p_id_agente INT UNSIGNED
)
BEGIN
    DELETE FROM agentes WHERE AG_NoID = p_id_agente;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `ModificarComprador`(
    IN p_id_comprador INT,
    IN p_nombre VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_celular INT
)
BEGIN
    UPDATE compradores
    SET CP_Nombre = p_nombre,
        CP_Direccion = p_direccion,
        CP_Celular = p_celular
    WHERE CP_NoID = p_id_comprador;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `ModificarPropiedadEnMercado`(
    IN p_id_propiedad INT,
    IN p_nombre VARCHAR(50),
    IN p_ciudad VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_cantidad_dormitorios TINYINT,
    IN p_caracteristicas TEXT,
    IN p_precio MEDIUMINT,
    IN p_fecha_publicacion DATE,
    IN p_agente_id INT,
    IN p_vendedor_id INT
)
BEGIN
    UPDATE propiedades_en_mercado
    SET PEM_Nombre = p_nombre,
        PEM_Ciudad = p_ciudad,
        PEM_Direccion = p_direccion,
        PEM_CantidadDormitorios = p_cantidad_dormitorios,
        PEM_Caracteristicas = p_caracteristicas,
        PEM_Precio = p_precio,
        PEM_FechaPublicacion = p_fecha_publicacion,
        PEM_AG_NoID = p_agente_id,
        PEM__VD_NoID = p_vendedor_id
    WHERE PEM_IDPropiedad = p_id_propiedad;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `ModificarPropiedadVendida`(
    IN p_id_propiedad INT,
    IN p_nombre VARCHAR(50),
    IN p_ciudad VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_cantidad_dormitorios TINYINT,
    IN p_caracteristicas TINYTEXT,
    IN p_precio MEDIUMINT,
    IN p_fecha_publicacion DATE,
    IN p_fecha_venta DATE,
    IN p_agente_id INT,
    IN p_vendedor_id INT,
    IN p_comision_venta INT,
    IN p_comprador_id INT
)
BEGIN
    UPDATE propiedades_vendidas
    SET PV_Nombre = p_nombre,
        PV_Ciudad = p_ciudad,
        PV_Direccion = p_direccion,
        PV_CantidadDormitorios = p_cantidad_dormitorios,
        PV_Caracteristicas = p_caracteristicas,
        PV_Precio = p_precio,
        PV_FechaPublicacion = p_fecha_publicacion,
        PV_FechaVenta = p_fecha_venta,
        PV_AG_NoID = p_agente_id,
        PV_VD_NoID = p_vendedor_id,
        PV_ComisionVenta = p_comision_venta,
        PV_CP_NoID = p_comprador_id
    WHERE PV_IDPropiedad = p_id_propiedad;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `modificar_agente`(
    IN p_id_agente INT UNSIGNED,
    IN p_nombre VARCHAR(50),
    IN p_direccion TINYTEXT,
    IN p_celular BIGINT UNSIGNED,
    IN p_telefono_oficina BIGINT UNSIGNED
)
BEGIN
    UPDATE agentes
    SET AG_Nombre = p_nombre,
        AG_Direccion = p_direccion,
        AG_Celular = p_celular,
        AG_TelefonoOficina = p_telefono_oficina
    WHERE AG_NoID = p_id_agente;
END//
DELIMITER ;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_delete_agentes` AFTER DELETE ON `agentes` FOR EACH ROW BEGIN
		INSERT INTO agentes_bitacora (AG_BIT_FECHA, AG_BIT_ExecutedSQL, AG_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("DELETE FROM agentes where AG_NoID = ", OLD.AG_NoID,";"),
			CONCAT("INSERT INTO agentes(AG_NoID, AG_Nombre, AG_Direccion, AG_Celular, AG_TelefonoOficina) VALUES ( ", OLD.AG_NoID, ", """,OLD.AG_Nombre,""", """,OLD.AG_Direccion,""", """,OLD.AG_Celular,""", ",OLD.AG_TelefonoOficina,");")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_delete_compradores` AFTER DELETE ON `compradores` FOR EACH ROW BEGIN
    INSERT INTO compradores_bitacora (CP_BIT_FECHA, CP_BIT_ExecutedSQL, CP_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('DELETE FROM compradores WHERE CP_NoID = ', OLD.CP_NoID, ';'),
        CONCAT('INSERT INTO compradores (CP_NoID, CP_Nombre, CP_Direccion, CP_Celular) VALUES (', OLD.CP_NoID, ', "', OLD.CP_Nombre, '", "', OLD.CP_Direccion, '", ', OLD.CP_Celular, ');')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_delete_propiedades_en_mercado` AFTER DELETE ON `propiedades_en_mercado` FOR EACH ROW BEGIN
    INSERT INTO propiedades_en_mercado_bitacora (PEM_BIT_FECHA, PEM_BIT_ExecutedSQL, PEM_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('DELETE FROM propiedades_en_mercado WHERE PEM_IDPropiedad = ', OLD.PEM_IDPropiedad, ';'),
        CONCAT('INSERT INTO propiedades_en_mercado (PEM_IDPropiedad, PEM_Nombre, PEM_Ciudad, PEM_Direccion, PEM_CantidadDormitorios, PEM_Caracteristicas, PEM_Precio, PEM_FechaPublicacion, PEM_AG_NoID, PEM__VD_NoID) VALUES (', OLD.PEM_IDPropiedad, ', "', OLD.PEM_Nombre, '", "', OLD.PEM_Ciudad, '", "', OLD.PEM_Direccion, '", ', OLD.PEM_CantidadDormitorios, ', "', OLD.PEM_Caracteristicas, '", ', OLD.PEM_Precio, ', "', OLD.PEM_FechaPublicacion, '", ', OLD.PEM_AG_NoID, ', ', OLD.PEM__VD_NoID, ');')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_delete_propiedades_vendidas` AFTER DELETE ON `propiedades_vendidas` FOR EACH ROW BEGIN
    INSERT INTO propiedades_vendidas_bitacora (PV_BIT_FECHA, PV_BIT_ExecutedSQL, PV_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('DELETE FROM propiedades_vendidas WHERE PV_IDPropiedad = ', OLD.PV_IDPropiedad, ';'),
        CONCAT('INSERT INTO propiedades_vendidas (PV_IDPropiedad, PV_Nombre, PV_Ciudad, PV_Direccion, PV_CantidadDormitorios, PV_Caracteristicas, PV_Precio, PV_FechaPublicacion, PV_FechaVenta, PV_AG_NoID, PV_VD_NoID, PV_ComisionVenta, PV_CP_NoID) VALUES (', OLD.PV_IDPropiedad, ', "', OLD.PV_Nombre, '", "', OLD.PV_Ciudad, '", "', OLD.PV_Direccion, '", ', OLD.PV_CantidadDormitorios, ', "', OLD.PV_Caracteristicas, '", ', OLD.PV_Precio, ', "', OLD.PV_FechaPublicacion, '", "', OLD.PV_FechaVenta, '", ', OLD.PV_AG_NoID, ', ', OLD.PV_VD_NoID, ', ', OLD.PV_ComisionVenta, ', ', OLD.PV_CP_NoID, ');')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_delete_vendedores` AFTER DELETE ON `vendedores` FOR EACH ROW BEGIN
		INSERT INTO vendedores_bitacora (VD_BIT_FECHA, VD_BIT_ExecutedSQL, VD_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("DELETE FROM vendedores where VD_NoID = ", OLD.VD_NoID,";"),
			CONCAT("INSERT INTO vendedores(VD_NoID, VD_Nombre, VD_Direccion, VD_Celular) VALUES ( ", OLD.VD_NoID, ", """,OLD.VD_Nombre,""", """,OLD.VD_Direccion,""", ",OLD.VD_Celular,");")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_agentes` AFTER INSERT ON `agentes` FOR EACH ROW BEGIN
		INSERT INTO agentes_bitacora (AG_BIT_FECHA, AG_BIT_ExecutedSQL, AG_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("INSERT INTO agentes(AG_NoID, AG_Nombre, AG_Direccion, AG_Celular, AG_TelefonoOficina) VALUES ( ", NEW.AG_NoID, ", """,NEW.AG_Nombre,""", """,NEW.AG_Direccion,""", """,NEW.AG_Celular,""", ",NEW.AG_TelefonoOficina,");"),
			CONCAT("DELETE FROM agentes where AG_NoID = ", NEW.AG_NoID,";")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_agentes_2` AFTER INSERT ON `agentes` FOR EACH ROW BEGIN
    DECLARE random_password VARCHAR(50);

    -- Generar una contraseña aleatoria
    SET random_password = SUBSTR(MD5(RAND()), 1, 8);  -- Genera una contraseña aleatoria de 8 caracteres
    
    -- Insertar un nuevo registro en la tabla `credenciales`
    INSERT INTO credenciales (
        Nombre_Usuario_Agentes,
        Nombre_Usuario_Vendedores,
        Nombre_Usuario_Compradores,
        Password,
        Nivel_Acceso
    ) VALUES (
        NEW.AG_Nombre,  -- El nombre del agente recién insertado
        NULL,  -- Usuario vendedor es NULL
        NULL,  -- Usuario comprador es NULL
        random_password,  -- Contraseña aleatoria generada
        1  -- Nivel de acceso es 1
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_compradores` AFTER INSERT ON `compradores` FOR EACH ROW BEGIN
    INSERT INTO compradores_bitacora (CP_BIT_FECHA, CP_BIT_ExecutedSQL, CP_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('INSERT INTO compradores (CP_NoID, CP_Nombre, CP_Direccion, CP_Celular) VALUES (', NEW.CP_NoID, ', "', NEW.CP_Nombre, '", "', NEW.CP_Direccion, '", ', NEW.CP_Celular, ');'),
        CONCAT('DELETE FROM compradores WHERE CP_NoID = ', NEW.CP_NoID, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_compradores_2` AFTER INSERT ON `compradores` FOR EACH ROW BEGIN
    DECLARE random_password VARCHAR(50);

    -- Generar una contraseña aleatoria
    SET random_password = SUBSTR(MD5(RAND()), 1, 8);  -- Genera una contraseña aleatoria de 8 caracteres
    
    -- Insertar un nuevo registro en la tabla `credenciales`
    INSERT INTO credenciales (
        Nombre_Usuario_Agentes,
        Nombre_Usuario_Vendedores,
        Nombre_Usuario_Compradores,
        Password,
        Nivel_Acceso
    ) VALUES (
        NULL	,  -- El nombre del agente recién insertado
        NULL,  -- Usuario vendedor es NULL
        NEW.CP_Nombre,  -- Usuario comprador es NULL
        random_password,  -- Contraseña aleatoria generada
        3  -- Nivel de acceso es 1
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_propiedades_en_mercado` AFTER INSERT ON `propiedades_en_mercado` FOR EACH ROW BEGIN
    INSERT INTO propiedades_en_mercado_bitacora (PEM_BIT_FECHA, PEM_BIT_ExecutedSQL, PEM_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('INSERT INTO propiedades_en_mercado (PEM_IDPropiedad, PEM_Nombre, PEM_Ciudad, PEM_Direccion, PEM_CantidadDormitorios, PEM_Caracteristicas, PEM_Precio, PEM_FechaPublicacion, PEM_AG_NoID, PEM__VD_NoID) VALUES (', NEW.PEM_IDPropiedad, ', "', NEW.PEM_Nombre, '", "', NEW.PEM_Ciudad, '", "', NEW.PEM_Direccion, '", ', NEW.PEM_CantidadDormitorios, ', "', NEW.PEM_Caracteristicas, '", ', NEW.PEM_Precio, ', "', NEW.PEM_FechaPublicacion, '", ', NEW.PEM_AG_NoID, ', ', NEW.PEM__VD_NoID, ');'),
        CONCAT('DELETE FROM propiedades_en_mercado WHERE PEM_IDPropiedad = ', NEW.PEM_IDPropiedad, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_propiedades_vendidas` AFTER INSERT ON `propiedades_vendidas` FOR EACH ROW BEGIN
    INSERT INTO propiedades_vendidas_bitacora (PV_BIT_FECHA, PV_BIT_ExecutedSQL, PV_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('INSERT INTO propiedades_vendidas (PV_IDPropiedad, PV_Nombre, PV_Ciudad, PV_Direccion, PV_CantidadDormitorios, PV_Caracteristicas, PV_Precio, PV_FechaPublicacion, PV_FechaVenta, PV_AG_NoID, PV_VD_NoID, PV_ComisionVenta, PV_CP_NoID) VALUES (', NEW.PV_IDPropiedad, ', "', NEW.PV_Nombre, '", "', NEW.PV_Ciudad, '", "', NEW.PV_Direccion, '", ', NEW.PV_CantidadDormitorios, ', "', NEW.PV_Caracteristicas, '", ', NEW.PV_Precio, ', "', NEW.PV_FechaPublicacion, '", "', NEW.PV_FechaVenta, '", ', NEW.PV_AG_NoID, ', ', NEW.PV_VD_NoID, ', ', NEW.PV_ComisionVenta, ', ', NEW.PV_CP_NoID, ');'),
        CONCAT('DELETE FROM propiedades_vendidas WHERE PV_IDPropiedad = ', NEW.PV_IDPropiedad, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_vendedores` AFTER INSERT ON `vendedores` FOR EACH ROW BEGIN
		INSERT INTO vendedores_bitacora (VD_BIT_FECHA, VD_BIT_ExecutedSQL, VD_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("INSERT INTO vendedores(VD_NoID, VD_Nombre, VD_Direccion, VD_Celular) VALUES ( ", NEW.VD_NoID, ", """,NEW.VD_Nombre,""", """,NEW.VD_Direccion,""", """,NEW.VD_Celular,");"),
			CONCAT("DELETE FROM vendedores where VD_NoID = ", NEW.VD_NoID,";")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_insert_vendedores_2` AFTER INSERT ON `vendedores` FOR EACH ROW BEGIN
    DECLARE random_password VARCHAR(50);

    -- Generar una contraseña aleatoria
    SET random_password = SUBSTR(MD5(RAND()), 1, 8);  -- Genera una contraseña aleatoria de 8 caracteres
    
    -- Insertar un nuevo registro en la tabla `credenciales`
    INSERT INTO credenciales (
        Nombre_Usuario_Agentes,
        Nombre_Usuario_Vendedores,
        Nombre_Usuario_Compradores,
        Password,
        Nivel_Acceso
    ) VALUES (
        NULL	,  -- El nombre del agente recién insertado
        NEW.VD_Nombre,  -- Usuario vendedor es NULL
        NULL,  -- Usuario comprador es NULL
        random_password,  -- Contraseña aleatoria generada
        2  -- Nivel de acceso es 1
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_updates_vendedores` AFTER UPDATE ON `vendedores` FOR EACH ROW BEGIN
		INSERT INTO vendedores_bitacora (VD_BIT_FECHA, VD_BIT_ExecutedSQL, VD_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("UPDATE vendedores  SET VD_NoID = ",NEW.VD_NoID,", VD_Nombre = """,NEW.VD_Nombre,""", VD_Direccion = """,NEW.VD_Direccion,""", VD_Celular = ",NEW.VD_Celular,"  WHERE VD_NoID = ", NEW.VD_NoID,";"),
			CONCAT("UPDATE vendedores  SET VD_NoID = ",OLD.VD_NoID,", VD_Nombre = """,OLD.VD_Nombre,""", VD_Direccion = """,OLD.VD_Direccion,""", VD_Celular = ",OLD.VD_Celular,"  WHERE VD_NoID = ", OLD.VD_NoID,";")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_update_agentes` AFTER UPDATE ON `agentes` FOR EACH ROW BEGIN
		INSERT INTO agentes_bitacora (AG_BIT_FECHA, AG_BIT_ExecutedSQL, AG_BIT_ReverseSQL)
		VALUES(
			NOW(),
			CONCAT("UPDATE agentes SET AG_NoID = ",NEW.AG_NoID,", AG_Nombre = """,NEW.AG_Nombre,""", AG_Direccion = """,NEW.AG_Direccion,""", AG_Celular = """,NEW.AG_Celular,""", AG_TelefonoOficina = ", NEW.AG_TelefonoOficina,"  WHERE AG_NoID = ", NEW.AG_NoID,";"),
			CONCAT("UPDATE agentes SET AG_NoID = ",OLD.AG_NoID,", AG_Nombre = """,OLD.AG_Nombre,""", AG_Direccion = """,OLD.AG_Direccion,""", AG_Celular = """,OLD.AG_Celular,""", AG_TelefonoOficina = ", OLD.AG_TelefonoOficina,"  WHERE AG_NoID = ", OLD.AG_NoID,";")
			);
	END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_update_compradores` AFTER UPDATE ON `compradores` FOR EACH ROW BEGIN
    INSERT INTO compradores_bitacora (CP_BIT_FECHA, CP_BIT_ExecutedSQL, CP_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('UPDATE compradores SET CP_NoID = ', NEW.CP_NoID, ', CP_Nombre = "', NEW.CP_Nombre, '", CP_Direccion = "', NEW.CP_Direccion, '", CP_Celular = ', NEW.CP_Celular, ' WHERE CP_NoID = ', NEW.CP_NoID, ';'),
        CONCAT('UPDATE compradores SET CP_NoID = ', OLD.CP_NoID, ', CP_Nombre = "', OLD.CP_Nombre, '", CP_Direccion = "', OLD.CP_Direccion, '", CP_Celular = ', OLD.CP_Celular, ' WHERE CP_NoID = ', OLD.CP_NoID, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_update_propiedades_en_mercado` AFTER UPDATE ON `propiedades_en_mercado` FOR EACH ROW BEGIN
    INSERT INTO propiedades_en_mercado_bitacora (PEM_BIT_FECHA, PEM_BIT_ExecutedSQL, PEM_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('UPDATE propiedades_en_mercado SET PEM_IDPropiedad = ', NEW.PEM_IDPropiedad, ', PEM_Nombre = "', NEW.PEM_Nombre, '", PEM_Ciudad = "', NEW.PEM_Ciudad, '", PEM_Direccion = "', NEW.PEM_Direccion, '", PEM_CantidadDormitorios = ', NEW.PEM_CantidadDormitorios, ', PEM_Caracteristicas = "', NEW.PEM_Caracteristicas, '", PEM_Precio = ', NEW.PEM_Precio, ', PEM_FechaPublicacion = "', NEW.PEM_FechaPublicacion, '", PEM_AG_NoID = ', NEW.PEM_AG_NoID, ', PEM__VD_NoID = ', NEW.PEM__VD_NoID, ' WHERE PEM_IDPropiedad = ', NEW.PEM_IDPropiedad, ';'),
        CONCAT('UPDATE propiedades_en_mercado SET PEM_IDPropiedad = ', OLD.PEM_IDPropiedad, ', PEM_Nombre = "', OLD.PEM_Nombre, '", PEM_Ciudad = "', OLD.PEM_Ciudad, '", PEM_Direccion = "', OLD.PEM_Direccion, '", PEM_CantidadDormitorios = ', OLD.PEM_CantidadDormitorios, ', PEM_Caracteristicas = "', OLD.PEM_Caracteristicas, '", PEM_Precio = ', OLD.PEM_Precio, ', PEM_FechaPublicacion = "', OLD.PEM_FechaPublicacion, '", PEM_AG_NoID = ', OLD.PEM_AG_NoID, ', PEM__VD_NoID = ', OLD.PEM__VD_NoID, ' WHERE PEM_IDPropiedad = ', OLD.PEM_IDPropiedad, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `after_update_propiedades_vendidas` AFTER UPDATE ON `propiedades_vendidas` FOR EACH ROW BEGIN
    INSERT INTO propiedades_vendidas_bitacora (PV_BIT_FECHA, PV_BIT_ExecutedSQL, PV_BIT_ReverseSQL)
    VALUES (
        NOW(),
        CONCAT('UPDATE propiedades_vendidas SET PV_IDPropiedad = ', NEW.PV_IDPropiedad, ', PV_Nombre = "', NEW.PV_Nombre, '", PV_Ciudad = "', NEW.PV_Ciudad, '", PV_Direccion = "', NEW.PV_Direccion, '", PV_CantidadDormitorios = ', NEW.PV_CantidadDormitorios, ', PV_Caracteristicas = "', NEW.PV_Caracteristicas, '", PV_Precio = ', NEW.PV_Precio, ', PV_FechaPublicacion = "', NEW.PV_FechaPublicacion, '", PV_FechaVenta = "', NEW.PV_FechaVenta, '", PV_AG_NoID = ', NEW.PV_AG_NoID, ', PV_VD_NoID = ', NEW.PV_VD_NoID, ', PV_ComisionVenta = ', NEW.PV_ComisionVenta, ', PV_CP_NoID = ', NEW.PV_CP_NoID, ' WHERE PV_IDPropiedad = ', NEW.PV_IDPropiedad, ';'),
        CONCAT('UPDATE propiedades_vendidas SET PV_IDPropiedad = ', OLD.PV_IDPropiedad, ', PV_Nombre = "', OLD.PV_Nombre, '", PV_Ciudad = "', OLD.PV_Ciudad, '", PV_Direccion = "', OLD.PV_Direccion, '", PV_CantidadDormitorios = ', OLD.PV_CantidadDormitorios, ', PV_Caracteristicas = "', OLD.PV_Caracteristicas, '", PV_Precio = ', OLD.PV_Precio, ', PV_FechaPublicacion = "', OLD.PV_FechaPublicacion, '", PV_FechaVenta = "', OLD.PV_FechaVenta, '", PV_AG_NoID = ', OLD.PV_AG_NoID, ', PV_VD_NoID = ', OLD.PV_VD_NoID, ', PV_ComisionVenta = ', OLD.PV_ComisionVenta, ', PV_CP_NoID = ', OLD.PV_CP_NoID, ' WHERE PV_IDPropiedad = ', OLD.PV_IDPropiedad, ';')
    );
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

DROP TABLE IF EXISTS `compras_por_comprador`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `compras_por_comprador` AS select `cp`.`CP_NoID` AS `CP_NoID`,`cp`.`CP_Nombre` AS `CP_Nombre`,count(`cp`.`CP_NoID`) AS `Total_Compras` from (`compradores` `cp` join `propiedades_vendidas` `pv` on((`cp`.`CP_NoID` = `pv`.`PV_CP_NoID`))) group by `cp`.`CP_NoID`;

DROP TABLE IF EXISTS `total_ventas_agentes_año`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `total_ventas_agentes_año` AS select `resultado`.`Año` AS `Año`,`resultado`.`ID_Agente` AS `ID_Agente`,`resultado`.`Nombre_Agente` AS `Nombre_Agente`,`resultado`.`Cantidad_Propiedades_Vendidas` AS `Cantidad_Propiedades_Vendidas` from ((select year(`pv`.`PV_FechaVenta`) AS `Año`,`ag`.`AG_NoID` AS `ID_Agente`,`ag`.`AG_Nombre` AS `Nombre_Agente`,count(`pv`.`PV_IDPropiedad`) AS `Cantidad_Propiedades_Vendidas` from (`propiedades_vendidas` `pv` join `agentes` `ag` on((`pv`.`PV_AG_NoID` = `ag`.`AG_NoID`))) group by `Año`,`ag`.`AG_NoID`) `resultado` join (select `subconsulta`.`Año` AS `Año`,max(`subconsulta`.`Cantidad_Propiedades_Vendidas`) AS `Max_Cantidad` from (select year(`pv`.`PV_FechaVenta`) AS `Año`,count(`pv`.`PV_IDPropiedad`) AS `Cantidad_Propiedades_Vendidas` from (`propiedades_vendidas` `pv` join `agentes` `ag` on((`pv`.`PV_AG_NoID` = `ag`.`AG_NoID`))) group by `Año`,`ag`.`AG_NoID`) `subconsulta` group by `subconsulta`.`Año`) `max_resultados` on(((`resultado`.`Año` = `max_resultados`.`Año`) and (`resultado`.`Cantidad_Propiedades_Vendidas` = `max_resultados`.`Max_Cantidad`))));

DROP TABLE IF EXISTS `ventas_por_agente`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ventas_por_agente` AS select `a`.`AG_NoID` AS `AG_NoID`,`a`.`AG_Nombre` AS `AG_Nombre`,count(`pv`.`PV_Nombre`) AS `Total_Ventas` from (`agentes` `a` join `propiedades_vendidas` `pv` on((`a`.`AG_NoID` = `pv`.`PV_AG_NoID`))) group by `a`.`AG_NoID`;

DROP TABLE IF EXISTS `ventas_por_cantidad_de_habitaciones`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ventas_por_cantidad_de_habitaciones` AS select `pv`.`PV_IDPropiedad` AS `PV_IDPropiedad`,`pv`.`PV_Nombre` AS `PV_Nombre`,`pv`.`PV_Ciudad` AS `PV_Ciudad`,`pv`.`PV_Direccion` AS `PV_Direccion`,`pv`.`PV_CantidadDormitorios` AS `PV_CantidadDormitorios`,`pv`.`PV_Caracteristicas` AS `PV_Caracteristicas`,`pv`.`PV_Precio` AS `PV_Precio`,`pv`.`PV_FechaPublicacion` AS `PV_FechaPublicacion`,`pv`.`PV_FechaVenta` AS `PV_FechaVenta`,`pv`.`PV_AG_NoID` AS `PV_AG_NoID`,`pv`.`PV_VD_NoID` AS `PV_VD_NoID`,`pv`.`PV_ComisionVenta` AS `PV_ComisionVenta`,`pv`.`PV_CP_NoID` AS `PV_CP_NoID` from `propiedades_vendidas` `pv` order by `pv`.`PV_CantidadDormitorios` desc;

DROP TABLE IF EXISTS `ventas_por_precio_propiedad`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ventas_por_precio_propiedad` AS select `pv`.`PV_IDPropiedad` AS `PV_IDPropiedad`,`pv`.`PV_Nombre` AS `PV_Nombre`,`pv`.`PV_Ciudad` AS `PV_Ciudad`,`pv`.`PV_Direccion` AS `PV_Direccion`,`pv`.`PV_CantidadDormitorios` AS `PV_CantidadDormitorios`,`pv`.`PV_Caracteristicas` AS `PV_Caracteristicas`,`pv`.`PV_Precio` AS `PV_Precio`,`pv`.`PV_FechaPublicacion` AS `PV_FechaPublicacion`,`pv`.`PV_FechaVenta` AS `PV_FechaVenta`,`pv`.`PV_AG_NoID` AS `PV_AG_NoID`,`pv`.`PV_VD_NoID` AS `PV_VD_NoID`,`pv`.`PV_ComisionVenta` AS `PV_ComisionVenta`,`pv`.`PV_CP_NoID` AS `PV_CP_NoID` from `propiedades_vendidas` `pv` order by `pv`.`PV_Precio` desc;

DROP TABLE IF EXISTS `ventas_por_ubicacion`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ventas_por_ubicacion` AS select `pv`.`PV_IDPropiedad` AS `PV_IDPropiedad`,`pv`.`PV_Nombre` AS `PV_Nombre`,`pv`.`PV_Ciudad` AS `PV_Ciudad`,`pv`.`PV_Direccion` AS `PV_Direccion`,`pv`.`PV_CantidadDormitorios` AS `PV_CantidadDormitorios`,`pv`.`PV_Caracteristicas` AS `PV_Caracteristicas`,`pv`.`PV_Precio` AS `PV_Precio`,`pv`.`PV_FechaPublicacion` AS `PV_FechaPublicacion`,`pv`.`PV_FechaVenta` AS `PV_FechaVenta`,`pv`.`PV_AG_NoID` AS `PV_AG_NoID`,`pv`.`PV_VD_NoID` AS `PV_VD_NoID`,`pv`.`PV_ComisionVenta` AS `PV_ComisionVenta`,`pv`.`PV_CP_NoID` AS `PV_CP_NoID` from `propiedades_vendidas` `pv` order by `pv`.`PV_Ciudad`;

DROP TABLE IF EXISTS `ventas_por_vendedor`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ventas_por_vendedor` AS select `vd`.`VD_NoID` AS `VD_NoID`,`vd`.`VD_Nombre` AS `VD_Nombre`,count(`pv`.`PV_Nombre`) AS `Total_ventas` from (`vendedores` `vd` join `propiedades_vendidas` `pv` on((`vd`.`VD_NoID` = `pv`.`PV_VD_NoID`))) group by `vd`.`VD_NoID`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
