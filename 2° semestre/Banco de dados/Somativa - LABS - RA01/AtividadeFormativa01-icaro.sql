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