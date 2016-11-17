/* Delete old database */
/***********************/

IF EXISTS(select * from sys.databases where name='sirsDB')
DROP DATABASE sirsDB
CREATE DATABASE sirsDB;
USE sirsDB;


/* Creation database structure */
/*******************************/

/* User(id, username, password, email, first_name, last_name, birth) */
CREATE TABLE User(
	id			INTEGER NOT NULL AUTO_INCREMENT,
	username	VARBINARY,
	password	VARBINARY,
	email		VARBINARY,
	first_name	VARBINARY,
	last_name	VARBINARY,
	birth_date	VARBINARY,
	PRIMARY KEY (id)
);

/* Doctor (id, specialty) */
CREATE TABLE IF NOT EXISTS Doctor(
	id				INTEGER NOT NULL AUTO_INCREMENT,
	specialty		VARBINARY,
	PRIMARY KEY (id),
	FOREIGN KEY (id) references User(id)
);

/* Pacient (id) */
CREATE TABLE IF NOT EXISTS Pacient(
	id			INTEGER NOT NULL AUTO_INCREMENT,
	blood_type	VARBINARY,
	weight		VARBINARY,
	deseases	VARBINARY,
	PRIMARY KEY (id),
	FOREIGN KEY (id) references User(id)
);

/* Appointment(patient_id, doctor_id, date, office) */
create table IF NOT EXISTS Appointment(
	patient_id  INTEGER NOT NULL AUTO_INCREMENT,
   	doctor_id  	INTEGER NOT NULL AUTO_INCREMENT,
    date  		date NOT NULL,
    office  	VARBINARY NOT NULL,
    primary key(patient_id, doctor_id, date),
    foreign key(pacient_id, doctor_id) references User(id, id)
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