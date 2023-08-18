
use CONCEITOS;


/* Lógico 3: */

CREATE TABLE Empregado (
    ID_Emp INT PRIMARY KEY,
    Nome VARCHAR(50),
    CPF VARCHAR(20)
);

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