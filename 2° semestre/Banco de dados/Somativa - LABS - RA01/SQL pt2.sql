Create database CONCEITOS;
use CONCEITOS;

/* PROJETO LOGICO = MODELO RELACIONAL: */

CREATE TABLE Empregado (
    ID_Emp INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF VARCHAR(20),
    fk_Departamento_ID_Depto INT
);

CREATE TABLE Departamento (
    ID_Depto INT PRIMARY KEY,
    Nome VARCHAR(50),
    Sigla VARCHAR(20)
);
 
ALTER TABLE Empregado ADD CONSTRAINT FK_Empregado_2
    FOREIGN KEY (fk_Departamento_ID_Depto)
    REFERENCES Departamento (ID_Depto)
    ON DELETE CASCADE;
    
INSERT INTO Departamento (ID_Depto, Nome, Sigla)
values 	(111, 'Vendas', 'D_V'),
		(222, 'Recursos Humanos', 'D_RH'),
        (333, 'Marketing', 'D_MKT')
;

INSERT INTO Empregado (ID_Emp, Nome, CPF, fk_Departamento_ID_Depto)
values 	(1, 'Icaro', '067.196.809-27', 111),
		(2, 'Ary', '112.939.089-67', 111),
        (3, 'Adriano', '067.378.089-99', 333)
;

select * from Empregado AS E, Departamento AS D
WHERE E.fk_Departamento_ID_Depto = D.ID_Depto
;

SELECT E.Nome AS 'Empregado', D.Nome AS 'Nome Depto', D.Sigla AS 'Sigla Depto' 
FROM Empregado AS E, Departamento AS D
WHERE E.fk_Departamento_ID_Depto = D.ID_Depto
;
