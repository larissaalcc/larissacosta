create database exercicio_28_9 character set utf8mb4 collate utf8mb4_unicode_ci;

use exercicio_28_9;

create table cadastro_cliente(
cpf int primary key,
nome varchar (255),
rg int,
id_estado int ,
id_cidade int ,
id_sexo int ,
id_nacionalidade int ,
id_raca int ,
id_escolaridade int ,
fone int
);
drop table cadastro_cliente;

create table estado(
id_estado int auto_increment primary key,
nome_estado varchar (255)
);

create table cidade(
id_estado int auto_increment primary key,
nome_cidade varchar (255)
);

create table sexo(
id_sexo int auto_increment primary key,
sexo varchar (255)
);

create table nacionalidade(
id_nacionalidade int auto_increment primary key,
nacionalidade varchar (255)
);

create table raca(
id_raca int auto_increment primary key,
raca varchar (255)
);

create table escolaridade(
id_escolaridade int auto_increment primary key,
escolaridade varchar (255)
);

insert into estado values (null, "Distrito Federal");
insert into estado values (null, "Goiás");
insert into estado values (null, "Mato Grosso");
insert into estado values (null, "Mato Grosso do Sul");
insert into estado values (null, "Alagoas");
insert into estado values (null, "Bahia");
insert into estado values (null, "Ceará");
insert into estado values (null, "Maranhão");
insert into estado values (null, "Paraíba");
insert into estado values (null, "Pernambuco");
insert into estado values (null, "Piaui");
insert into estado values (null, "Rio Grande do Norte");
insert into estado values (null, "Sergipe");
insert into estado values (null, "Acre");
insert into estado values (null, "Amapá");
insert into estado values (null, "Amazonas");
insert into estado values (null, "Pará");
insert into estado values (null, "Rondônia");
insert into estado values (null, "Roraima");
insert into estado values (null, "tocantins");
insert into estado values (null, "Espírito Santo");
insert into estado values (null, "Minas Gerais");
insert into estado values (null, "Rio de Janeiro");
insert into estado values (null, "São Paulo");
insert into estado values (null, "Paraná");
insert into estado values (null, "Rio Grande do Sul");
insert into estado values (null, "Santa Catarina");

select * from estado;

insert into sexo values (null, "Masculino");
insert into sexo values (null, "Feminino");
insert into sexo values (null, "Não Binário");

select * from sexo;

insert into raca values (null, "Branco");
insert into raca values (null, "Preto");
insert into raca values (null, "Amarelo");
insert into raca values (null, "Indígena");
insert into raca values (null, "Pardo");

select * from raca;

insert into escolaridade values (null, "Analfabeto");
insert into escolaridade values (null, "Ensino Médio Completo");
insert into escolaridade values (null, "Ensino Médio Incompleto");
insert into escolaridade values (null, "Ensino Fundamental Completo");
insert into escolaridade values (null, "Ensino Fundamental Incompleto");
insert into escolaridade values (null, "Ensino Superior");
insert into escolaridade values (null, "Mestrado");
insert into escolaridade values (null, "Pós - Graduação");

select * from  escolaridade;

insert into nacionalidade values (null, "Brasileiro");
insert into nacionalidade values (null, "Estrangeiro");

drop table nacionalidade;
select * from nacionalidade;

set sql_safe_updates = 0;
update cidade set nome_cidade = "Abaixo de M" where  nome_cidade like 'A%' or nome_cidade like 'B%' or nome_cidade like 'C%' or 
nome_cidade like 'D%' or nome_cidade like 'E%' or nome_cidade like 'F%' or nome_cidade like 'G%' or nome_cidade like 'H%' or 
nome_cidade like 'I%' or nome_cidade like 'J%' or nome_cidade like 'K%' or nome_cidade like 'L%'or nome_cidade like 'M%';

select * from cidade order by nome_cidade;

update cidade set nome_cidade = "Acima de M" where  nome_cidade like 'N%' or nome_cidade like 'O%' or nome_cidade like 'P%' or 
nome_cidade like 'Q%' or nome_cidade like 'R%' or nome_cidade like 'S%' or nome_cidade like 'T%' or nome_cidade like 'U%' or 
nome_cidade like 'V%' or nome_cidade like 'W%' or nome_cidade like 'X%' or nome_cidade like 'Y%'or nome_cidade like 'Z%';

select * from cidade order by nome_cidade ;

update nacionalidade set nacionalidade = 'Fora do Brasil' where nacionalidade like 'estrangeiro';
select * from nacionalidade;

update raca set raca = 'Seres Humanos' where raca like 'branco' or raca like 'preto' or raca like 'amarelo' or raca like 'indígena' or raca like 'pardo';
select * from raca;

update escolaridade set escolaridade = 'Ensino Básico' where escolaridade like 'Analfabeto' or  escolaridade like 'Ensino Médio Completo'
or  escolaridade like 'Ensino médio Incompleto' or escolaridade like  'Ensino Fundamental Completo' or  escolaridade
like'Ensino Fundamental Incompleto';
select * from escolaridade;

update escolaridade set escolaridade = 'Ensino Avançado' where escolaridade like 'Ensino Superior' or escolaridade like 'Mestrado' 
or escolaridade like 'Pós - Graduação';
select * from escolaridade;

update estado set nome_estado = 'Região Centro - Oeste' where nome_estado like 'Distrito Federal' or nome_estado like 'Goiás' or nome_estado like
'Mato Grosso' or nome_estado like ' Mato Grosso do Sul';

set sql_safe_updates = 0;

update estado set nome_estado = 'Nordeste' where nome_estado like 'Alagoas' or nome_estado like 'Bahia' or nome_estado like 'Ceará' or
nome_estado like 'Maranhão' or nome_estado like 'Paraíba' or nome_estado like 'Pernambuco' or nome_estado like 'Piaui' or nome_estado like 'Rio Grande do Norte'
or nome_estado like 'Sergipe';

select * from estado;






 
