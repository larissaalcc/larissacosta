create database fabrica character set utf8mb4 collate utf8mb4_unicode_ci;
use fabrica;
create table fabricas(
id int not null,
nome varchar (30) not null,
endereco_de_imagem varchar (50) not null,
texto varchar (50) not null,
primary key(id)
);

drop table edital;
create table edital(
id_edital int not null,
data_inicio date not null,
data_fim date not null,
nome varchar (30) not null,
numero_do_edital int not null,
endereco_arquivo varchar (50) not null,
primary key (id_edital)
);

drop table banco_de_dados;
create table banco_de_talentos(
id int not null,
nome varchar (30) not null,
cpf int not null,
rg int not null,
data_nascimento date not null,
endereco varchar (50) not null, 
fone float not null,
linkedln varchar (30) not null,
primary key(id)
);

create table adm(
id int not null,
nome varchar (30) not null,
cpf int not null,
senha varchar (30) not null,
fone int not null,
email varchar (30) not null,
primary key (id)
);

drop table vagas_psg;
create table vagas_psg(
id int not null,
nome varchar (30) not null,
data_nascimento date not null,
nome_responsavel varchar (30) not null,
cpf_responsavel int not null,
email_responsavel varchar (30) not null,
fone_responsavel int not null,
id_edital int not null,
constraint fk_vagaedital foreign key (id_edital) references edital(id_edital),
escolaridade varchar (30) not null,
primary key(id)
);

describe vagas_psg;

create table vagas_empresas(
id int not null,
nome_empresa varchar (30) not null,
cnpj int not null,
fone int not null,
representante varchar (30) not null,
email_representante varchar (30) not null,
descricao_vaga varchar (50) not null,
primary key (id)
);

show tables;

create table projetos(
id int not null,
nome_empresa varchar (30) not null,
cnpj int not null,
nome_titular varchar (30) not null,
cpf int not null,
fone int not null,
descricao_do_projeto varchar (100) not null,
email varchar (30) not null,
primary key(id)
);






















