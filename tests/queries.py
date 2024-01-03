sql_queries = [
    """
    SELECT 
        (SELECT COUNT(*) FROM table2 WHERE column1 = (SELECT MAX(column2) FROM table3)) as count,
        (SELECT AVG(column3) FROM table4 WHERE column4 IN (SELECT column5 FROM table5 WHERE column6 > 50))
    FROM 
        table1
    """,
    """
    SELECT t1.column1, t2.column2
    FROM table1 as t1
    JOIN (SELECT column3, column4 FROM table2 WHERE column5 IN (SELECT column6 FROM table6)) as t2
    ON t1.column1 = t2.column3
    """,
    """
    SELECT column1
    FROM table1
    WHERE column2 > (
        SELECT AVG(column3) 
        FROM table2 
        WHERE column4 IN (
            SELECT column5 
            FROM table3 
            WHERE column6 = (
                SELECT MAX(column7) 
                FROM table4
            )
        )
    )
    """,
    """
    SELECT column1, 
           (SELECT AVG(column2) 
            FROM table2 
            WHERE column2 IN (SELECT column3 FROM table3 WHERE column3 > 100)
           ) AS avg_value 
    FROM table1 
    WHERE column1 IN (SELECT column4 FROM table4)
    AND EXISTS (SELECT column5 FROM table5) 
    """,
    """
    INSERT INTO orders (product_id, quantity) VALUES (1, 10) 
    """,
    """
    UPDATE employees SET salary = 50000 WHERE department = "HR" 
    """,
    """
    SELECT p.name, c.name FROM products p INNER JOIN categories c ON p.category_id = c.id 
    """,
    """
    UPDATE table3 SET column1 = value1 WHERE column2 = value2 
    """,
    """
    DELETE FROM table4 WHERE column1 = value1 
    """,
    """
    SELECT *
        FROM (table1
            INNER JOIN table2 ON table1.id = table2.table1_id)
            LEFT JOIN (table3
                        INNER JOIN table4 ON table3.id = table4.table3_id)
            ON table2.id = table3.table2_id
    """,
    """
    SELECT * FROM (
        SELECT * FROM table1 WHERE id IN (
            SELECT table1_id FROM table2
        )
    ) AS subquery
    INNER JOIN table3 ON subquery.id = table3.id
    """,
    """
    SELECT a.*, b.name
    FROM table1 AS a
    INNER JOIN (
        SELECT id, name FROM table2
    ) AS b ON a.table2_id = b.id
    LEFT JOIN table3 c ON a.table3_id = c.id;
    """,
    """
    WITH cte AS (
        SELECT id FROM table1
    )
    INSERT INTO table2 (id, name)
    SELECT id, 'Name' FROM cte
    WHERE id NOT IN (SELECT id FROM table3)
    """,
    """
    UPDATE table1
    SET name = (
        SELECT name FROM table2 WHERE table1.id = table2.table1_id
    )
    WHERE EXISTS (
        SELECT id FROM table3 WHERE table1.id = table3.table1_id
    )
    """,
    """
    DELETE t1
    FROM table1 t1
    INNER JOIN table2 t2 ON t1.id = t2.table1_id
    WHERE t2.name = 'SpecificName');
    """
]
