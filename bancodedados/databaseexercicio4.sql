use exercicio_28_9;

insert into cadastro_cliente (cpf,nome,rg,id_estado,id_cidade,id_sexo,id_nacionalidade,fone,id_raca,id_escolaridade) values
('1','nome1',1,1,1,1,1,1,1,1),
('2','nome2',2,2,2,2,2,2,2,2),
('3','nome3',3,3,3,3,1,3,3,3),
('4','nome4',4,4,4,1,1,4,4,4),
('5','nome5',5,5,5,1,1,5,5,5),
('6','nome6',6,6,6,1,1,6,1,6),
('7','nome7',7,7,7,1,1,7,1,7),
('8','nome8',8,8,8,1,1,8,1,8),
('9','nome9',9,9,9,1,1,9,1,1),
('10','nome10',10,10,10,1,1,10,1,1),
('11','nome11',11,11,11,1,1,11,1,1),
('12','nome12',12,12,12,1,1,12,1,1),
('13','nome13',13,13,13,1,1,13,1,1),
('14','nome14',14,14,14,1,1,14,1,1),
('15','nome15',15,15,15,1,1,15,1,1),
('16','nome16',16,16,16,1,1,16,1,1),
('17','nome17',17,17,17,1,1,17,1,1),
('18','nome18',18,18,18,1,1,18,1,1),
('19','nome19',19,19,19,1,1,19,1,1),
('20','nome20',20,20,20,1,1,20,1,1);

#select cadastro_cliente.nome, estado.nome_estado from cadastro_cliente inner join estado on cadastro.id_estado=estado.id_estado;
#select cadastro.nome, cadastro.cpf, raca.raca from cadastro inner join raca on cadastro.id_raca=raca.id_raca;
#select cadastro.nome, nacionalidade.nacionalidade from cadastro inner join nacionalidade on cadastro.id_nacionalidade=nacionalidade.id_nacionalidade order by nome desc;
#select cadastro.nome, escolaridade.escolaridade from cadastro inner join escolaridade on cadastro.id_escolaridade=escolaridade.id_escolaridade;
#select cadastro.nome, cidade.cidade, estado.estado from cadastro inner join cidade on cadastro.id_cidade=cidade.id_cidade inner join estado on cadastro.id_estado=estado.id_estado;
#select cadastro.nome, cadastro.fone, cadastro.rg, sexo.sexo, nacionalidade.nacionalidade, cidade.cidade, estado.estado, raca.raca from cadastro inner join cidade on cadastro.id_cidade=cidade.id_cidade inner join estado on cadastro.id_estado=estado.id_estado inner join sexo on cadastro.id_sexo=sexo.id_sexo inner join nacionalidade on cadastro.id_nacionalidade=nacionalidade.id_nacionalidade inner join raca on cadastro.id_raca=raca.id_raca;



