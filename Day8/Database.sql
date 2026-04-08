CREATE DATABASE expense_db;

USE expense_db;


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE expenses (
    exp_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount Float,
    category VARCHAR(50),
    description VARCHAR(100),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
