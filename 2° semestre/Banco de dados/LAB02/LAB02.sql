CREATE DATABASE LAB02;
USE LAB02;

/* Lógico_1: */

CREATE TABLE Empregado (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF VARCHAR(15),
    Dt_nascimento DATE
);

CREATE TABLE Dependente (
    ID_Dependente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Dt_nascimento DATE,
    fk_Empregado_Matricula INT
);
 
ALTER TABLE Dependente ADD CONSTRAINT FK_Dependente_2
    FOREIGN KEY (fk_Empregado_Matricula)
    REFERENCES Empregado (Matricula)
    ON DELETE CASCADE;
    
INSERT INTO Empregado (Matricula, Nome, CPF, Dt_nascimento)
VALUES 	(123, 'Ícaro Lima', '067.196.809-27', '2005-05-10'),
		(234, 'Nicole Seradas', '130.465.399-40', '2005-09-15'),
        (345, 'Alex', '420.420.420-69', '2005-06-21')
;

INSERT INTO Dependente (ID_Dependente, Nome, Dt_nascimento, fk_Empregado_Matricula)
VALUES	(1, 'Thiaguin', '2000-01-01', 123),
		(2, 'Bucetonha', '2000-01-01', 234),
        (3, 'Uiuiui', '2000-01-01', 345)
;

/*
SELECT * FROM Empregado;
SELECT * FROM Dependente;
*/

SELECT * FROM Empregado, Dependente;

SELECT * FROM Empregado, Dependente WHERE Empregado.Matricula = Dependente.fk_Empregado_Matricula;

/*
PARTE 2 DO PDF E COISARADA
*/


CREATE TABLE Disciplina(
ID_discip 	INT 		NOT NULL,
Nome 		VARCHAR(50) NOT NULL,
Ementa 		text		NOT NULL,
Creditos	INT			NOT NULL,
Periodo 	INT			NOT NULL
);

ALTER TABLE Disciplina
ADD CONSTRAINT PRIMARY KEY (id_discip);



INSERT INTO Disciplina 
VALUES	(1, 'Banco de dados', 'Introdução a criação de banco de dados', 4, 2),
		(2, 'Redes de computadores', 'Básico de redes de computadores', 4, 3)
;
SELECT * FROM Disciplina;

DROP TABLE PROFESSOR;

CREATE TABLE Professor(
ID_prof			INT AUTO_INCREMENT PRIMARY KEY,
Nome			VARCHAR(50) NOT NULL,
DT_nascimento	DATE,
Apelido			VARCHAR(50) GENERATED ALWAYS AS (SUBSTRING_INDEX(Nome, " ", 1))
);

INSERT INTO Professor(Nome, DT_nascimento)
VALUES	('Afonso Miguel Fodases', '1975-05-10');

INSERT INTO Professor (Nome, DT_nascimento) VALUES 
('Sheiladas Resenhas', STR_TO_DATE('08/04/1985', '%d/%m/%Y')),
('Maicris Grávido', STR_TO_DATE('14/02/1978', '%d/%m/%Y')),
('Japinha do balaco', STR_TO_DATE('22/11/1989', '%d/%m/%Y'));


SELECT * FROM Professor;

/*
PARTE 3 DO PDF E COISARADA
*/

DROP TABLE Turma;

CREATE TABLE Turma(
ID_turma	INT AUTO_INCREMENT PRIMARY KEY,
Ano			INT NOT NULL,
Semestre	INT NOT NULL,
ID_discip	INT NOT NULL,
ID_prof		INT NOT NULL,

CONSTRAINT CK_Semestre	CHECK (semestre BETWEEN 1 AND 2),
CONSTRAINT UN_Oferta	UNIQUE (ano, semestre, ID_discip, ID_prof),
CONSTRAINT FK_Prof		FOREIGN KEY (ID_prof)	REFERENCES Professor (ID_prof),
CONSTRAINT FK_Discip 	FOREIGN KEY (ID_discip)	REFERENCES Disciplina (ID_discip)
);


INSERT INTO Turma (ano, semestre, id_prof, id_discip) VALUES
(2020, 1, 2, 2),
(2019, 2, 2, 2),
(2020, 1, 3, 1),
(2021, 2, 3, 2);
/*
SELECT * FROM Turma;
SELECT * FROM Turma ORDER BY turma.ID_turma ASC;
*/

SELECT * FROM Turma, Professor, Disciplina;

SELECT * FROM Turma AS t, Professor AS p, Disciplina AS d 
WHERE t.ID_discip = d.ID_discip AND t.ID_prof = p.ID_prof 
ORDER BY t.ID_turma ASC, t.ano ASC;

SELECT t.ano, t.semestre, p.nome, d.nome
FROM Turma AS t, Professor AS p, Disciplina AS d
WHERE t.id_discip = d.id_discip AND t.id_prof = p.id_prof
ORDER BY t.ano ASC;


CREATE TABLE Colaborador (
	ID_emp INT NOT NULL,
	Nome VARCHAR(50) NOT NULL,
	Salario FLOAT NOT NULL,

	CONSTRAINT PK_emp PRIMARY KEY (ID_emp),
	CONSTRAINT ID_val CHECK (id_emp BETWEEN 0 AND 1000),
    CONSTRAINT SL_val CHECK (salario >= 1000)
);


