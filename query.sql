create database Ecole;
use Ecole;
create table etudiant ( 
    student_id int primary key auto_increment,
    nom varchar(100),
    prenom varchar(100),
    numero_salle int,
    telephone varchar(20) not null unique,
    email varchar(100) unique,
    annee_obtention year,
    numero_classe  int 
) ;

create table enseignants (
    teacher_id int primary key auto_increment,
    prenom varchar(50),
    nom varchar(50),
    numero_salle varchar(50),
    departement varchar(100),
    annee_obtention  year,
    email varchar(100) unique,
    telephone varchar(50) not null unique,
    numero_classe int 
    );

insert into etudiant (prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
values ('Mark', 'Watney', 101, '777-555-1234', null, 2035, 5),
('Alice', 'Johnson', 102, '777-555-5678', 'alice.johnson@example.com', 2024, 6),
('Bob', 'Smith', 103, '777-555-8765', 'bob.smith@example.com', 2025, 5),
('Charlie', 'Brown', 104, '777-555-4321', null, 2026, 6),
('Daisy', 'Miller', 105, '777-555-9876', 'daisy.miller@example.com', 2024, 7);

insert into enseignants (prenom, nom, departement, email, telephone, numero_classe)
values ('Jonas', 'Salk', 'Biologie', 'jsalk@school.org', '777-555-4321', 5),
('Emily', 'Davis', 'Mathématiques', 'edavis@school.org', '777-555-6789', 6),
('Michael', 'Brown', 'Physique', 'mbrown@school.org', '777-555-9876', 5),
('Sarah', 'Williams', 'Chimie', 'swilliams@school.org', '777-555-1234', 7),
('David', 'Wilson', 'Informatique', 'dwilson@school.org', '777-555-1111', 6);
