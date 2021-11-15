-- MySQL Script generated by MySQL Workbench
-- нд, 07-лис-2021 12:07:14 +0200
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tus_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tus_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tus_db` ;
USE `tus_db` ;

-- -----------------------------------------------------
-- Table `tus_db`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tus_db`.`User` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(55) NOT NULL,
  `last_name` VARCHAR(55) NOT NULL,
  `location` VARCHAR(55) NULL,
  `username` VARCHAR(55) NOT NULL,
  `password_hash` VARCHAR(300) NOT NULL,
  `email` VARCHAR(60) NOT NULL,
  `phone` VARCHAR(15) NULL,
  `photo` VARCHAR(200) NULL,
  `role` ENUM('Tutor', 'Admin', 'Client') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tus_db`.`CV`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tus_db`.`CV` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(2000) NOT NULL,
  `rating` FLOAT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_CV_User_idx` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `User_id_UNIQUE` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_CV_User`
    FOREIGN KEY (`user_id`)
    REFERENCES `tus_db`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tus_db`.`Subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tus_db`.`Subject` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` ENUM('English', 'German', 'Chemistry', 'Math', 'Biology', 'History', 'Physics', 'Astronomy', 'Literature') NOT NULL,
  `cv_id` INT UNSIGNED NOT NULL,
  `cv_user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `cv_id`, `cv_user_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_Subject_CV1_idx` (`cv_id` ASC, `cv_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Subject_CV1`
    FOREIGN KEY (`cv_id` , `cv_user_id`)
    REFERENCES `tus_db`.`CV` (`id` , `user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tus_db`.`Review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tus_db`.`Review` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(1000) NOT NULL,
  `mark` INT NOT NULL DEFAULT 0,
  `user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_Review_User1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Review_User1`
    FOREIGN KEY (`user_id`)
    REFERENCES `tus_db`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
