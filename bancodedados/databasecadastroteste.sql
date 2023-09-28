create database bancoTeste character set utf8mb4 collate utf8mb4_unicode_ci;
use bancoTeste;
create table cadastro(
idCliente int auto_increment primary key,
nome varchar (50), 
cpf int not null
);

insert into cadastro (idCliente, nome, cpf) values (null,'larissa', 123456789);
select * from cadastro;
select nome from cadastro;
insert into cadastro (idCliente, nome, cpf) values (null, 'larissa', '123456789');
select distinct nome from cadastro;
show tables;
describe cadastro;
select * from cadastro;
describe cadastro;
insert into cadastro (idCliente, nome, cpf) values (null, 'luiz', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'ana', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'julio', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'clara', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'larissa', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'luiz', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'guilherme', 32156471);
insert into cadastro (idCliente, nome, cpf) values (null, 'luiz', 32156471);

select * from cadastro where nome = 'luiz';	
