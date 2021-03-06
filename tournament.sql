-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

CREATE TABLE player (
        pname text,
        wins INTEGER,
        losses INTEGER,
        id SERIAL PRIMARY KEY );

CREATE TABLE matches (
         id integer,
         FOREIGN KEY (id) REFERENCES player(id),
         match_id INTEGER
 );
