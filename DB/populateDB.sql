/* Populate the database */
/*************************/

/* User(id, email, password, name, birth) */
INSERT INTO User (email, password, name, birth) VALUES (AES_ENCRYPT('comer@gmail.com', UNHEX('F3229A0B371ED2D9441B830D21A390C3')), 'dsads', 'sads', 'sadas');
-- INSERT INTO User (email, password, name, birth) VALUES (AES_ENCRYPT('comer@gmail.com', UNHEX(SHA2('passwordxpto',512))));
INSERT INTO User VALUES (2, 'EmpresaFixe');
INSERT INTO User VALUES (3, 'EmpresaAzul');
INSERT INTO User VALUES (4, 'EmpresaLocal');
INSERT INTO User VALUES (5, 'EMpresaVerde');

/* Doctor (id, specialty) */
INSERT INTO Doctor VALUES (1, 'FixEverything');
INSERT INTO Doctor VALUES (2, 'EmpresaFixe');
INSERT INTO Doctor VALUES (3, 'EmpresaAzul');
INSERT INTO Doctor VALUES (4, 'EmpresaLocal');
INSERT INTO Doctor VALUES (5, 'EMpresaVerde');

/* Nurse (id) */
INSERT INTO Nurse VALUES ('Rua D.Henrique');
INSERT INTO Nurse VALUES ('Rua do Manuel');
INSERT INTO Nurse VALUES ('Rua amarela');
INSERT INTO Nurse VALUES ('Rua vermelha');
INSERT INTO Nurse VALUES ('Rua cor-de-rosa');

/* Pacient (id) */
INSERT INTO Pacient VALUES (231231231, 261234567, 'Rui');
INSERT INTO Pacient VALUES (123123123, 264987654, 'Guilherme');
INSERT INTO Pacient VALUES (789789789, 263098765, 'Ricardo');
INSERT INTO Pacient VALUES (456456456, 265231425, 'Madalena');
INSERT INTO Pacient VALUES (234234234, 263143567, 'Marta');

/* Receptionist (id) */
INSERT INTO Receptionist VALUES (1);
INSERT INTO Receptionist VALUES (2);
INSERT INTO Receptionist VALUES (3);
INSERT INTO Receptionist VALUES (4);
INSERT INTO Receptionist VALUES (5);

/* Appointment(patient_id, doctor_id, date, office) */
INSERT INTO Appointment VALUES (1);
INSERT INTO Appointment VALUES (2);
INSERT INTO Appointment VALUES (3);
INSERT INTO Appointment VALUES (4);
INSERT INTO Appointment VALUES (5);