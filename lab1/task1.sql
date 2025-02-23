--1---------------------------------------------------
--створення таблиць

CREATE TABLE Department (
    dept_id SERIAL PRIMARY KEY,    -- первинний ключ
    dept_name TEXT NOT NULL
);

CREATE TABLE Professor (
    prof_id SERIAL PRIMARY KEY,    -- первинний ключ
    dept_id INT,                   -- зовнішній ключ
    salary NUMERIC NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)  -- зв'язок з Department
);

--заповнення таблиць 

INSERT INTO Department (dept_name)
VALUES
    ('Biology'),
    ('Computer Science'),
    ('Mathematics'),
    ('Physics');

INSERT INTO Professor (dept_id, salary)
VALUES
    (1, 85000.00),  -- Biology
    (2, 95000.00),  -- Computer Science
    (3, 88000.00),  -- Mathematics
    (4, 92000.00);  -- Physics

-- 1. Розширені агрегаційні функції
-- Запит 1: Агрегація з додатковими функціями

SELECT 
    d.dept_name,
    COUNT(DISTINCT p.prof_id) as professor_count,
    SUM(p.salary) as total_salary,
    AVG(p.salary) as avg_salary,
    MIN(p.salary) as min_salary,
    MAX(p.salary) as max_salary,
    STDDEV(p.salary) as salary_deviation,
    MODE() WITHIN GROUP (ORDER BY p.salary) as mode_salary
FROM Department d
LEFT JOIN Professor p ON d.dept_id = p.dept_id
GROUP BY d.dept_name;

/* Очікуваний результат:
dept_name         | professor_count | total_salary | avg_salary         | min_salary | max_salary | salary_deviation | mode_salary
Biology           |              "1"|    "85000.00"|"85000.000000000000"|"85000.00"  |"85000.00"  |"null"            |"85000.00"
Computer Science  |              "1"|     "95000.00|"95000.000000000000"|"95000.00"  |"95000.00"  |"null"            |"95000.00"
Mathematics       |              "1"|    "88000.00"|"88000.000000000000"|"88000.00"  |"88000.00"  |"null"            |"88000.00"
Physics           |              "1"|    "92000.00"|"92000.000000000000"|"92000.00"  |"92000.00"  |"null"            |"92000.00" 
*/

























