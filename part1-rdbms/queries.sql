-- Q1: Customers from Mumbai with total order value
SELECT c.customer_name, SUM(p.unit_price * oi.quantity) AS total_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.customer_city = "Mumbai"
GROUP BY c.customer_name;

-- Q2: Top 3 products by quantity sold
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 3;

-- Q3: Sales reps and number of customers handled
SELECT sr.sales_rep_name, COUNT(DISTINCT o.customer_id) AS customers
FROM sales_reps sr
JOIN orders o ON sr.sales_rep_id = o.sales_rep_id
GROUP BY sr.sales_rep_name;

-- Q4: Orders above 10000
SELECT o.order_id, SUM(p.unit_price * oi.quantity) AS total_value
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id
HAVING total_value > 10000
ORDER BY total_value DESC;

-- Q5: Products never ordered
SELECT p.product_name
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;