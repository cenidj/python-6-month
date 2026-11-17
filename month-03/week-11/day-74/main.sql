-- UPDATE, DELETE, AND, OR, LIMIT

-- UPDATE - Modify data
UPDATE nombre_tabla
SET columna = nuevo_valor
WHERE condicion;

-- DELETE - remove data
DELETE FROM nombre_tabla
WHERE condicion;


-- Practice
SELECT title, price, published_year
FROM books
WHERE price > 30 AND published_year > 2000
ORDER BY price DESC
LIMIT 1;