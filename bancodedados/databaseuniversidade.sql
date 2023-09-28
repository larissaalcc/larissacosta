create database universidade character set utf8mb4 collate utf8mb4_unicode_ci;
use universidade;

create table departamento(
	codigo int auto_increment primary key,
    nome varchar (50) not null,
    telefone varchar (30) not null,
    centro varchar (50) not null
    );
    
create table aluno(
	numeromatricula int auto_increment primary key,
    nome varchar (255) not null,
    cpf varchar (30) not null,
    endereco varchar (255) not null,
    telefone varchar (255) not null,
    datanascimento date not null,
    sexo enum ('F','M','O')not null,
    departamento varchar (255) not null,
    curso varchar (255) not null
    );
    
create table curso(
nome varchar(255) not null,
tipo enum
    
    
    
