DROP DATABASE IF EXISTS join_exercise;
CREATE DATABASE join_exercise;

USE join_exercise;

CREATE TABLE customers (
  customer_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  PRIMARY KEY(customer_id)
);

CREATE TABLE complaints (
  complaint_id INT NOT NULL AUTO_INCREMENT,
  complaint_date_time DATETIME DEFAULT NOW(),
  complaint_text VARCHAR(1000) NOT NULL,
  customer_id INT,
  PRIMARY KEY(complaint_id)
);

INSERT INTO customers (first_name, last_name) VALUES ('Elton', 'John');
INSERT INTO customers (first_name, last_name) VALUES ('Roger', 'Waters');
INSERT INTO customers (first_name, last_name) VALUES ('Lady', 'Gaga');
INSERT INTO customers (first_name, last_name) VALUES ('Freddie', 'Mercury');
INSERT INTO customers (first_name, last_name) VALUES ('Rihanna', 'Fenty');

INSERT INTO complaints (complaint_text, customer_id) VALUES ("I'm still standing, but this standing desk is horrible, can I get a refund please?", 1);
INSERT INTO complaints (complaint_text, customer_id) VALUES ("I've always been mad, I know I've been mad. But not mad enough to accept a guitar of such bad quality!", 2);
INSERT INTO complaints (complaint_text, customer_id) VALUES ("Hello, hello baby you called, I can't hear a thing. I have got no service with this phone-a-hey-hey. Do not recommend!", 3);
INSERT INTO complaints (complaint_text, customer_id) VALUES ("EEEEEEOOOOO, EEEEE-EEEEOOOOO... This microphone is not powerful enough to do the EEEOOOs at Wembley. The website claimed too much", 4);
INSERT INTO complaints (complaint_text, customer_id) VALUES ("This Umbrella-ela-ela-ee-ee lets the rain through, oh wait that's Riri's order... nvm!", 3);
INSERT INTO complaints (complaint_text, customer_id) VALUES ("This notepad is awful to write on... How am I supposed to write another breakup album with my age as the Title..?", 6);

SELECT * FROM customers;
SELECT * FROM complaints;
