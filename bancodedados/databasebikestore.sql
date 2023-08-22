drop database bike_store;
create database bike_store character set utf8mb4 collate utf8mb4_unicode_ci;

use bike_store;

create table Acct_Typ_Cd_LU_Tab(
Acct_Code int not null,
Acct_Type varchar (30) not null,
primary key(Acct_code)
);
drop table Custumer;
drop table Customer;
create table Customer(
Customer_Lname varchar (30) not null,
Customer_Fname varchar (30) not null,
Cust_Street varchar (30) not null,
Cust_City varchar (30) not null,
St_Code float not null,
Cust_zip float not null,
Cust_phone float not null,
Fax_phone float not null,
Acct_code float not null,
Customer_ID int not null,
primary key (Customer_ID)
);

 show tables;

create table State_Ikup(
St_code float not null,
State_name varchar (30) not null,
primary key (St_Code)
);

drop table Supplier;
create table Supplier(
Supplier_ID float not null,
Supplier_name varchar (30) not null,
Sup_street varchar (30) not null,
Sup_city varchar (30),
St_code float not null,
Sup_zip float not null,
Sup_phone float not null,
Sup_fax float not null,
primary key (Supplier_ID)
);
show tables;

drop table Parts_Inventory;
create table Parts_Inventory(
Bar_code float not null,
Part_name varchar (30) not null,
Supplier_ID float not null,
Prt_description varchar (30) not null,
Prt_cost float not null, 
Prt_price float not null,
Quantity int not null,
primary key (Bar_code)
);
drop table Purchase_order;
 create table Purchase_order(
 Seq_ID float not null,
 Purch_dte date not null,
 Custumer_ID float not null,
 Bar_code float not null,
 Serial_num float not null,
 Model_ID float not null,
 Quantity int not null,
 Price float not null,
 primary key (Seq_ID)
 );
 
 create table Bike_description(
 Model_ID float not null, 
 Model_name varchar (30) not null,
 Inv_price float not null,
 Sale_price float not null,
 Description varchar (30) not null,
 primary key(Model_ID)
 );
 
 create table Bike_inventary(
 Seq_ID float not null, 
 Serial_number float not null,
 Supplier_ID float not null,
 Inventory_dte date not null,
 Model_ID float not null,
 primary key(Seq_ID)
 );
 
 drop table Custumer_Acct_Hist1;
 create table Customer_Acct_Hist1(
 Customer_ID float not null,
 Trans_dte date not null,
 Trans_code float not null,
 Old_acct_balance float not null,
 New_acct_balance float not null,
 primary key (Customer_ID)
 );
 
 create table Transaction_code(
 Trans_code float not null,
 Transaction_description varchar (50) not null,
 primary key (Trans_code)
 );
 
describe Bike_description;






