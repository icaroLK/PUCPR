create database LAB_01;

use LAB_01;

CREATE TABLE CLIENTE (
	ID INT PRIMARY KEY NOT NULL,
    NOME varchar(50),
    SOBRENOME varchar(50)
);

insert into cliente (ID, NOME, SOBRENOME)
VALUES
		(2, 'Ary', 'Farah'),
        (3, 'Carol', 'Assis'),
        (4, 'Adriano', 'Vale'),
        (5, 'Galo', 'cu')
;

select * from cliente;