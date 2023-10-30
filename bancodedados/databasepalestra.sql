drop database hub_innovation;
create database hub_innovation character set utf8mb4 collate utf8mb4_unicode_ci;

use hub_innovation;

drop table usuario;

create table usuario(
id_usuario int auto_increment primary key,
nome varchar (50),
cpf varchar (11),
email varchar (50),
data_nascimento datetime,
genero varchar (50),
telefone int,
id_palestra int,
autorizacao_de_dados_pessoais varchar (3),
concorda_em_receber_informacoes varchar (3),
constraint fk_palestra_usuario foreign key (id_palestra) references palestra (id_palestra)
);

drop table palestra;

create table palestra(
id_palestra int primary key,
nome_palestra varchar (50),
palestrante varchar (50),
quantidade_vagas int
);




insert into usuario values (null, "Ederson", "06606606695", "ederson@ederson", '1982-08-26',"Masculino", 999999999, 1, "Modelagem 3D de Personagens","sim","não");

select * from usuario;

delimiter #
create trigger tgr_palestra_insert after insert 
on usuario
for each row
begin
	update palestra set quantidade_vagas = quantidade_vagas - 1 where id_palestra = New.id_palestra; 
end#
delimiter ;
insert into palestra values (1,"Modelagem 3D de Personagens","Gabriel Ferreira",50);
select * from palestra;
	
insert into usuario values (null,"Larissa","06602885162","larissacgr05@gmail.com",'2005-08-16',"Feminino",991751168,1,"sim","sim");
select * from usuario;

delimiter #


set sql_safe_updates = 0 ;

create trigger trg_palestra_delete after delete
on usuario
for each row
begin
	update palestra set quantidade_vagas = quantidade_vagas + 1 where id_palestra = old.id_palestra;
end #

delimiter ; 