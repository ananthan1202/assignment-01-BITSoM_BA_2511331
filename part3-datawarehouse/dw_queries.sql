-- Q1 Total sales
SELECT SUM(amount) FROM fact_sales;

-- Q2 Sales by product
SELECT product_id, SUM(amount)
FROM fact_sales
GROUP BY product_id;
