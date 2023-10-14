CREATE DATABASE TDE;
USE TDE;


SET @@autocommit = OFF;  /* No MySQL o padrão é estar com o commit automático 
						pra operações como insert, update, delete. Então precisamos 
                        desativa-la antes de demonstrar a transação e assim serem
                        ativadas quando EU quiser*/

CREATE TABLE Livros(
ID INT PRIMARY KEY,
Nome varchar(50),
Preco decimal(5,2)
);

INSERT INTO Livros (ID, nome, preco) VALUES
(1, 'A arte da guerra', 40.00),
(2, 'Sapiens', 69.90),
(3, 'A revolução dos bichos', 29.90),
(4, 'Clean Code', 32.00);

START TRANSACTION; /*A partir daqui, tudo será tratado como um único bloco, até ser encontrado
					um COMMIT ou um ROLLBACK*/
	DELETE FROM Livros;
    INSERT INTO Livros(ID, nome, preco) VALUES
		(1, 'Ciência de dados com python', 79.90);
	SELECT * FROM livros;
ROLLBACK; 




START TRANSACTION;
	DELETE FROM Livros;
    INSERT INTO Livros(ID, nome, preco) VALUES
		(1, 'Ciência de dados com python', 79.90);
COMMIT;




SELECT * FROM LIVROS;
DESCRIBE Livros;














/*


DROP TABLE CONTAS;
CREATE TABLE contas(
ID INT PRIMARY KEY,
Nome varchar(50),
Saldo DECIMAL(10, 2)
);

INSERT INTO Contas (ID, Nome, Saldo) VALUES
(1, 'Icaro', 1000.00),
(2, 'Ana', 500.00),
(3, 'Rafael', 250.00),
(4, 'Lucas', 820.00);

BEGIN;
DECLARE SaldoIcaro DECIMAL(10,2);
SELECT Saldo INTO SaldoIcaro FROM contas WHERE ID = 1;
*/