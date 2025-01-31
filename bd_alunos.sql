create database bd_alunos;
use bd_alunos;
create table alunos(
codigo int primary key auto_increment,
nome varchar(100),
curso varchar(100),
turno varchar(100),
atleta varchar(100),
bolsista varchar(100),
observacao varchar(200));