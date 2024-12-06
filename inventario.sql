create database inventario;
use inventario;

create table equipamentos(
codigo int primary key auto_increment,
descricao varchar(200) not null,
localizacao varchar(200) not null);

