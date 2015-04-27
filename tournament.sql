-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

CREATE TABLE player (
        pname text,
        wins INTEGER,
        losses INTEGER,
        id SERIAL PRIMARY KEY );

# These tables are not used in the final implementation as they are not needed
CREATE TABLE matches (
        id integer,
        FOREIGN KEY (id) REFERENCES player(id),
        match_id INTEGER
);

# These tables are not used in the final implementation as they are not needed
CREATE TABLE results (
        id SERIAL PRIMARY KEY ,
        FOREIGN KEY (id) REFERENCES player(id),
        wins INTEGER,
        losses INTEGER
        );
