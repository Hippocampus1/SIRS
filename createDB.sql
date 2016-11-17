/* Delete old database */
/***********************/

-- IF EXISTS(select * from sys.databases where name='sirsDB')
-- DROP DATABASE sirsDB
-- CREATE DATABASE sirsDB;
-- USE sirsDB;
USE sirsDB;
drop table IF EXISTS Appointment;
drop table IF EXISTS Patient;
drop table IF EXISTS Doctor;
drop table IF EXISTS User;

/* Creation database structure */
/*******************************/

/* User(id, username, password, email, first_name, last_name, birth) */
CREATE TABLE IF NOT EXISTS User(
	id			INTEGER NOT NULL AUTO_INCREMENT,
	username	VARCHAR(50), 
	password	VARCHAR(50), 
	email		VARCHAR(50), 
	first_name	VARCHAR(50), 
	last_name	VARCHAR(50), 
	birth_date	date, 
	PRIMARY KEY (id)
);

/* Doctor (id, specialty) */
CREATE TABLE IF NOT EXISTS Doctor(
	id				INTEGER NOT NULL,
	specialty		VARCHAR(50), 
	PRIMARY KEY (id),
	FOREIGN KEY (id) references User(id)
);

/* Patient (id, blood_type, weight, deseases) */
CREATE TABLE IF NOT EXISTS Patient(
	id			INTEGER NOT NULL,
	blood_type	VARCHAR(5), 
	weight		DECIMAL(10,3), 
	deseases	VARCHAR(50), 
	PRIMARY KEY (id),
	FOREIGN KEY (id) references User(id)
);

/* Appointment(patient_id, doctor_id, date, office) */
create table IF NOT EXISTS Appointment(
	patient_id  INTEGER NOT NULL,
   	doctor_id  	INTEGER NOT NULL,
    date  		date NOT NULL,
    time		VARCHAR(7) NOT NULL,
    office  	VARCHAR(50),
    primary key (patient_id, doctor_id, date),
    foreign key (patient_id) references Patient(id),
    foreign key (doctor_id) references Doctor(id)
);

-- /* Nurse (id) */
-- CREATE TABLE IF NOT EXISTS Nurse(
-- 	id		INTEGER NOT NULL AUTO_INCREMENT,
-- 	PRIMARY KEY (id),
-- 	FOREIGN (id) references User(id)
-- );

--  /* Receptionist (id) */ 
-- CREATE TABLE IF NOT EXISTS Receptionist(
-- 	id		INTEGER NOT NULL AUTO_INCREMENT,
-- 	PRIMARY KEY (id),
-- 	FOREIGN KEY (id) references User(id)
-- );