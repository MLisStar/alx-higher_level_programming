-- Create a database and table with a primary key.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
	(id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);