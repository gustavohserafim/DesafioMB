CREATE TABLE `pair` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pair` varchar(6) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `mms_20` double DEFAULT NULL,
  `mms_50` double DEFAULT NULL,
  `mms_200` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
