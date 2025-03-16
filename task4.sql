ALTER TABLE Student
ADD COLUMN gpa NUMERIC;


UPDATE Student
SET gpa = CASE 
    WHEN name = 'Alice'   THEN 3.8
	WHEN name = 'Charlie' THEN 3.7
	WHEN name = 'David'   THEN 3.6
    WHEN name = 'Bob'     THEN 3.5
   
    ELSE gpa  -- якщо ім'я не збігається, залишаємо старе значення
END;


-- 4. UNION запит з додатковими умовами
SELECT 
    s.name,
    'High Performer' as status
FROM Student s
WHERE s.gpa >= 3.7
UNION ALL
SELECT 
    s.name,
    'Average Performer' as status
FROM Student s
WHERE s.gpa >= 3.5 AND s.gpa < 3.7
UNION ALL
SELECT 
    s.name,
    'Low Performer' as status
FROM Student s
WHERE s.gpa < 3.5;

/* Очікуваний результат:
name    | status
Alice   | High Performer
Charlie | High Performer
David   | Average Performer
Bob     | Average Performer
*/
