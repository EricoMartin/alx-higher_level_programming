-- A script that creates the database hbtn_0d_usa and
-- the table cities (in the database hbtn_0d_usa)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS Cities(
        id INT AUTO_INCREMENT PRIMARY KEY,
        FOREIGN KEY(state_id INT) REFERENCES states(id),
        name VARCHAR(256) NOT NULL
        )
