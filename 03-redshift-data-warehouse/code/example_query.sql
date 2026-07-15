-- Top 5 products by revenue in 2023
SELECT product_id, SUM(quantity * price) AS revenue
FROM sales
WHERE EXTRACT(YEAR FROM sale_date) = 2023
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 5;
