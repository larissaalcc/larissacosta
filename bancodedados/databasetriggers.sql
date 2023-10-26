

create database teste_trigger character set utf8mb4 collate utf8mb4_unicode_ci;

create table produto(
referencia varchar (3) primary key,
descricacao varchar (50) unique,
estoque int not null default 0
);

drop table produto;

insert into produto values ('001','feijao',10);

insert into produto values ('002','arroz',5);

insert into produto values ('003','farinha',15);

select * from produto;

create table itens_venda(
venda int,
produto varchar (3),
quantidade int
);

insert into itens_venda values (1,'001',3);

insert into itens_venda values (1,'002',1);

insert into itens_venda values (1,'003',5);

select * from itens_venda;

delimiter #

select * from produto #

delimiter ;

select * from produto;

delimiter $

create trigger tgr_itens_venda_insert after insert 
on itens_venda
for each row
begin
	update produto set estoque = estoque - new.quantidade where referencia = new.produto; 
end$

insert into itens_venda values (1,"002",3)$

select * from produto$

create trigger tgr_itens_venda_delete after delete 
on itens_venda
for each row
begin
	update produto set estoque = estoque + old.quantidade
where referencia = old.quantidade;
end $

set sql_safe_updates = 0 $
drop table produto $

delete from itens_venda where produto = '001' $

select * from produto $
select * from itens_venda $