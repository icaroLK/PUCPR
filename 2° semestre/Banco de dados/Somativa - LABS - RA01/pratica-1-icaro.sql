create database LAB_01;

use LAB_01;

CREATE TABLE CLIENTE (
	ID INT PRIMARY KEY NOT NULL,
    NOME varchar(50),
    SOBRENOME varchar(50)
);

insert into cliente (ID, NOME, SOBRENOME)
VALUES              (2, 'Ary', 'Farah'),
					(3, 'Carol', 'Assis'),
					(4, 'Adriano', 'Vale'),
					(5, 'Galo', 'cu')
;

update cliente set nome = 'Galo', sobrenome = 'Utrabo' where ID = 5;

delete from cliente where id = 5; 

select * from cliente;


/* Lógico_1: */

CREATE TABLE Carro (
    Cod INT PRIMARY KEY,
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Ano INT,
    Km FLOAT,
    Cor VARCHAR(20)
);

insert into Carro	(Cod, Marca, Modelo, Ano, KM, Cor)
values				(97854, 'Tesla', 'X', 2020, 0, 'Branco'),
					(84953, 'Mustang', 'GT', 1969, 300000, 'Preto'),
                    (29321, 'Ferrari', 'Enzo', 1980, 500469, 'Vermelho')
;

update Carro set Cor = 'Azul Meia Noite' where Cod = 97854;

update carro set ano = 1970 where cod = 84953;

delete from carro where cod = 97854;


select * from carro;
