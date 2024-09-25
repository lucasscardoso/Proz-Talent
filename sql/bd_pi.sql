CREATE TABLE Cliente (
    id_usuario SERIAL PRIMARY KEY,
    nomeCompleto_usuario VARCHAR(100) NOT NULL,
    cpf_usuario VARCHAR(11) NOT NULL UNIQUE,
    dataNascimento_usuario DATE NOT NULL
);

CREATE TABLE Conta (
    id_usuario INT,
    nome_usuario VARCHAR(50) NOT NULL,
    senha_usuario VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario),
    FOREIGN KEY (id_usuario) REFERENCES Cliente(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Filme (
    id_filme  SERIAL PRIMARY KEY,
    nome_filme VARCHAR(100) NOT NULL,
    genero_filme VARCHAR(50) NOT NULL
);



CREATE TABLE Serie (
    id_serie serial  PRIMARY KEY ,
    nome_serie VARCHAR(100) NOT NULL,
    genero_serie VARCHAR(50) NOT NULL
);

CREATE TABLE Anime (
    id_anime Serial PRIMARY KEY ,
    nome_anime VARCHAR(100) NOT NULL,
    genero_anime VARCHAR(50) NOT NULL
);

CREATE TABLE CompraVenda (
    id_compra SERIAL PRIMARY KEY,
    id_usuario INT,
    tipo_compra VARCHAR(50)
);

CREATE TABLE conteudo (
    id_conteudo SERIAL PRIMARY KEY,
    tipo_conteudo VARCHAR(100) NOT NULL,
    id_filme INT,
    id_serie INT,
    id_anime INT,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_serie) REFERENCES Serie(id_serie) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_anime) REFERENCES Anime(id_anime) ON DELETE CASCADE ON UPDATE CASCADE
);
