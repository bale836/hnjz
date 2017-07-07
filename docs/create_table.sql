create database hnjz;
use hnjz;
drop table h_s_order;
create table h_s_order
(
orderID serial not null primary key,
customerID int,
productID int,
amount int,
total DEC(10,2),
discount int,
status int,
deliverDeadline DATE,
createTime DATETIME
);

drop table h_s_product;
create table h_s_product
(
productID serial not null primary key,
productName varchar(63),
productPrice Dec(10,2),
productRemark varchar(255)
);

drop table h_s_product_integration;
create table h_s_product_integration
(
productID serial not null primary key,
materialID int,
amount int
);

drop table h_s_inventory;
create table h_s_inventory
(
productID serial not null primary key,
amount int
);

drop table h_p_order;
create table h_p_order
(
orderID serial not null primary key,
providerID int,
materialID int,
amount int,
total DEC(10,2),
discount int,
status int,
deliverDeadline DATE,
createTime DATETIME
);

drop table h_p_material;
create table h_p_material
(
materialID serial not null primary key,
materialName varchar(63),
materialRemark varchar(255)
);

drop table h_p_inventory;
create table h_p_inventory
(
materialID serial not null primary key,
amount int
);

drop table h_employee;  -- Use auth_user of django
create table h_employee
(
employeeID serial not null primary key,
userName varchar(63),
password varchar(255),
roleID int
);

drop table h_role;  -- Use auth_group of django
create table h_role
(
roleID serial not null primary key,
roleName varchar(63),
roleRemark varchar(255)
);

drop table h_customer;
create table h_customer
(
customerID serial not null primary key,
customerName varchar(63),
customerAddress varchar(255),
customerOC varchar(20),
customerContactor varchar(63),
customerContactPhone varchar(12)
);

drop table h_provider;
create table h_provider
(
providerID serial not null primary key,
providerName varchar(63),
providerAddress varchar(255),
providerOC varchar(20),
providerContactor varchar(63),
providerContactPhone varchar(12)
);
