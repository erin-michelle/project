JOINS

1:1		SELECT column_name(s) 
		FROM table1
		JOIN table2 ON table2.column_name = table1.column_name;

1:M		SELECT column_name(s) 
		FROM table1
		JOIN table2 ON table2.column_name = table1.column_name;
		connects where ids match

		JOIN sites ON clients.id = sites.client_id
		JOIN leads ON sites.id = leads.site_id;

	LEFT JOIN

		SELECT column_name(s) FROM table1		
		LEFT JOIN table2 ON table1.column_name = table2.column_name
		WHERE table1.column_name = ?;

	RIGHT JOIN (rare on a 1:M)

		SELECT column_name(s) FROM table1		
		LEFT JOIN table2 ON table1.column_name = table2.column_name
		WHERE table1.column_name = ?;

M:M 	SELECT * FROM table1
		JOIN table2 ON table1.column_name = table2.column_name
		JOIN table3 ON table3.column_name = table2.column_name;

	SELF JOINS (remember AS)

		SELECT table.column_name AS something, table1.column_name AS somethingelse
		FROM users
		LEFT JOIN follows ON users.id = follows.something_id
		LEFT JOIN table AS table1 ON table1.id = follows.somethingelse_id
		WHERE users.id = 2
		GROUP BY users.id;

**JOIN won't show table records that don't have a partner (null)
**LEFT JOIN will show them



MySQL Queries - CRUD

CREATE =	INSERT INTO table (column_name1,column_name2,...) VALUES (column_value, column_value, ...);

READ = 		SELECT * FROM users WHERE first_name LIKE "%e" -- will end in 'e'
			ORDER BY birthday DESC;

UPDATE =	UPDATE table_name SET column_name1 = 'new_value', column_name2 = 'new_value' WHERE = ?;
				-------MUST USE A WHERE---------TRUST ME---------I KNOW THINGS------------

DELETE =	DELETE FROM table_name WHERE id = ?;
  				-------MUST USE A WHERE---------TRUST ME---------I KNOW THINGS------------
  				(MAY NEED ENTER THIS IN WORKBENCH FIRST BEFORE BEING PERMITTED TO DELETE)
  			SET SQL_SAFE_UPDATES = 0;



 NESTED QUERIES

 			SELECT * FROM table 
 			WHERE column_name NOT IN (SELECT * FROM table WHERE column_name = ?);

 			SELECT * FROM table 
 			WHERE column_name != ?;

 			SELECT * FROM table 
 			WHERE column_name <> ?;



