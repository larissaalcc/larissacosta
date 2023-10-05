create database violencia_policial_fatal character set utf8mb4 collate utf8mb4_unicode_ci;
use violencia_policial_fatal;

create table vitima(
id_caso int primary key,
data datetime,
nome varchar (255),
idade int,
raca varchar (255),
id_genero int,
id_doenca int,
id_ameaca int,
id_arma int,
id_fuga int,
id_localizacao int,
#numero_agencia int,
constraint fk_localvitima foreign key (id_localizacao) references localizacao (id_localizacao),
#constraint fk_agenciavitima foreign key (numero_agencia) references observacao (numero_agencia),
constraint fk_fugavitima foreign key (id_fuga) references fuga (id_fuga),
constraint fk_armavitima foreign key (id_arma) references arma (id_arma),
constraint fk_ameacavitima foreign key (id_ameaca) references ameaca (id_ameaca),
constraint fk_doencavitima foreign key (id_doenca) references doenca_mental_relatada (id_doenca),
constraint fk_generovitima foreign key (id_genero) references genero (id_genero)
);

create table genero(
id_genero int auto_increment primary key,
genero varchar (10)
);

create table doenca_mental_relatada(
id_doenca int auto_increment primary key,
doenca_relatada varchar (10)
);

create table ameaca(
id_ameaca int auto_increment primary key,
ameaca varchar (50)
);

create table arma(
id_arma int auto_increment primary key,
arma varchar (20)
);


create table fuga(
id_fuga int auto_increment primary key,
fuga varchar (50)
);

create table observacao(
numero_agencia int
);

create table localizacao(
id_localizacao int auto_increment primary key,
cidade varchar (255),
estado varchar (255),
pais varchar (255),
latitude float,
longitude float,
precisao_localizacao varchar (255)
);

insert into genero (id_genero, genero) values
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "f"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "m"),
(null, "F");

select * from genero;


 