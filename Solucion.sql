-- 1.	Cantidad de órdenes y monto total de órdenes por ciudad, país. Nivel año-mes
/*Se me ocurren dos interpreteciones de la letra: en la Solucion 1 los resultados son agrupados por la ciudad, 
devolviendo a demas la columna de pais; la solucion 2 la aplico porque tambien entiendo que la letra puede llegar a estar pidiendo 
que ademas de dar los resultados agrupados por ciudad, se realice otra cosulta para dar los resultados agrupados por país.
*/

-- Solucion 1
SELECT count(id) AS 'Cantidad de Ordenes', SUM(order_amount) AS 'Monto total', city AS 'Ciudad', country AS 'Pais'
FROM orders
GROUP BY city
ORDER BY order_date;

-- Solucion 2
SELECT count(id) AS 'Cantidad de Ordenes', SUM(order_amount) AS 'Monto total', country AS 'Pais'
FROM orders
GROUP BY country
ORDER BY order_date;

-- 2. Cantidad de restaurantes en Uruguay, por categoría de restaurante, 
-- que tienen por lo menos un monto mensual (order amount) en abril 2017 mayor a 1000.

SELECT restaurants.category, COUNT(restaurants.id) AS 'Restaurantes en Uruguay', Monto AS 'Monto mensual mayores a 1000 en abril de 2017'
FROM restaurants
JOIN (
	SELECT restaurant_id, SUM(order_amount) AS Monto 
    FROM orders 
    WHERE country = 'Uruguay'
    AND order_date
    LIKE '2017-04%'
    GROUP BY restaurant_id
    ) orders
ON restaurants.id = orders.restaurant_id
WHERE Monto > 1000
GROUP BY category;

-- 3.	Cantidad de restaurantes distintos en que compró cada usuario en todo el período. 

SELECT user_id AS 'Id del Usuario', COUNT(DISTINCT restaurant_id) AS 'Cantidad de restaurantes utilizados'
FROM orders
GROUP BY user_id;

