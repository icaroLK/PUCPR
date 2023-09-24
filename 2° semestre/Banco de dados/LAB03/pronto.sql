CREATE DATABASE IF NOT EXISTS LAB03;
USE LAB03;

DROP TABLE IF EXISTS departamento;
CREATE TABLE departamento (
  ID_depto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sigla VARCHAR(5) NOT NULL,
  nome VARCHAR(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO departamento VALUES 
(100,'RH','Recursos Humanos'),
(101,'CTB','Contabilidade'),
(102,'VND','Vendas'),
(103,'ETQ','Estoque'),
(104,'ATM','Atendimento'),
(105,'CNG','Carteira de Negócios');

DROP TABLE IF EXISTS empregado;
CREATE TABLE empregado(
  ID_emp INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  dt_nascimento DATE NOT NULL,
  ID_depto INT NOT NULL,
  Salario FLOAT DEFAULT NULL,
  KEY FK_Empregado_Departamento (ID_depto),
  CONSTRAINT FK_Empregado_Departamento FOREIGN KEY (ID_depto) REFERENCES departamento (ID_depto)
) ENGINE=InnoDB AUTO_INCREMENT=1008 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO empregado VALUES 
(1000,'José da Silva','2000-12-20',100,2000),
(1001,'Maria das Flores','1995-05-14',101,2500),
(1002,'Antônio Lopes','1998-04-18',101,1500),
(1003,'Catarina Santos','2002-08-05',102,1500),
(1004,'Olívia Andrade','1993-07-19',102,2200),
(1005,'Arthur Coimbra','1980-10-06',103,2900),
(1006,'Jonas Alves','1990-12-13',103,2080),
(1007,'Amélia Silveira','1980-05-06',100,3005);


DROP TABLE IF EXISTS skill;
CREATE TABLE skill (
  ID_skill INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  descricao TEXT NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO skill VALUES 
(1,'MS Word','Conhece o ambiente do editor de texto e sabe criar, salvar e modificar documentos.'),
(2,'MS Excel','Conhece o ambiente da planilha eletrônica e sabe criar, salvar e modificar documentos.'),
(3,'MS Power Point','Conhece o ambiente do editor de apresentações e sabe criar, salvar e modificar documentos.'),
(4,'Pytho','Conhece linguagem de programação Python e sabe criar, salvar e modificar programas na linguagem.'),
(5,'Java','Conhece linguagem de programação Java e sabe criar, salvar e modificar programas na linguagem.'),
(6,'HTML','Conhece linguagem de marcação HTML e sabe criar, salvar e modificar documentos HTML.');

DROP TABLE IF EXISTS empskill;
CREATE TABLE empskill (
  ID_emp INT NOT NULL,
  ID_skill INT NOT NULL,
  nivel VARCHAR(20) NOT NULL,
  PRIMARY KEY(ID_emp, ID_skill),
  KEY FK_EmpSkill_Skill (ID_skill),
  CONSTRAINT FK_EmpSkill_Empregado FOREIGN KEY (ID_emp) REFERENCES empregado (ID_emp),
  CONSTRAINT FK_EmpSkill_Skill FOREIGN KEY (ID_skill) REFERENCES skill (ID_skill)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO empskill VALUES 
(1000,1,'Básico'),
(1000,2,'Intermediário'),
(1000,3,'Básico'),
(1002,4,'Avançado'),
(1002,5,'Básico'),
(1004,4,'Intermediário'),
(1004,5,'Básico');




SELECT Nome, dt_nascimento, DATE_FORMAT(dt_nascimento, '%d/%m/%Y') AS 'Aniversario',
	(YEAR(NOW()) - YEAR(dt_nascimento) - CASE 
		WHEN (MONTH(NOW()) * 100 + DAY(NOW())) > (MONTH(dt_nascimento) * 100 + DAY(dt_nascimento))
		THEN 0 
        ELSE 1 
        END) AS Idade
FROM Empregado;




CREATE TABLE ex(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50),
nascimento DATE
);


INSERT INTO ex VALUES
(DEFAULT, 'Ícaro', '2005-05-10');

UPDATE ex SET nascimento = '2005-05-10' WHERE id = 1;


SELECT 
    YEAR(NOW()) - YEAR(nascimento) - CASE
        WHEN (MONTH(NOW()) * 100 + DAY(NOW())) > (MONTH(nascimento) * 100 + DAY(nascimento)) THEN 0
        ELSE 1
    END AS Idade
FROM ex;



/*---------------------PRATICA 3.3---------------------*/
SELECT *
FROM Empregado AS E, Departamento AS D 
WHERE E.ID_depto = D.ID_depto 
ORDER BY E.nome;

SELECT *
FROM Empregado AS E INNER JOIN Departamento AS D -- JOIN ou INNER JOIN
ON (E.ID_depto = D.ID_depto) -- Condição para retorno
ORDER BY E.nome;



SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E, EmpSkill AS ES, Skill AS S 
WHERE E.ID_emp = ES.ID_emp AND 
S.ID_skill = ES.ID_skill
ORDER BY S.nome, E.nome;

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
INNER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp) 
INNER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;


/*---------------------PRATICA 3.4---------------------*/

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
LEFT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
LEFT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;


/*---------------------PRATICA 3.5---------------------*/
SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
RIGHT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
RIGHT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
ORDER BY S.nome, E.nome;

SELECT * FROM EmpSkill;
SELECT * FROM Skill;


(
SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
LEFT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
LEFT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
)
UNION 
(
SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
RIGHT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
RIGHT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
) ORDER BY nivel;

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
LEFT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
LEFT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill);

SELECT E.nome AS Empregado, ES.nivel, S.nome
FROM Empregado AS E 
RIGHT OUTER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
RIGHT OUTER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill);




/*---------------------PRATICA 3.6---------------------*/


SELECT E.ID_emp, E.nome
FROM Empregado AS E 
JOIN Departamento AS D ON (E.ID_depto = D.ID_depto)
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
ORDER BY E.nome;


SELECT E.ID_emp, E.nome FROM Empregado AS E
WHERE E.ID_depto IN
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
)
ORDER BY E.nome;






SELECT E.ID_depto, E.ID_emp, E.nome
FROM Empregado AS E
WHERE E.ID_depto NOT IN
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
) ORDER BY E.nome;



SELECT E.ID_depto, E.ID_emp, E.nome
FROM Empregado AS E
WHERE E.ID_depto <> ALL
(
SELECT D.ID_depto
FROM Departamento AS D
WHERE D.sigla = 'CTB' OR D.sigla ='VND'
) ORDER BY E.nome;






SELECT E.ID_depto, E.ID_emp, E.nome, E.dt_nascimento
FROM Empregado AS E
WHERE YEAR(E.dt_nascimento) >= 1998 AND E.ID_depto IN
(
SELECT D.ID_depto
FROM Departamento AS D, Empregado AS E1
WHERE D.ID_depto = E1.ID_depto AND
 (D.sigla = 'CTB' OR D.sigla ='VND')
)
ORDER BY E.nome;





/*---------------------PRATICA 3.8---------------------*/

DROP VIEW IF EXISTS CompetenciasEmpregados;


CREATE VIEW CompetenciasEmpregados AS
(
SELECT D.sigla AS Depto, S.nome AS Competencia, ES.nivel AS Nivel, E.nome AS Empregado
FROM
 ((
 Empregado AS E INNER JOIN EmpSkill AS ES ON (E.ID_emp = ES.ID_emp)
) INNER JOIN Skill AS S ON (S.ID_skill = ES.ID_skill)
 ) INNER JOIN Departamento AS D ON (D.ID_depto = E.ID_depto) 
);



SELECT * FROM CompetenciasEmpregados
ORDER BY Depto, Competencia, Empregado;






/*---------------------PRATICA 3.9---------------------*/


SELECT
COUNT(*) AS 'Número de Empregados',
AVG(salario) AS 'Salário Médio',
MIN(salario) AS 'Menor Salário' ,
MAX(salario) AS 'Maior Salário' ,
SUM(salario) AS 'Total Salários'
FROM Empregado;

SELECT
COUNT(*) AS 'Número de Empregados',
CONVERT(AVG(salario), DECIMAL(8,2)) AS 'Salário Médio',
MIN(salario) AS 'Menor Salário' ,
MAX(salario) AS 'Maior Salário' ,
SUM(salario) AS 'Total Salários'
FROM Empregado;

