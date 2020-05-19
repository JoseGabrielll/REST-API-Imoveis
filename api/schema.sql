DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS imovel;
DROP TABLE IF EXISTS contrato;

CREATE TABLE cliente(
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    cpf CHAR(11),
    renda REAL
);

CREATE TABLE imovel(
    id_imovel SERIAL PRIMARY KEY,
    situacao INTEGER,
    valor REAL
);

CREATE TABLE contrato(
    id_contrato SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES cliente(id_cliente),
    id_imovel INTEGER REFERENCES imovel(id_imovel)
);


