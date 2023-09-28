insert into ex2_cliente (codcliente, nome, datanascimento, cpf) values(null, 'luiz','2002-10-01',123);
describe ex2_cliente;
select * from ex2_cliente;
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'larissa','2005-08-16',1234);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'julia','2006-03-06',1234);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'luiz','2002-10-01',123);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null,'pedro','2005-08-16',1234);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'joao','2000-10-01',1234);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'maria','2002-10-02',123);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'luana','2004-12-18',123);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'thiago','2002-10-01',12347);
insert into ex2_cliente(codcliente, nome, datanascimento, cpf) values(null, 'isabela','2006-10-01',123);
select * from ex2_cliente;

insert into ex2_produto(codproduto, descricao, quantidade) values(null, 'pó compacto',1);
insert into ex2_produto (codproduto, descricao, quantidade) values (null,'batom',1);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'corretivo',2);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'rímel',2);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'base',1);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'iluminador',1);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'paleta de sombra',1);
insert into ex2_produto (codproduto, descricao, quantidade) values (null, 'primer',1);
select * from ex2_produto;

insert into ex2_pedido(codpedido, datapedido, nf, valortotal, codcliente) values (null,'2023-08-31',1,100.00,1);
insert into ex2_pedido (codpedido, datapedido, nf, valortotal, codcliente) values (null,'2020-08-31',2,100.00,2);
insert into ex2_pedido (codpedido, datapedido, nf, valortotal, codcliente) values (null,'2023-08-31',3,100.00,3);
insert into ex2_pedido (codpedido, datapedido, nf, valortotal, codcliente) values (null,'2023-12-30',4,100.00,4);
insert into ex2_pedido (codpedido, datapedido, nf, valortotal, codcliente) values (null,'2023-01-02',5,100.00,5);
select * from ex2_pedido;

insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto)values (null,1,1,100,1);
insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,2,2,100,2);
describe ex2_itempedido;
select * from ex2_itempedido;

drop table ex2_itempedido;
create table ex2_itempedido(
codpedido int auto_increment not null,
numeroitem int not null,
valorunitario float not null,
quantidade int not null,
codproduto int not null,
constraint fk_pedidoproduto foreign key (codproduto) references ex2_produto (codproduto),
primary key (codpedido)
);

insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,1,100,1,1);
insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,2,100,1,2);
insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,3,100,1,3);
insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,4,100,1,4);
insert into ex2_itempedido (codpedido, numeroitem, valorunitario, quantidade, codproduto) values (null,5,100,1,5);
select * from ex2_itempedido;








