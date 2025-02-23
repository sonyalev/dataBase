DELETE FROM Course;

ALTER TABLE Course
ADD COLUMN dept_id INT;

ALTER TABLE Course
ADD CONSTRAINT fk_course
FOREIGN KEY (dept_id) REFERENCES Department(dept_id) ON DELETE CASCADE;

INSERT INTO Course (course_id, course_name, dept_id) VALUES 
    (1, 'Advanced Algorithms', 2),
	(2, 'Quantum Mechanics', 4),
    (3, 'Molecular Biology', 1),
	(4, 'Linear Algebra', 3);   

DELETE FROM Professor;

ALTER TABLE Professor
ADD COLUMN name TEXT NOT NULL;

INSERT INTO Professor (dept_id, salary, name)
VALUES
    (1, 85000.00, 'Dr. Brown'),  -- Biology
    (2, 95000.00, 'Dr. Smith'),  -- Computer Science
    (3, 88000.00, 'Dr. Johnson'),  -- Mathematics
    (4, 92000.00, 'Dr. Williams');  -- Physics

INSERT INTO Student (student_id, name) VALUES 
    (3, 'David'),
	(4, 'Bob'),
	(5, 'Grace');  
ALTER TABLE Enrollment
ADD COLUMN professor_id INT;

ALTER TABLE Enrollment
ADD CONSTRAINT fk_professor
FOREIGN KEY (professor_id) REFERENCES Professor(prof_id);


DELETE FROM Enrollment;	
INSERT INTO Enrollment (student_id, course_id, grade, professor_id) VALUES
    (1, 1, 4.00, 6),
    (3, 2, 4.00, 8),
    (2, 3, 3.80, 5), 
    (4, 4, 3.50, 7),
    (5, 4, 3.70, 7);  


-- 3. Складні JOIN запити
-- Запит 3: Повний аналіз курсів, викладачів, студентів
SELECT 
    c.course_name,
    p.name as professor,
    d.dept_name,
    COUNT(DISTINCT e.student_id) as enrolled_students,
    ROUND(AVG(e.grade), 2) as avg_course_grade,
    MAX(e.grade) as max_grade,
    MIN(e.grade) as min_grade
FROM Course c
LEFT JOIN Enrollment e ON c.course_id = e.course_id
LEFT JOIN Professor p ON e.professor_id = p.prof_id
LEFT JOIN Department d ON c.dept_id = d.dept_id
GROUP BY c.course_name, p.name, d.dept_name
ORDER BY avg_course_grade DESC;

/* Очікуваний результат:
course_name          | professor    | dept_name        | enrolled_students | avg_course_grade | max_grade | min_grade
"Advanced Algorithms"|"Dr. Smith"   |"Computer Science"|"1"                |"4.00"            |"4.00"     |"4.00"
"Quantum Mechanics"  |"Dr. Williams"|"Physics"	        |"1"                |"4.00"            |"4.00"     |"4.00"
"Molecular Biology"  |"Dr. Brown"   |"Biology"         |"1"                |"3.80"            |"3.80"     |"3.80"
"Linear Algebra"     |"Dr. Johnson" |"Mathematics"	    |"2"                |"3.60"            |"3.70"     |"3.50"*/
