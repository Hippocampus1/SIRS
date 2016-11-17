/* Populate the database */
/*************************/

/* User(id, username, password, email, first_name, last_name, birth) */
-- INSERT INTO User (email, password, name, birth) VALUES (AES_ENCRYPT('comer@gmail.com', UNHEX('F3229A0B371ED2D9441B830D21A390C3')), 'dsads', 'sads', 'sadas');
-- INSERT INTO User (email, password, name, birth) VALUES (AES_ENCRYPT('comer@gmail.com', UNHEX(SHA2('passwordxpto',512))));
INSERT INTO User VALUES (1, 'j09', '12345', 'j09x@hotmail.com', 'joao', 'mateus', '1995-03-14');
INSERT INTO User VALUES (2, 'gheo1998', 'queijo', 'ghe98@gmail.com', 'guilherme', 'castanheiro', '1987-06-27');
INSERT INTO User VALUES (3, 'marrria', 'batatas', 'mari@sapo.pt', 'maria', 'rocha', '1977-09-01');

INSERT INTO User VALUES (4, 'vortex', 'cremoso', 'docinho@gmail.com', 'roberto', 'foca', '1970-02-11');
INSERT INTO User VALUES (5, 'axul', 'natural', 'vegetal56@hotmail.com', 'liliana', 'sousa', '1985-12-19');
INSERT INTO User VALUES (6, 'limao', 'password', 'cha@gmail.com', 'miguel', 'lourenco', '1969-10-07');

/* Doctor (id, specialty) */
INSERT INTO Doctor VALUES (4, 'dermatologia');
INSERT INTO Doctor VALUES (5, 'ginecologia');
INSERT INTO Doctor VALUES (6, 'homeopatia');

/* Patient (id, blood_type, weight, deseases) */
INSERT INTO Patient VALUES (1, 'A+', '70.232', 'cenas');
INSERT INTO Patient VALUES (2, 'AB', '45.356', 'doenca');
INSERT INTO Patient VALUES (3, 'B-', '90.123', 'manias');

/* Appointment(patient_id, doctor_id, date, time, office) */
INSERT INTO Appointment VALUES (1, 4, '2016-12-04', '12:00', 'gab 5');
INSERT INTO Appointment VALUES (3, 5, '2016-12-13', '14:00', 'gab 39');
INSERT INTO Appointment VALUES (3, 6, '2016-12-13', '17:30', 'gab 21');