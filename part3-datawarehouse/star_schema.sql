CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    month_name VARCHAR(20)
);

CREATE TABLE dim_store (
    store_id SERIAL PRIMARY KEY,
    store_name VARCHAR(100),
    store_city VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE fact_sales (
    sales_id SERIAL PRIMARY KEY,
    date_id DATE,
    store_id INT,
    product_id INT,
    units_sold INT,
    unit_price DECIMAL(10,2),
    revenue DECIMAL(12,2),

    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (store_id) REFERENCES dim_store(store_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);

INSERT INTO dim_date VALUES
('2023-08-29',2023,8,'August'),
('2023-12-12',2023,12,'December'),
('2023-02-05',2023,2,'February'),
('2023-02-20',2023,2,'February'),
('2023-01-15',2023,1,'January'),
('2023-08-09',2023,8,'August'),
('2023-03-31',2023,3,'March'),
('2023-10-26',2023,10,'October'),
('2023-12-08',2023,12,'December')
('2023-08-15',2023,8,'August');

INSERT INTO dim_store (store_name,store_city) VALUES
('Chennai Anna','Chennai'),
('Delhi South','Delhi'),
('Bangalore MG','Bangalore'),
('Pune FC Road','Pune'),
('Mumbai Central','Mumbai'),

INSERT INTO dim_product (product_name,category) VALUES
('Speaker','Electronics'),
('Tablet','Electronics'),
('Phone','Electronics'),
('Smartwatch','Electronics'),
('Headphones','Electronics'),
('Jeans','Clothing'),
('Jacket','Clothing'),
('T-Shirt','Clothing'),
('Saree','Clothing'),
('Atta 10kg','Groceries'),
('Milk 1L','Groceries'),
('Biscuits','Groceries'),
('Rice 5kg','Groceries'),
('Pulses 1kg','Groceries');

INSERT INTO fact_sales 
(date,store_id,product_id,units_sold,unit_price,revenue) VALUES 
('2023-08-29',1,1,3,49262.78,147788.34),
('2023-12-12',1,2,11,23226.12,255487.32),
('2023-02-05',1,3,20,48703.39,974067.80),
('2023-02-02',2,2,14,23226.12,325165.68),
('2023-01-15',1,4,10,58851.01,588510.10),
('2023-08-09',3,7,12,52464.00,629568.00),
('2023-03-31',4,4,6,58851.01,353106.06),
('2023-10-26',4,5,16,2317.47,37079.52),
('2023-12-08',3,7,9,27469.99,247229.91),
('2023-08-15',3,4,3,58851.01,176553.03);

