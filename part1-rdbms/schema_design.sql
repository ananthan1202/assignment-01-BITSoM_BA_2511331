-- Customers
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_city VARCHAR(50)
);

-- Products
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

-- Sales Representatives
CREATE TABLE sales_reps (
    sales_rep_id VARCHAR(10) PRIMARY KEY,
    sales_rep_name VARCHAR(100),
    sales_rep_email VARCHAR(100),
    office_location VARCHAR(150)
);

-- Orders
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    sales_rep_id VARCHAR(10),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (sales_rep_id) REFERENCES sales_reps(sales_rep_id)
);

-- Order Items
CREATE TABLE order_items (
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Sample inserts

INSERT INTO customers VALUES
('C002','Priya Sharma','priya@gmail.com','Delhi'),
('C001','Rohan Mehta','rohan@gmail.com','Mumbai'),
('C006','Neha Gupta','neha@gmail.com','Delhi'),
('C003','Amit Verma','amit@gmail.com','Bangalore'),
('C005','Vikram Singh','vikram@gmail.com','Mumbai');

INSERT INTO products VALUES
('P001','Laptop','Electronics',55000),
('P002','Mouse','Electronics',800),
('P003','Desk Chair','Furniture',8500),
('P004','Notebook','Stationery',120),
('P005','Headphones','Electronics',3200);

INSERT INTO sales_reps VALUES
('SR01','Deepak Joshi','deepak@corp.com','Mumbai HQ'),
('SR02','Anita Desai','anita@corp.com','Delhi Office'),
('SR03','Ravi Kumar','ravi@corp.com','Bangalore Office');

INSERT INTO orders VALUES
('ORD1027','C002','SR02','2023-11-02'),
('ORD1114','C001','SR01','2023-08-06'),
('ORD1153','C006','SR01','2023-12-14'),
('ORD1002','C002','SR02','2023-01-17'),
('ORD1118','C006','SR02','2023-11-10');

INSERT INTO order_items VALUES
('OORD1027','P004',4),
('ORD1114','P007',2),
('ORD1153','P007',3),
('ORD1002','P005',1),
('ORD1118','P007',5);


