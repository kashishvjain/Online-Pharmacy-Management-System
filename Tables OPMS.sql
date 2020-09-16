create table customer (
  CID varchar(8) PRIMARY KEY check(CID like 'C%'), 
  first_name varchar(20) not null, 
  middle_name varchar(20), 
  sur_name varchar(20), 
  street varchar(50) not null, 
  city varchar(20) not null, 
  pincode int not null, 
  state varchar(20), 
  gender char(1) check(
    gender in ('M', 'F', 'O')
  ), 
  phone decimal(10, 0) unique, 
  password varchar(15), 
  DOB date, 
  age decimal(4, 2)
);

CREATE TABLE generic(
  generic_id INT PRIMARY KEY, 
  generic_name VARCHAR(100)
);

CREATE TABLE pharmacy (
  PNAME VARCHAR(20),  
  STREET_NAME varchar(50), 
  CITY varchar(20), 
  PINCODE int, 
  STATE varchar(20), 
  PID varchar(10) PRIMARY KEY
);

CREATE TABLE medicine(
  exp_date DATE, 
  unit_price DECIMAL(6, 2), 
  prescription TINYINT(1), 
  effect VARCHAR(100), 
  side_effect VARCHAR(100), 
  dose VARCHAR(100), 
  name VARCHAR(100), 
  brand VARCHAR(100), 
  stock INT, 
  id INT PRIMARY KEY, 
  generic_id INT, 
  pharmacy_id varchar(10), 
  FOREIGN KEY(generic_id) REFERENCES generic(generic_id), 
  FOREIGN KEY(pharmacy_id) REFERENCES pharmacy(PID)
);

CREATE TABLE transact(
  CID varchar(8), 
  INVOICE_NO VARCHAR(10), 
  SUCCESS TINYINT(1), 
  TID varchar(10) PRIMARY KEY, 
  ITEM_CODE INT, 
  FOREIGN KEY(ITEM_CODE) REFERENCES medicine(id), 
  FOREIGN KEY(CID) REFERENCES customer(CID)
);



INSERT INTO customer 
(CID, first_name, middle_name,sur_name,street,city,pincode,state,gender,phone,password,DOB)
values
('C0000001', 'Adwait', 'Ajay', 'Hegde', 'Sector 9 Mira Road','Thane', 401107,'Maharashtra','M',9833512267,'password','20010117'),
('C0000002', 'Yash', NULL, 'Jagtap', 'Khau Gali, Malad','Mumbai', 401005,'Maharashtra','M',9735563567,'passcode','20010612'),
('C0000003', 'Kashish', 'D', 'Jain', '9-C20 Bandra','Mumbai', 400011,'Maharashtra','M',7833548139,'wordpass','20010322'),
('C0000004', 'Jash', 'J', 'J', 'C-56, Charter Road','Mumbai', 400057,'Maharashtra','M',9898922267,'pass','20001020'),
('C0000005', 'Payal', 'Naitk', 'Shah', 'N Nivas, Malad','Alappuzha', 601078,'Kerala','F',8833512267,'passkey','20020228'),
('C0000006', 'Naitik', 'Amar', 'Shrivasthav', 'B9 Chedder Road','Mumbai', 400023,'Maharashtra','O',7865412267,'keypass','20010717');

INSERT INTO generic VALUES
    (1,'Paracetamol'),
    (2,'Acetylsalicylic Acid')
;

INSERT INTO pharmacy(PNAME,STREET_NAME,CITY,PINCODE,STATE,PID) VALUES
    ('New Pharma','110, N C Road, Dispensary Road','Bangalore','560001','Karnataka','P0001'),
    ('General Medicine','2, Warden Court, Gowalia Tank Rd','Mumbai','40001','Maharashtra','P0002');


INSERT INTO medicine (id,exp_date,unit_price,prescription,effect,side_effect,dose,name,brand,stock,generic_id,pharmacy_id) VALUES
    (1,'20300401',200,1,'Reduces Headache',NULL,2,'Dolo 65','Sun Pharma',100,1,'P0001'),
    (2,'20240705',180,1,'Reduces Headache',NULL,2,'Dolo 65','Sun Pharma',20,1,'P0002'),
    (3,'20220205',100,0,'Prevention of Heart Attack','Indigestion',1,'Ecosprin','USV',100,2,'P0001'),
    (4,'20210904',120,0,'Prevention of Heart Attack','Indigestion',1,'Ecosprin','USV',50,2,'P0002'),
    (5,'20211010',300,0,'Prevention of Heart Attack',NULL,1,'Loprin','Unichem',150,2,'P0002')
;

INSERT INTO transact (CID,INVOICE_NO,SUCCESS,TID,ITEM_CODE) VALUES
('C0000001','I0001',1,1,1),
('C0000003','I0002',1,2,3),
('C0000002','I0003',1,3,5),
('C0000003','I0004',1,4,2),
('C0000005','I0005',1,5,4)
;



SELECT 
  INVOICE_NO,
  customer.first_name,
  medicine.name,
  medicine.unit_price
FROM transact 
JOIN medicine
  ON transact.ITEM_CODE = medicine.id
JOIN customer
  ON transact.CID = customer.CID;