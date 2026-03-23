-- Q1: Total Sales by Category per Month
SELECT
d.month,
p.category,
SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY d.month,p.category
ORDER BY d.month;

--Q2: Top 2 Stores by Revenue 
SELECT
s.store_name,
SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_store s ON f.store_id = s.store_id
GROUP BY s.store_name
ORDER BY total_revenue DESC
LIMIT 2;

--Q3 Month-over-Month Sales Trend 
SELECT
d.year,
d.month,
SUM(f.revenue) AS monthly_sales
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year,d.month
ORDER BY d.year,d.month;



