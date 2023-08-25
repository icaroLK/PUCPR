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


CREATE TABLE Projeto (
    ID_Proj INT PRIMARY KEY,
    Nome VARCHAR(50),
    Descricao TEXT
);

CREATE TABLE Trabalha (
    ID_Trab INT PRIMARY KEY,
    fk_Empregado_ID_Emp INT,
    fk_Projeto_ID_Proj INT,
    Dt_Fim DATE,
    Dt_Inicio DATE
);
 
ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_1
    FOREIGN KEY (fk_Empregado_ID_Emp)
    REFERENCES Empregado (ID_Emp)
    ON DELETE SET NULL;
 
ALTER TABLE Trabalha ADD CONSTRAINT FK_Trabalha_2
    FOREIGN KEY (fk_Projeto_ID_Proj)
    REFERENCES Projeto (ID_Proj)
    ON DELETE SET NULL;
    
    
INSERT INTO Projeto(ID_ProJ, Nome, Descricao)
VALUES	(1000, 'Sistema X', 'Sistema novo e coisarada tlg'),
		(2000, 'Sistema ABC', 'Manutenção');
        
SELECT * FROM PROJETO;

insert INTO Trabalha (ID_Trab, fk_Empregado_ID_Emp, fk_Empregado_ID_Proj, Dt_Inicio, Dt_Fim)
VALUES		(1, 1, 1000, '2020-04-20', NULL),
			(2, 3, 2000, '2019-12-07', '2022-10-12')
;

SELECT * FROM Trabalha;

DELETE FROM Trabalha;

