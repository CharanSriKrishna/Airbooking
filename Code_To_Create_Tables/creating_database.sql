-- create database 
create database airbooking;

-- use the database airbooking
use airbooking;

-- create user_details table with values user_id , password , email_id , phone_no , date_created

create table user_details ( 
user_id varchar(30) primary key , 
password varchar(80)not null , 
email_id varchar(30) not null unique,  
phone_no int not null, 
name varchar(50) not null , 
date_created datetime not null 
);

-- create admin_details table with values admin_id , password , email_id 

create table admin_details ( 
admin_id varchar(30)primary key, 
password varchar(80) not null, 
email_id varchar(20) not null unique 
);

-- create flight details table with values flight_id , flight_company , flight_time , empty_seats , flight_name

create table flight_details ( 
flight_id varchar(30)primary key , 
flight_company varchar(30) not null, 
flight_time datetime, 
empty_seat int default 60, 
flight_name varchar(50) not null unique 
);

-- create flight details table with values booking_id , flight_id , user_id , booking_time 

create table Booking_details ( 
booking_id int primary key auto_increment, 
flight_id varchar(30), 
user_id varchar(30), 
booking_time datetime default current_timestamp,
Foreign key (user_id) REFERENCES user_details(user_id)ON DELETE SET NULL
ON UPDATE SET NULL,
Foreign key (flight_id) REFERENCES flight_details(flight_id)ON DELETE SET NULL
ON UPDATE SET NULL
);

