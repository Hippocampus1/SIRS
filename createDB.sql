/* Delete old database */
/***********************/

IF EXISTS(select * from sys.databases where name='sirsDB')
DROP DATABASE sirsDB
CREATE DATABASE sirsDB;
USE sirsDB;


/* Creation database structure */
/*******************************/

/* Doctor (id, empresa) */
CREATE TABLE Doctor(
	id		INT,
	empresa	VARCHAR(200),
	PRIMARY KEY (id)
);

/* Nurse (morada) */
CREATE TABLE Nurse(
	morada	VARCHAR(200),
	PRIMARY KEY (morada)
);

/* Pacient (nif, telefone, nome)
unique(telefone) */
CREATE TABLE Pacient(
	nif			INT,
	telefone	INT,
	nome		VARCHAR(100),
	PRIMARY KEY (nif)
);

/* Reserva (número) */
CREATE TABLE Reserva(
	numero INT,
	PRIMARY KEY (numero)
);

/* Alugável (código, morada, nif, foto)
nif: FK Pacient(nif)
morada: FK Nurse(morada)
unique(foto) */
CREATE TABLE Alugavel(
	codigo	INT,
	morada	VARCHAR(200),
	nif		INT,
	foto	VARCHAR(100) NOT NULL UNIQUE,
	PRIMARY KEY (codigo, morada),
	FOREIGN KEY (nif) references Pacient(nif),
	FOREIGN KEY (morada) references Nurse(morada)
);


/* Espaço (código, morada)
código, morada: FK Alugável(código, morada) */
CREATE TABLE Espaco(
	codigo 	INT,
	morada	VARCHAR(200),
	PRIMARY KEY (codigo, morada),
	FOREIGN KEY (codigo, morada) references Alugavel(codigo, morada)
);

/* Posto (código, morada, código_espaço)
código_espaço, morada: FK Espaço (código, morada) */
CREATE TABLE Posto(
	codigo			INT,
	morada			VARCHAR(200),
	codigo_espaco	INT,
	PRIMARY KEY (codigo, morada, codigo_espaco),
	FOREIGN KEY (codigo_espaco, morada) references Espaco(codigo, morada)
);

/* Oferta (código, morada, data_início, data_fim, tarifa)
código, morada: FK Alugável(código, morada)
unique(data_fim) */
CREATE TABLE Oferta(
	codigo 			INT,
	morada			VARCHAR(200),
	data_inicio		DATE,
	data_fim		DATE UNIQUE,
	tarifa			FLOAT(10,2),
	PRIMARY KEY (codigo, morada, data_inicio),
	FOREIGN KEY (codigo, morada) references Alugavel(codigo, morada)
);

/* Paga (número, data, método)
número: FK Reserva(número) */
CREATE TABLE Paga(
	numero	INT,
	data 	DATE,
	metodo	VARCHAR(30),
	PRIMARY KEY (numero),
	FOREIGN KEY (numero) references Reserva(numero)
);

/* Estado (timestamp, número, estado)
número: FK Reserva(número) */
CREATE TABLE Estado(
	timestamp	TIMESTAMP,
	numero		INT,
	estado 		VARCHAR(10),
	PRIMARY KEY (timestamp, numero),
	FOREIGN KEY (numero) references Reserva(numero)
);

/* Doctoriza (id, nif, morada, código)
id: FK Doctor(id)
nif, morada, código: FK Alugável(nif, morada, código) */
CREATE TABLE Doctoriza(
	id		INT,
	nif		INT,
	morada	VARCHAR(200),
	codigo 	INT,
	PRIMARY KEY (id, nif, morada, codigo),
	FOREIGN KEY (id) references Doctor(id),
	FOREIGN KEY (nif, morada, codigo) references Alugavel(nif, morada, codigo)
);

/* Aluga (nif, número, morada, código, data_início)
nif: FK Pacient(nif)
número: FK Reserva (número)
morada, código, data_início: FK Oferta(morada, código, data_início) */
CREATE TABLE Aluga(
	nif			INT,
	numero		INT,
	morada		VARCHAR(200),
	codigo 		INT,
	data_inicio	DATE,
	PRIMARY KEY (nif, numero, morada, codigo, data_inicio),
	FOREIGN KEY (nif) references Pacient(nif),
	FOREIGN KEY (numero) references Reserva(numero),
	FOREIGN KEY (morada, codigo, data_inicio) references Oferta(morada, codigo, data_inicio)
);

/* Populate the database */
/*************************/

/* Doctor (id, empresa) */
INSERT INTO Doctor VALUES (1, 'FixEverything');
INSERT INTO Doctor VALUES (2, 'EmpresaFixe');
INSERT INTO Doctor VALUES (3, 'EmpresaAzul');
INSERT INTO Doctor VALUES (4, 'EmpresaLocal');
INSERT INTO Doctor VALUES (5, 'EMpresaVerde');

/* Edifício (morada) */
INSERT INTO Nurse VALUES ('Rua D.Henrique');
INSERT INTO Nurse VALUES ('Rua do Manuel');
INSERT INTO Nurse VALUES ('Rua amarela');
INSERT INTO Nurse VALUES ('Rua vermelha');
INSERT INTO Nurse VALUES ('Rua cor-de-rosa');

/* Pacient (nif, telefone, nome) */
INSERT INTO Pacient VALUES (231231231, 261234567, 'Rui');
INSERT INTO Pacient VALUES (123123123, 264987654, 'Guilherme');
INSERT INTO Pacient VALUES (789789789, 263098765, 'Ricardo');
INSERT INTO Pacient VALUES (456456456, 265231425, 'Madalena');
INSERT INTO Pacient VALUES (234234234, 263143567, 'Marta');

/* Reserva (número) */
INSERT INTO Reserva VALUES (1);
INSERT INTO Reserva VALUES (2);
INSERT INTO Reserva VALUES (3);
INSERT INTO Reserva VALUES (4);
INSERT INTO Reserva VALUES (5);

/* Alugável (código, morada, nif, foto) */
INSERT INTO Alugavel VALUES (123456789, 'Rua D.Henriques', 231231231, '2313_12312.jpg');
INSERT INTO Alugavel VALUES (987654321, 'Rua do Manuel', 123123123, 'dfjndf.jpg');
INSERT INTO Alugavel VALUES (192837465, 'Rua amarela', 789789789, 'imagem.png');
INSERT INTO Alugavel VALUES (918273645, 'Rua vermelha', 456456456, 'foto.jpg');
INSERT INTO Alugavel VALUES (111111111, 'Rua cor-de-rosa', 234234234, '234_dsf.png');
INSERT INTO Alugavel VALUES (222222222, 'Rua cor-de-rosa', 234234234, '234_dsf.png');
INSERT INTO Alugavel VALUES (333333333, 'Rua cor-de-rosa', 234234234, '234_dsf.png');

/* Espaço (código, morada) */
INSERT INTO Espaco VALUES (123456789, 'Rua D.Henriques');
INSERT INTO Espaco VALUES (987654321, 'Rua do Manuel');
INSERT INTO Espaco VALUES (192837465, 'Rua amarela');
INSERT INTO Espaco VALUES (918273645, 'Rua vermelha');
INSERT INTO Espaco VALUES (111111111, 'Rua cor-de-rosa'); /*<------ Espaco com postos */

/* Posto (código, morada, código_espaço) */
INSERT INTO Posto VALUES (222222222, 'Rua cor-de-rosa', 111111111);
INSERT INTO Posto VALUES (333333333, 'Rua cor-de-rosa', 111111111);

/* Oferta (código, morada, data_início, data_fim, tarifa) */
INSERT INTO Oferta VALUES (123456789, 'Rua D.Henriques', '2016-11-03', '2016-11-04', );
INSERT INTO Oferta VALUES ();
INSERT INTO Oferta VALUES ();
INSERT INTO Oferta VALUES ();
INSERT INTO Oferta VALUES ();

/* Paga (número, data, método) */
INSERT INTO Paga VALUES ();
INSERT INTO Paga VALUES ();
INSERT INTO Paga VALUES ();
INSERT INTO Paga VALUES ();
INSERT INTO Paga VALUES ();

/* Estado (timestamp, número, estado) */
INSERT INTO Estado VALUES ();
INSERT INTO Estado VALUES ();
INSERT INTO Estado VALUES ();
INSERT INTO Estado VALUES ();
INSERT INTO Estado VALUES ();

/* Doctoriza (id, nif, morada, código) */
INSERT INTO Doctoriza VALUES ();
INSERT INTO Doctoriza VALUES ();
INSERT INTO Doctoriza VALUES ();
INSERT INTO Doctoriza VALUES ();
INSERT INTO Doctoriza VALUES ();

/* Aluga (nif, número, morada, código, data_início) */
INSERT INTO Aluga VALUES ();
INSERT INTO Aluga VALUES ();
INSERT INTO Aluga VALUES ();
INSERT INTO Aluga VALUES ();
INSERT INTO Aluga VALUES ();
