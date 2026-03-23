CREATE TABLE fact_sales (
    sale_id INT,
    customer_id INT,
    product_id INT,
    amount DECIMAL(10,2)
);

CREATE TABLE dim_customer (
    customer_id INT,
    name VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id INT,
    name VARCHAR(100)
);
