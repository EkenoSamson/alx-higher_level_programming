-- create table unique_id
-- default for id is 1
-- id is unique

CREATE TABLE IF NOT EXISTS unique_id
(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
