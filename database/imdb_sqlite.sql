
-- -----------------------------------------------------
-- Table `cinema`.`genero`
-- -----------------------------------------------------
CREATE TABLE genero (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(60) NOT NULL);

-- -----------------------------------------------------
-- Table `cinema`.`filme`
-- -----------------------------------------------------
CREATE TABLE filme (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo VARCHAR(150) NOT NULL,
  ano YEAR NOT NULL);


-- -----------------------------------------------------
-- Table `cinema`.`filme_genero`
-- -----------------------------------------------------
CREATE TABLE filme_genero (
  genero_id INT NOT NULL,
  filme_id INT NOT NULL,
  PRIMARY KEY (genero_id, filme_id),
  CONSTRAINT fk_filme_genero_genero
    FOREIGN KEY (genero_id)
    REFERENCES genero (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_filme_genero_filme
    FOREIGN KEY (filme_id)
    REFERENCES filme (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `cinema`.`pessoa`
-- -----------------------------------------------------
CREATE TABLE pessoa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(120) NOT NULL);

-- -----------------------------------------------------
-- Table `cinema`.`filme_pessoa`
-- -----------------------------------------------------
CREATE TABLE filme_pessoa (
  filme_id INT NOT NULL,
  pessoa_id INT NOT NULL,
  funcao VARCHAR(100) NOT NULL CHECK(funcao IN ('Ator/Atriz', 'Diretor(a)')),
  PRIMARY KEY (filme_id, pessoa_id),
  CONSTRAINT fk_filme_pessoa_filme
    FOREIGN KEY (filme_id)
    REFERENCES filme (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_filme_pessoa_pessoa
    FOREIGN KEY (pessoa_id)
    REFERENCES pessoa (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO genero (nome) VALUES ('Ação'); 
INSERT INTO genero (nome) VALUES ('Animação');  
INSERT INTO genero (nome) VALUES ('Aventura');  
INSERT INTO genero (nome) VALUES ('Chanchada');  
INSERT INTO genero (nome) VALUES ('Cinema catástrofe');  
INSERT INTO genero (nome) VALUES ('Comédia');  
INSERT INTO genero (nome) VALUES ('Comédia romântica');  
INSERT INTO genero (nome) VALUES ('Comédia dramática');  
INSERT INTO genero (nome) VALUES ('Comédia de ação');  
INSERT INTO genero (nome) VALUES ('Cult');  
INSERT INTO genero (nome) VALUES ('Documentários'); 
INSERT INTO genero (nome) VALUES ('Drama'); 
INSERT INTO genero (nome) VALUES ('Espionagem'); 
INSERT INTO genero (nome) VALUES ('Erótico'); 
INSERT INTO genero (nome) VALUES ('Fantasia'); 
INSERT INTO genero (nome) VALUES ('Faroeste (ou western)'); 
INSERT INTO genero (nome) VALUES ('Ficção científica');
INSERT INTO genero (nome) VALUES ('Franchise/Séries'); 
INSERT INTO genero (nome) VALUES ('Guerra'); 
INSERT INTO genero (nome) VALUES ('Machinima'); 
INSERT INTO genero (nome) VALUES ('Musical'); 
INSERT INTO genero (nome) VALUES ('Filme noir'); 
INSERT INTO genero (nome) VALUES ('Policial'); 
INSERT INTO genero (nome) VALUES ('Pornochanchada'); 
INSERT INTO genero (nome) VALUES ('Pornográfico'); 
INSERT INTO genero (nome) VALUES ('Romance'); 
INSERT INTO genero (nome) VALUES ('Suspense'); 
INSERT INTO genero (nome) VALUES ('Terror (ou horror)'); 
INSERT INTO genero (nome) VALUES ('Trash');


INSERT INTO pessoa (nome) VALUES ('Michael J. Fox');
INSERT INTO pessoa (nome) VALUES ('Christopher Lloyd');
INSERT INTO pessoa (nome) VALUES ('Robert Zemeckis');

INSERT INTO filme (titulo, ano) VALUES ('De Volta para o Futuro', 1985);

INSERT INTO filme_genero (filme_id, genero_id) VALUES (1, 3); 
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (1, 1, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (1, 2, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (1, 3, 'Diretor(a)');


INSERT INTO pessoa (nome) VALUES ('Tim Robbins');
INSERT INTO pessoa (nome) VALUES ('Morgan Freeman');
INSERT INTO pessoa (nome) VALUES ('Frank Darabont');


INSERT INTO filme (titulo, ano) VALUES ('Um Sonho de Liberdade', 1994);

INSERT INTO filme_genero (filme_id, genero_id) VALUES (2, 12); 
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 4, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 5, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 6, 'Diretor(a)');





INSERT INTO pessoa (nome) VALUES ('Bill Murray');
INSERT INTO pessoa (nome) VALUES ('Andie MacDowell');
INSERT INTO pessoa (nome) VALUES ('Harold Ramis');

INSERT INTO filme (titulo, ano) VALUES ('Feitiço do Tempo', 1993);

INSERT INTO filme_genero (filme_id, genero_id) VALUES (3, 6); 
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 7, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 8, 'Ator/Atriz');
INSERT INTO filme_pessoa (filme_id, pessoa_id, funcao) VALUES (2, 9, 'Diretor(a)');





