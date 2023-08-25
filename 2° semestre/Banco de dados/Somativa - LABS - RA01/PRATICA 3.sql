SELECT * FROM trabalha;

select E.Nome, P.Nome, T.Dt_Inicio, T.Dt_Fim
from Trabalha AS T, Empregado AS E, projeto AS P
WHERE 	T.fk_Projeto_ID_Proj = P.ID_Proj AND
		T.fk_Empregado_ID_Emp = E.ID_Emp;
        

INSERT INTO Trabalha (ID_Trab, fk_Projeto_ID_Proj, fk_Empregado_ID_Emp, Dt_Inicio, Dt_Fim)
VALUES	(3, 2000, 1, '2018-10-20', '2020-10-20'),
		(4, 2000, 3, '2010-05-03', '2019-05-03');
        
        
        
        
SELECT E.Nome AS 'Nome Empregado', P.Nome as 'Nome Projeto', T.Dt_Inicio, T.Dt_Fim