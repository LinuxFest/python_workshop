-- mysql -uroot -pp
CREATE DATABASE `python_tutorial_db`;
USE `python_tutorial_db`;

CREATE TABLE `python_user` (
    `id` INT(11) NOT NULL auto_increment,
    `created_at` INT(11) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255),
    `phone` VARCHAR(20),
    `password` VARCHAR(255),
    UNIQUE KEY (`username`),
    UNIQUE KEY (`email`),
    PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci COMMENT='list of users' AUTO_INCREMENT=0 ;

SHOW COLUMNS IN `python_user`;
SELECT * FROM `python_user`;