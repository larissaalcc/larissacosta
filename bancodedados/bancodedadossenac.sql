create database netflix character set utf8mb4 collate utf8mb4_unicode_ci;
use netflix;

create table usuario(
nome varchar (30) not null,
senha varchar (30) not null,
email varchar (30) not null,
telefone int not null,
endereço varchar (30) not null,
cartao int not null,
cpf int not null,
primary key (cpf)
);
describe usuario;

create table mensalidade(
mesano int not null,
valorpago int not null,
datapagamento int not null,
primary key (mesano)
);
describe mensalidade;

create table ator(
nome varchar (30) not null,
datanasc int not null,
localnascimento varchar (30) not null,
primary key (nome)
);
describe ator;

create table video(
temporada int not null,
episodio int not null,
titulo varchar (30) not null,
ano int not null,
duração int not null, 
produtora varchar (30) not null,
tipo varchar (30) not null,
primary key(titulo)
);
describe video;
show tables;
