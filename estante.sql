CREATE DATABASE `estante` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

CREATE TABLE `livros` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `paginas` int(11) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `` (`codigo`,`titulo`,`autor`,`paginas`) VALUES (1,'Pulp à Brasiliana','Yvis Tomazini',150);
INSERT INTO `` (`codigo`,`titulo`,`autor`,`paginas`) VALUES (2,'Noturno','J.C.Gray',178);
INSERT INTO `` (`codigo`,`titulo`,`autor`,`paginas`) VALUES (3,'Dá um tempo','Izabella Camargo',250);
INSERT INTO `` (`codigo`,`titulo`,`autor`,`paginas`) VALUES (4,'Heroinas do Brasil','Lucia Tulchinski',123);