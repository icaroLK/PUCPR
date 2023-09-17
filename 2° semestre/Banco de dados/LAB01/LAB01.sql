CREATE DATABASE LAB01;
USE LAB01;
CREATE TABLE CLIENTE(
	ID INT PRIMARY KEY NOT NULL,
    NOME VARCHAR(50),
    SOBRENOME VARCHAR(50)
);

INSERT INTO CLIENTE (ID, NOME, SOBRENOME)
VALUES  (1, 'Ícaro', 'Kuchanovicz'),
		(2, 'Nicole', 'Serafas'),
		(3, 'Ary', 'Farah'),
        (4, 'Alex', 'Americana'),
        (5, 'Fodase', 'Preguiças')
;

UPDATE CLIENTE SET NOME = 'Garrafa', SOBRENOME = 'Pet' WHERE ID = 5;
DELETE FROM CLIENTE WHERE ID = 2;
SELECT * FROM CLIENTE;





/* Lógico_1: */

CREATE DATABASE LAB01;
USE LAB01;

CREATE TABLE Carro (
    CodCarro INT PRIMARY KEY,
    Marca VARCHAR(100),
    Modelo VARCHAR(100),
    Ano DATE,
    KM FLOAT,
    Cor VARCHAR(50)
);


INSERT INTO Carro (CodCarro, Marca, Modelo, Ano, KM, Cor)
VALUES	(1, 'Tesla', 'SEX', '2020-05-16', 0, 'Preto'),
		(2, 'Tesla', 'X', '2020-01-01', 0, 'Branco'),
		(3, 'Mustang', 'GT', '1969-01-01', 300000, 'Preto'),
		(4, 'Ferrari', 'Enzo', '1980-01-01', 500469, 'Vermelho')
;

UPDATE CARRO SET Cor = 'Verde Musgo' WHERE CodCarro = 1;

UPDATE CARRO SET Ano = '2022-01-02' WHERE CodCarro = 2;


SELECT * FROM Carro;

