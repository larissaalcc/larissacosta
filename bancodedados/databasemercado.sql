create database mercado character set utf8mb4 collate utf8mb4_unicode_ci;
use mercado;
create table fornecedor(
cod_fornecedor varchar (255) not null,
nome varchar (255) not null,
cidade_sede varchar (255) not null,
grupo_cod_fornecedor varchar (255),
primary key (cod_fornecedor)
);
drop table fornecedor;

create table materiais(
cod_material int primary key,
nome varchar (255),
descricao varchar (255),
cod_fornecedor varchar(255),
constraint ft_materialfornecedor foreign key (cod_fornecedor) references fornecedor (cod_fornecedor)
);
drop table materiais;
describe materiais;
show tables; 
insert into fornecedor (cod_fornecedor, nome, cidade_sede, grupo_cod_fornecedor) values ('ABC','ABC Materiais Elétricos','Vitória',null);
insert into fornecedor (cod_fornecedor, nome, cidade_sede, grupo_cod_fornecedor) values ('XYZ','XYZ Materiais de Escritório','Rio de Janeiro','Hix');
insert into fornecedor (cod_fornecedor, nome, cidade_sede, grupo_cod_fornecedor) values ('Hidra','Hidra Materiais Hidraulicos','São Paulo','Hix');
insert into fornecedor (cod_fornecedor, nome, cidade_sede, grupo_cod_fornecedor) values ('HiX','HidraX Materiais Elétricos e Hidraulicos','São Paulo',null);
describe fornecedor;
drop table materiais;
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('123','ABC','Tomada Elétrica 10A Nova','Tomada Elétrica 10A padrão novo');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('234','ABC','Disjuntor 25A','Disjuntor Elétrico 25A');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('345','XYZ','Resma Papel A4','Resma papel branco A4');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('456','XYZ','Toner Imp HR5522','Toner Impressora HR5522');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('678','Hidra','Cano PVC 1/2','Cano PVC 1/2 pol');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('679','Hidra','Toner Imp HR5522','Toner Impressora HR5522');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('680','Hidra','Medidor Hidr 1/2','Medidor Hidraulico 1/2 pol');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('681','Hidra','Joelho 1/2','Conector Joelho 1/2 pol');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('682','Hidra','Junta 1/2','Cano PVC 1/2 pol');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('1234','ABC','Tomada eletrica 20A Nova','Tomada Eletrica 20A padrao novo');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('2345','XYZ','Caneta Azul','Caneta esferografica azul');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('4567','XYZ','Grampeador','Grampeador mesa pequeno');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('4568','XYZ','Caneta Marca Texto Amarela','Caneta Marca Texto A marela');
insert into materiais (cod_material, cod_fornecedor, nome, descricao) values ('4569','XYZ','Lapis HB','Lapis Preto HB');

select * from materiais;
select * from fornecedor;










 
